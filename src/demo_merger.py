"""
Demo PDF report merger.
Uses only fictional sample files and generic section labels.
This is a portfolio-safe demonstration, not the original internal tool.
"""
from __future__ import annotations

import argparse
import os
from collections import defaultdict
from pathlib import Path

import pymupdf as fitz
import pandas as pd
from pypdf import PdfReader, PdfWriter


TEMPLATE_FILENAME = "demo_template.pdf"
OUTPUT_FILENAME = "merged_demo_report.pdf"
SUMMARY_FILENAME = "demo_error_summary.xlsx"
CHECKLIST = [f"Sample Check {i:02d}." for i in range(1, 16)]


def extract_error_counts_from_folder(folder_path: Path, source_files: list[Path]):
    """Count E statuses in source reports only; do not count template/output files."""
    error_counts = defaultdict(int)
    all_items = set()

    for pdf_path in source_files:
        with fitz.open(pdf_path) as doc:
            for page in doc:
                lines = [line.strip() for line in page.get_text().splitlines() if line.strip()]
                for i in range(len(lines) - 2):
                    title, status, count_str = lines[i], lines[i + 1], lines[i + 2]
                    if status in ("E", "P") and count_str.isdigit():
                        if title in CHECKLIST:
                            all_items.add(title)
                            if status == "E":
                                error_counts[title] += int(count_str)

    return error_counts, all_items


def save_error_summary_to_excel(folder_path: Path, error_counts, all_items):
    if not all_items:
        print("No sample checklist items found; summary workbook was not created.")
        return None

    rows = [
        {"Sample checklist item": item, "E (Error) total": error_counts.get(item, 0)}
        for item in CHECKLIST if item in all_items
    ]
    output_path = folder_path / SUMMARY_FILENAME
    pd.DataFrame(rows).to_excel(output_path, index=False)
    print(f"Excel summary saved: {output_path}")
    return output_path


def merge_pdfs_with_template(input_dir: Path, output_path: Path, source_files: list[Path]):
    template_path = input_dir / TEMPLATE_FILENAME
    if not template_path.is_file():
        raise FileNotFoundError(f"Required template not found: {template_path}")

    template_reader = PdfReader(str(template_path))
    if len(template_reader.pages) < len(CHECKLIST) + 1:
        raise ValueError(
            f"Template must contain a cover page plus {len(CHECKLIST)} section pages."
        )

    checklist_pages = {i: [] for i in range(len(CHECKLIST))}

    for pdf_path in source_files:
        print(f"Processing: {pdf_path.name}")
        reader = PdfReader(str(pdf_path))
        current_section = None

        for page_num, page in enumerate(reader.pages):
            # Demo input format intentionally has two introductory pages.
            if page_num < 2:
                continue

            text = page.extract_text() or ""
            new_section = next(
                (idx for idx, item in enumerate(CHECKLIST) if item in text),
                None,
            )
            if new_section is not None:
                current_section = new_section

            if current_section is not None:
                checklist_pages[current_section].append(page)

    writer = PdfWriter()
    writer.add_page(template_reader.pages[0])

    for idx in range(len(CHECKLIST)):
        writer.add_page(template_reader.pages[idx + 1])
        for page in checklist_pages[idx]:
            writer.add_page(page)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("wb") as output_file:
        writer.write(output_file)

    print(f"Merged PDF saved: {output_path}")
    return output_path


def select_input_folder():
    """Use a folder picker when available; otherwise request a path in the terminal."""
    try:
        import tkinter as tk
        from tkinter import filedialog, messagebox
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo(
            "폴더 선택 안내",
            "📑확인 버튼을 누른 후 병합할 파일이 있는 폴더를 선택해 주세요."
        )
        selected = filedialog.askdirectory(title="Select the demo PDF input folder")
        root.destroy()
        if selected:
            return Path(selected)
    except Exception:
        pass

    typed = input("Enter the demo input folder path: ").strip().strip('"')
    return Path(typed) if typed else None


def main():
    parser = argparse.ArgumentParser(description="Merge fictional demo report PDFs.")
    parser.add_argument("--input-dir", type=Path, help="Folder containing demo_template.pdf and sample report PDFs")
    parser.add_argument("--output-dir", type=Path, help="Output folder (defaults to <input-dir>/output)")
    args = parser.parse_args()

    input_dir = args.input_dir or select_input_folder()
    if not input_dir or not input_dir.is_dir():
        raise SystemExit("A valid input folder is required.")

    template_path = input_dir / TEMPLATE_FILENAME
    if not template_path.is_file():
        raise SystemExit(f"Template not found: {template_path}")

    source_files = sorted(
        p for p in input_dir.glob("*.pdf")
        if p.name != TEMPLATE_FILENAME and p.name != OUTPUT_FILENAME
    )
    if not source_files:
        raise SystemExit("No source report PDFs found in the input folder.")

    output_dir = args.output_dir or (input_dir.parent / "output")
    output_path = output_dir / OUTPUT_FILENAME

    merge_pdfs_with_template(input_dir, output_path, source_files)
    error_counts, all_items = extract_error_counts_from_folder(input_dir, source_files)
    save_error_summary_to_excel(output_dir, error_counts, all_items)


if __name__ == "__main__":
    main()
