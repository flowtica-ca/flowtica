import pathlib
import build_jobs

# Files will be concatenated in this order
PARTS = [
    "_head.html",
    "home.html",
    "about.html",
    "services.html",
    "portfolio.html",
    "offers.html",
    "careers.html",
    "contact.html",
    "_footer.html",
]

SRC_DIR = pathlib.Path("src")
OUT_FILE = pathlib.Path("index.html")
NAV_FILE = SRC_DIR / "_nav.html"


def render_nav(prefix: str, portfolio_active: bool) -> str:
    if not NAV_FILE.exists():
        raise FileNotFoundError("Missing nav partial: src/_nav.html")

    nav_template = NAV_FILE.read_text(encoding="utf-8").strip()
    return (
        nav_template.replace("{{PREFIX}}", prefix)
        .replace("{{HOME_ACTIVE}}", " class=\"active\"" if not portfolio_active else "")
        .replace(
            "{{PORTFOLIO_ACTIVE}}", " class=\"active\"" if portfolio_active else ""
        )
    )


def load_part(name: str) -> str:
    path = SRC_DIR / name
    if not path.exists():
        raise FileNotFoundError(f"Missing section file: {path}")

    text = path.read_text(encoding="utf-8").strip()
    if name == "_head.html":
        nav = render_nav(prefix="", portfolio_active=False)
        return text.replace("{{NAV}}", nav)
    return text


def main():
    chunks = [load_part(name) for name in PARTS]

    # Join sections with a newline between them and write index.html
    OUT_FILE.write_text("\n".join(chunks) + "\n", encoding="utf-8")
    print("✅ Rebuilt index.html from src/*.html")
    import build_cases
    build_cases.main()
    build_jobs.main()


if __name__ == "__main__":
    main()
