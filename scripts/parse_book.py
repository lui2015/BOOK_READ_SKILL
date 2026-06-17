#!/usr/bin/env python3
"""
parse_book.py — Extract text and chapter structure from PDF/EPUB files.

Usage:
    python3 parse_book.py <input_file> [--output <output.json>]

Output JSON format:
{
    "title": "Book Title",
    "format": "pdf|epub",
    "total_pages": 300,
    "chapters": [
        {
            "number": 1,
            "title": "Chapter Title",
            "content": "Full text...",
            "page_start": 1,
            "page_end": 25
        }
    ],
    "raw_text": "Full book text...",
    "metadata": {
        "author": "",
        "isbn": "",
        "language": ""
    }
}

Dependencies:
    pip install PyPDF2 ebooklib beautifulsoup4
"""

import argparse
import json
import os
import re
import sys


def parse_pdf(filepath):
    """Extract text and structure from PDF."""
    try:
        from PyPDF2 import PdfReader
    except ImportError:
        print("ERROR: PyPDF2 not installed. Run: pip install PyPDF2", file=sys.stderr)
        sys.exit(1)

    reader = PdfReader(filepath)
    total_pages = len(reader.pages)

    # Extract all text
    pages_text = []
    for i, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        pages_text.append({"page": i + 1, "text": text})

    raw_text = "\n".join(p["text"] for p in pages_text)

    # Extract metadata
    metadata = {}
    if reader.metadata:
        metadata["author"] = reader.metadata.get("/Author", "")
        metadata["title"] = reader.metadata.get("/Title", "")

    # Try to detect chapters from TOC or heading patterns
    chapters = detect_chapters_from_text(pages_text)

    title = metadata.get("title", "") or os.path.splitext(os.path.basename(filepath))[0]

    return {
        "title": title,
        "format": "pdf",
        "total_pages": total_pages,
        "chapters": chapters,
        "raw_text": raw_text,
        "metadata": metadata,
    }


def parse_epub(filepath):
    """Extract text and structure from EPUB."""
    try:
        import ebooklib
        from ebooklib import epub
        from bs4 import BeautifulSoup
    except ImportError:
        print(
            "ERROR: ebooklib/beautifulsoup4 not installed. Run: pip install ebooklib beautifulsoup4",
            file=sys.stderr,
        )
        sys.exit(1)

    book = epub.read_epub(filepath)

    # Extract metadata
    metadata = {}
    title_meta = book.get_metadata("DC", "title")
    if title_meta:
        metadata["title"] = title_meta[0][0]
    creator_meta = book.get_metadata("DC", "creator")
    if creator_meta:
        metadata["author"] = creator_meta[0][0]
    lang_meta = book.get_metadata("DC", "language")
    if lang_meta:
        metadata["language"] = lang_meta[0][0]
    isbn_meta = book.get_metadata("DC", "identifier")
    if isbn_meta:
        metadata["isbn"] = isbn_meta[0][0]

    # Extract chapters
    chapters = []
    chapter_num = 0
    all_text_parts = []

    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            soup = BeautifulSoup(item.get_content(), "html.parser")
            text = soup.get_text(separator="\n", strip=True)

            if not text.strip():
                continue

            all_text_parts.append(text)

            # Try to extract chapter title from first heading
            heading = soup.find(["h1", "h2", "h3"])
            if heading:
                chapter_num += 1
                chapters.append(
                    {
                        "number": chapter_num,
                        "title": heading.get_text(strip=True),
                        "content": text,
                        "page_start": None,
                        "page_end": None,
                    }
                )
            elif chapters:
                # Append to last chapter if no heading found
                chapters[-1]["content"] += "\n\n" + text
            else:
                # Pre-chapter content (foreword, etc.)
                chapter_num += 1
                chapters.append(
                    {
                        "number": chapter_num,
                        "title": "前言/引言",
                        "content": text,
                        "page_start": None,
                        "page_end": None,
                    }
                )

    raw_text = "\n\n".join(all_text_parts)
    title = metadata.get("title", "") or os.path.splitext(os.path.basename(filepath))[0]

    return {
        "title": title,
        "format": "epub",
        "total_pages": None,
        "chapters": chapters,
        "raw_text": raw_text,
        "metadata": metadata,
    }


def detect_chapters_from_text(pages_text):
    """Detect chapter boundaries from page text using heading patterns."""
    # Common chapter heading patterns (Chinese and English)
    patterns = [
        r"^第[一二三四五六七八九十百零\d]+章[\s：:].+",
        r"^Chapter\s+\d+[\s：:].+",
        r"^CHAPTER\s+\d+[\s：:].+",
        r"^Part\s+\d+[\s：:].+",
        r"^第[一二三四五六七八九十百零\d]+部分[\s：:].+",
        r"^第[一二三四五六七八九十百零\d]+节[\s：:].+",
        r"^\d+\.\s+[A-Z\u4e00-\u9fff].{2,50}$",
    ]

    chapters = []
    current_chapter = None
    chapter_num = 0

    for page_info in pages_text:
        lines = page_info["text"].split("\n")
        for line in lines:
            line = line.strip()
            if not line:
                continue

            is_chapter_heading = False
            for pattern in patterns:
                if re.match(pattern, line, re.MULTILINE):
                    is_chapter_heading = True
                    break

            if is_chapter_heading:
                if current_chapter:
                    current_chapter["page_end"] = page_info["page"] - 1
                    chapters.append(current_chapter)

                chapter_num += 1
                current_chapter = {
                    "number": chapter_num,
                    "title": line,
                    "content": "",
                    "page_start": page_info["page"],
                    "page_end": None,
                }
            elif current_chapter:
                current_chapter["content"] += line + "\n"

    # Add the last chapter
    if current_chapter:
        current_chapter["page_end"] = pages_text[-1]["page"] if pages_text else None
        chapters.append(current_chapter)

    # If no chapters detected, treat entire book as one chapter
    if not chapters:
        all_text = "\n".join(p["text"] for p in pages_text)
        chapters = [
            {
                "number": 1,
                "title": "全文",
                "content": all_text,
                "page_start": 1,
                "page_end": pages_text[-1]["page"] if pages_text else None,
            }
        ]

    return chapters


def main():
    parser = argparse.ArgumentParser(description="Extract text and structure from PDF/EPUB")
    parser.add_argument("input_file", help="Path to PDF or EPUB file")
    parser.add_argument("--output", "-o", help="Output JSON file path (default: stdout)")
    args = parser.parse_args()

    filepath = args.input_file

    if not os.path.exists(filepath):
        print(f"ERROR: File not found: {filepath}", file=sys.stderr)
        sys.exit(1)

    ext = os.path.splitext(filepath)[1].lower()

    if ext == ".pdf":
        result = parse_pdf(filepath)
    elif ext == ".epub":
        result = parse_epub(filepath)
    else:
        print(f"ERROR: Unsupported format: {ext}. Only .pdf and .epub are supported.", file=sys.stderr)
        sys.exit(1)

    # Output
    output_json = json.dumps(result, ensure_ascii=False, indent=2)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(output_json)
        print(f"Output written to: {args.output}", file=sys.stderr)
    else:
        print(output_json)


if __name__ == "__main__":
    main()
