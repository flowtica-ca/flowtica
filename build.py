import pathlib
import re
import build_jobs

SRC_DIR = pathlib.Path("src")
OUT_FILE = pathlib.Path("index.html")
NAV_FILE = SRC_DIR / "_nav.html"
HEAD_FILE = SRC_DIR / "_head.html"
FOOTER_FILE = SRC_DIR / "_footer.html"

# Files will be concatenated between head and footer in this order
PARTS = [
    "home.html",
    "about.html",
    "services.html",
    "portfolio.html",
    "offers.html",
    "careers.html",
    "contact.html",
]

HEAD_DEFAULTS = {
    "PAGE_TITLE": "Flowtica | Back-Office Clerk Automation Sprint (Canada)",
    "PAGE_DESCRIPTION": (
        "Flowtica automates the clerical layer of back-office processes in 2 weeks—intake → validation → routing → updates → sync—leaving only true exceptions to humans. Deployed on a private, client-owned workflow stack that integrates with your existing tools."
    ),
    "PAGE_KEYWORDS": (
        "Flowtica, back office automation, clerk automation, accounts payable automation, accounts receivable automation, vendor compliance automation, workflow automation Canada, approvals automation, exception queue, audit logging, systems integration"
    ),
    "PAGE_CANONICAL": "https://flowtica.ca/",
    "OG_TITLE": "Flowtica | Back-Office Clerk Automation Sprint (Canada)",
    "OG_DESCRIPTION": (
        "Automate one clerical process in 2 weeks (intake → validation → approvals → updates → sync), with exception handling and audit logs. Deployed in your environment."
    ),
    "OG_URL": "https://flowtica.ca/",
    "EXTRA_HEAD": "",
}


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


def apply_includes(text: str) -> str:
    pattern = re.compile(r"\{\{INCLUDE:([^}]+)\}\}")
    while True:
        match = pattern.search(text)
        if not match:
            break
        include_path = SRC_DIR / match.group(1).strip()
        if not include_path.exists():
            raise FileNotFoundError(f"Missing include file: {include_path}")
        include_content = include_path.read_text(encoding="utf-8").strip()
        text = text[: match.start()] + include_content + text[match.end() :]
    return text


def render_head(nav: str, asset_prefix: str, meta: dict) -> str:
    if not HEAD_FILE.exists():
        raise FileNotFoundError("Missing head partial: src/_head.html")

    head_template = HEAD_FILE.read_text(encoding="utf-8").strip()
    replacements = {**HEAD_DEFAULTS, **meta, "ASSET_PREFIX": asset_prefix, "NAV": nav}
    for key, value in replacements.items():
        head_template = head_template.replace(f"{{{{{key}}}}}", value)
    return head_template


def render_footer(asset_prefix: str) -> str:
    if not FOOTER_FILE.exists():
        raise FileNotFoundError("Missing footer partial: src/_footer.html")

    footer_template = FOOTER_FILE.read_text(encoding="utf-8").strip()
    return footer_template.replace("{{ASSET_PREFIX}}", asset_prefix)


def load_part(name: str) -> str:
    path = SRC_DIR / name
    if not path.exists():
        raise FileNotFoundError(f"Missing section file: {path}")

    text = path.read_text(encoding="utf-8").strip()
    return apply_includes(text)


def main():
    nav = render_nav(prefix="", portfolio_active=False)
    head = render_head(nav=nav, asset_prefix="", meta={})
    body_chunks = [load_part(name) for name in PARTS]
    footer = render_footer(asset_prefix="")

    OUT_FILE.write_text("\n".join([head, *body_chunks, footer]) + "\n", encoding="utf-8")
    print("✅ Rebuilt index.html from src/*.html")
    import build_cases

    build_cases.main()
    build_jobs.main()


if __name__ == "__main__":
    main()
