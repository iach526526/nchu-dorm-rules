import fitz
import os
import glob
import argparse

def convert_pdf(pdf_path, output_path):
    doc = fitz.open(pdf_path)
    lines = []
    for page_index, page in enumerate(doc):
        page_no = page_index + 1
        lines.append(f"\n--- Page {page_no} ---\n")
        blocks = page.get_text("blocks", sort=True)
        image_no = 0
        for block in blocks:
            x0, y0, x1, y1, content, block_no, block_type = block
            if block_type == 0:
                text = content.strip()
                if text:
                    lines.append(text + "\n\n")
            elif block_type == 1:
                image_no += 1
                lines.append(
                    f"[IMAGE: page {page_no}, image {image_no}, "
                    f"bbox=({x0:.0f}, {y0:.0f}, {x1:.0f}, {y1:.0f})]\n\n"
                )
    doc.close()
    with open(output_path, "w", encoding="utf-8") as f:
        f.writelines(lines)
    return len(lines)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert PDF to text with image placeholders")
    parser.add_argument("input", nargs="?", default="input.pdf", help="Input PDF file or directory")
    parser.add_argument("-o", "--output", default="output.txt", help="Output file or directory")
    args = parser.parse_args()

    if os.path.isdir(args.input):
        os.makedirs(args.output, exist_ok=True)
        for pdf_path in sorted(glob.glob(os.path.join(args.input, "*.pdf"))):
            base = os.path.splitext(os.path.basename(pdf_path))[0]
            out_path = os.path.join(args.output, f"{base}.txt")
            if os.path.exists(out_path):
                print(f"SKIP (exists): {base}")
                continue
            n = convert_pdf(pdf_path, out_path)
            print(f"OK: {base} ({n} lines)")
    else:
        convert_pdf(args.input, args.output)
        print(f"OK: {args.input} -> {args.output}")
