import pathlib

JOBS = [
    {
        "slug": "automation-implementation-specialist",
        "title": "Automation Implementation Specialist (Junior–Mid) | Flowtica",
        "description": "On-site in Kingston, ON. Deliver customer automation end-to-end (discovery → plan → build → iterate).",
        "content": "automation-implementation-specialist.html",
        "date_posted": "2025-12-24",
        "valid_through": "2026-01-31T23:59:59-05:00",
        "apply_email": "hello@flowtica.ca",
        "canonical": "https://flowtica.ca/jobs/automation-implementation-specialist.html",
    },
]

SRC_DIR = pathlib.Path("src/jobs")
TEMPLATE_FILE = SRC_DIR / "_job_template.html"
NAV_FILE = pathlib.Path("src/_nav.html")
OUT_DIR = pathlib.Path("jobs")


def render_nav(prefix: str) -> str:
    nav_template = NAV_FILE.read_text(encoding="utf-8").strip()
    # No active highlighting needed on job pages
    return (
        nav_template.replace("{{PREFIX}}", prefix)
        .replace("{{HOME_ACTIVE}}", "")
        .replace("{{PORTFOLIO_ACTIVE}}", "")
    )


def build_job(config: dict, template: str) -> None:
    content_path = SRC_DIR / config["content"]
    content = content_path.read_text(encoding="utf-8").strip()

    nav = render_nav(prefix="../index.html")

    # IMPORTANT: no salary in schema or page content.
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

    html = (
        template.replace("{{TITLE}}", config["title"])
        .replace("{{DESCRIPTION}}", config["description"])
        .replace("{{CANONICAL}}", config["canonical"])
        .replace("{{NAV}}", nav)
        .replace("{{JOB_JSONLD}}", job_jsonld)
        .replace("{{CONTENT}}", content)
        .replace("{{APPLY_EMAIL}}", config["apply_email"])
    )

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUT_DIR / f"{config['slug']}.html"
    out_path.write_text(html + "\n", encoding="utf-8")
    print(f"✅ Built {out_path}")


def json_escape_for_ld(html: str) -> str:
    """
    Return a JSON string literal containing HTML.
    We keep the job description aligned with visible page content.
    """
    import json
    # Normalize newlines; keep as a JSON string
    return json.dumps(html.replace("\r\n", "\n"))


def main() -> None:
    if not TEMPLATE_FILE.exists():
        raise FileNotFoundError("Missing job template: src/jobs/_job_template.html")
    if not NAV_FILE.exists():
        raise FileNotFoundError("Missing nav partial: src/_nav.html")

    template = TEMPLATE_FILE.read_text(encoding="utf-8")
    for job in JOBS:
        build_job(job, template)


if __name__ == "__main__":
    main()

