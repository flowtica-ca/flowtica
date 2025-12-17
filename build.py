import pathlib

# Files will be concatenated in this order
PARTS = [
    "_head.html",
    "home.html",
    "about.html",
    "services.html",
    "portfolio.html",
    "offers.html",
    "career.html",
    "contact.html",
    "_footer.html",
]

SRC_DIR = pathlib.Path("src")
OUT_FILE = pathlib.Path("index.html")


def main():
    chunks = []
    for name in PARTS:
        path = SRC_DIR / name
        if not path.exists():
            raise FileNotFoundError(f"Missing section file: {path}")
        text = path.read_text(encoding="utf-8").strip()
        chunks.append(text)

    # Join sections with a newline between them and write index.html
    OUT_FILE.write_text("\n".join(chunks) + "\n", encoding="utf-8")
    print("✅ Rebuilt index.html from src/*.html")


if __name__ == "__main__":
    main()
