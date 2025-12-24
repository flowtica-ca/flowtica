import pathlib
import json

JOBS = [
    {
        "slug": "automation-implementation-specialist",
        "title": "Automation Implementation Specialist (Junior–Mid) | Flowtica",
        "description": "On-site in Kingston, ON. Deliver customer automation end-to-end (discovery → plan → build → iterate).",
        "content": "automation-implementation-specialist.body.html",
        "date_posted": "2025-12-24",
        "valid_through": "2026-01-31T23:59:59-05:00",
        "apply_email": "hello@flowtica.ca",
        "canonical": "https://flowtica.ca/jobs/automation-implementation-specialist.html",
    },
]

SRC_DIR = pathlib.Path("src/jobs")
TEMPLATE_FILE = SRC_DIR / "_job_template.html"
NAV_FILE = pathlib.Path("src/_nav.html")
HEAD_FILE = pathlib.Path("src/_head.html")
FOOTER_FILE = pathlib.Path("src/_footer.html")
OUT_DIR = pathlib.Path("jobs")

HEAD_DEFAULTS = {
    "PAGE_TITLE": "Flowtica | Workflow Automation for Operations Teams (Canada)",
    "PAGE_DESCRIPTION": (
        "Flowtica helps operational teams automate routine work with dependable AI assistants and workflow integrations. "
        "We deliver outcomes quickly, integrating with the tools you already use."
    ),
    "PAGE_KEYWORDS": (
        "Flowtica, AI workflow automation, AI assistants, AI consultant, AI consultant Canada, phone agents, document Q&A, RAG, operations"
    ),
    "PAGE_CANONICAL": "https://flowtica.ca/",
    "OG_TITLE": "Flowtica | Workflow Automation for Operations Teams (Canada)",
    "OG_DESCRIPTION": (
        "Flowtica designs and operates AI assistants and workflow automation that integrate with your existing tools so teams save time, reduce errors, and move faster."
    ),
    "OG_URL": "https://flowtica.ca/",
    "EXTRA_HEAD": "",
}


def render_nav(prefix: str) -> str:
    nav_template = NAV_FILE.read_text(encoding="utf-8").strip()
    return (
        nav_template.replace("{{PREFIX}}", prefix)
        .replace("{{HOME_ACTIVE}}", "")
        .replace("{{PORTFOLIO_ACTIVE}}", "")
    )


def render_head(nav: str, asset_prefix: str, meta: dict) -> str:
    head_template = HEAD_FILE.read_text(encoding="utf-8").strip()
    replacements = {**HEAD_DEFAULTS, **meta, "ASSET_PREFIX": asset_prefix, "NAV": nav}
    for key, value in replacements.items():
        head_template = head_template.replace(f"{{{{{key}}}}}", value)
    return head_template


def render_footer(asset_prefix: str) -> str:
    footer_template = FOOTER_FILE.read_text(encoding="utf-8").strip()
    return footer_template.replace("{{ASSET_PREFIX}}", asset_prefix)


def json_escape_for_ld(html: str) -> str:
    """
    Return a JSON string literal containing HTML.
    We keep the job description aligned with visible page content.
    """
    return json.dumps(html.replace("\r\n", "\n"))


def build_job(config: dict, template: str) -> None:
    content_path = SRC_DIR / config["content"]
    content = content_path.read_text(encoding="utf-8").strip()

    nav = render_nav(prefix="../index.html")
    job_jsonld = f"""{{
  "@context": "https://schema.org",
  "@type": "JobPosting",
  "title": "Automation Implementation Specialist (Junior–Mid)",
  "description": {json_escape_for_ld(content)},
  "datePosted": "{config['date_posted']}",
  "validThrough": "{config['valid_through']}",
  "employmentType": "FULL_TIME",
  "hiringOrganization": {{
    "@type": "Organization",
    "name": "Flowtica",
    "sameAs": "https://flowtica.ca/",
    "logo": "https://flowtica.ca/images/logo.png"
  }},
  "jobLocation": {{
    "@type": "Place",
    "address": {{
      "@type": "PostalAddress",
      "addressLocality": "Kingston",
      "addressRegion": "ON",
      "addressCountry": "CA"
    }}
  }},
  "directApply": true,
  "url": "{config['canonical']}",
  "identifier": {{
    "@type": "PropertyValue",
    "name": "Flowtica",
    "value": "{config['slug']}"
  }}
}}"""

    job_jsonld_script = f"""    <!-- JobPosting structured data (no salary) -->
    <script type="application/ld+json">
{job_jsonld}
    </script>"""

    head = render_head(
        nav=nav,
        asset_prefix="../",
        meta={
            "PAGE_TITLE": config["title"],
            "PAGE_DESCRIPTION": config["description"],
            "PAGE_KEYWORDS": (
                "Flowtica, Automation Implementation Specialist, automation jobs, Kingston, ON, workflow automation"
            ),
            "PAGE_CANONICAL": config["canonical"],
            "OG_TITLE": config["title"],
            "OG_DESCRIPTION": config["description"],
            "OG_URL": config["canonical"],
            "EXTRA_HEAD": job_jsonld_script,
        },
    )

    job_section = (
        template.replace("{{JOB_BODY}}", content).replace("{{APPLY_EMAIL}}", config["apply_email"])
    )

    footer = render_footer(asset_prefix="../")

    html = "\n".join([head, job_section, footer])

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUT_DIR / f"{config['slug']}.html"
    out_path.write_text(html + "\n", encoding="utf-8")
    print(f"✅ Built {out_path}")


def main() -> None:
    if not TEMPLATE_FILE.exists():
        raise FileNotFoundError("Missing job template: src/jobs/_job_template.html")
    if not NAV_FILE.exists():
        raise FileNotFoundError("Missing nav partial: src/_nav.html")
    if not HEAD_FILE.exists():
        raise FileNotFoundError("Missing head partial: src/_head.html")
    if not FOOTER_FILE.exists():
        raise FileNotFoundError("Missing footer partial: src/_footer.html")

    template = TEMPLATE_FILE.read_text(encoding="utf-8").strip()
    for job in JOBS:
        build_job(job, template)


if __name__ == "__main__":
    main()
