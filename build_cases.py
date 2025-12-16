import pathlib

CASES = [
    {
        "slug": "case-ai-consultant-canada",
        "title": "Flowtica | AI Consulting in Canada",
        "description": (
            "How Flowtica works as an AI consultant in Canada for operations-heavy teams, "
            "focusing on AI assistants and workflow automation that behave like part of your infrastructure."
        ),
        "content": "ai-consultant-canada.html",
    },
    {
        "slug": "case-hr-copilot",
        "title": "Flowtica | Policy & HR Knowledge Copilot",
        "description": (
            "How Flowtica designs a policy and HR knowledge copilot, giving employees grounded answers from your own documentation "
            "while keeping data inside your environment."
        ),
        "content": "hr-copilot.html",
    },
    {
        "slug": "case-property-management",
        "title": "Flowtica | Property Management Automation",
        "description": (
            "How Flowtica designs and operates AI assistants for property management teams, handling resident questions, work orders, "
            "and workflows across systems."
        ),
        "content": "property-management.html",
    },
    {
        "slug": "case-service-business",
        "title": "Flowtica | Service Business Co-Pilot",
        "description": (
            "How Flowtica builds AI co-pilots for service businesses to triage inquiries, surface knowledge, and keep operations moving."
        ),
        "content": "service-business.html",
    },
]

SRC_DIR = pathlib.Path("src/cases")
TEMPLATE_FILE = SRC_DIR / "_case_template.html"


def build_case(config: dict, template: str) -> None:
    content_path = SRC_DIR / config["content"]
    if not content_path.exists():
        raise FileNotFoundError(f"Missing case content: {content_path}")

    content = content_path.read_text(encoding="utf-8").strip()
    html = (
        template.replace("{{TITLE}}", config["title"])
        .replace("{{DESCRIPTION}}", config["description"])
        .replace("{{CONTENT}}", content)
    )

    out_path = pathlib.Path(f"{config['slug']}.html")
    out_path.write_text(html + "\n", encoding="utf-8")
    print(f"✅ Built {out_path}")


def main() -> None:
    if not TEMPLATE_FILE.exists():
        raise FileNotFoundError("Missing case template. Run from repo root.")

    template = TEMPLATE_FILE.read_text(encoding="utf-8")
    for case in CASES:
        build_case(case, template)


if __name__ == "__main__":
    main()
