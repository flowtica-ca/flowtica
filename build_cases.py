import pathlib

SITE_URL = "https://flowtica.ca"

PAGES = [
    {
        "slug": "property-management-maintenance-intake-automation",
        "title": "Flowtica | Property Management Maintenance Intake Automation",
        "description": (
            "Buyer-focused overview of maintenance intake automation for property management teams, covering request intake, "
            "triage, dispatch, tenant updates, and escalation handling."
        ),
        "content": "property-management-maintenance-intake-automation.html",
        "page_type": "landing",
        "cta_label": "Discuss maintenance intake automation",
        "eyebrow_label": "Solution · Property Management",
    },
    {
        "slug": "accounts-payable-back-office-automation",
        "title": "Flowtica | Accounts Payable and Back-Office Automation",
        "description": (
            "Buyer-focused overview of accounts payable automation for finance teams, covering invoice intake, approval routing, "
            "exception handling, auditability, and fewer manual touches."
        ),
        "content": "accounts-payable-back-office-automation.html",
        "page_type": "landing",
        "cta_label": "Discuss AP automation",
        "eyebrow_label": "Solution · Finance Operations",
    },
    {
        "slug": "casl-first-outreach-automation",
        "title": "Flowtica | CASL-First Outreach Automation",
        "description": (
            "Structured outreach workflow design centered on prospect research, public-source evidence capture, draft generation, "
            "and human review before outbound use."
        ),
        "content": "casl-first-outreach-automation.html",
        "page_type": "landing",
        "cta_label": "Discuss an outreach workflow",
        "eyebrow_label": "Solution · Outreach Operations",
    },
    {
        "slug": "case-finance-ops-ap-automation",
        "title": "Flowtica | Accounts Payable Automation for Finance Teams",
        "description": (
            "A practical example of automating invoice intake, validation, approval routing, and posting/export "
            "so finance teams reduce manual AP effort, prevent duplicates, and improve auditability."
        ),
        "content": "finance-ops-ap-automation.html",
        "page_type": "example",
    },
    {
        "slug": "case-property-management-maintenance-automation",
        "title": "Flowtica | Maintenance Request Automation for Property Managers",
        "description": (
            "A practical example of automating maintenance request intake, triage, vendor dispatch, and tenant updates "
            "so property management teams move faster with fewer escalations."
        ),
        "content": "property-management-maintenance-automation.html",
        "page_type": "example",
    },
    {
        "slug": "case-staffing-last-minute-shift-fill",
        "title": "Flowtica | Last Minute Shift Fill Automation for Staffing Agencies",
        "description": (
            "A practical example of automating last-minute shift broadcast, confirmations, allocation, and client updates "
            "so staffing agencies fill roles faster with less coordinator effort."
        ),
        "content": "staffing-last-minute-shift-fill.html",
        "page_type": "example",
    },
    {
        "slug": "case-ai-consultant-canada",
        "title": "Flowtica | AI Consulting in Canada",
        "description": (
            "How Flowtica works as an AI consultant in Canada for operations-heavy teams, "
            "focusing on AI assistants and workflow automation that behave like part of your infrastructure."
        ),
        "content": "ai-consultant-canada.html",
        "page_type": "example",
    },
    {
        "slug": "case-hr-copilot",
        "title": "Flowtica | Policy & HR Knowledge Copilot",
        "description": (
            "How Flowtica designs a policy and HR knowledge copilot, giving employees grounded answers from your own documentation "
            "while keeping data inside your environment."
        ),
        "content": "hr-copilot.html",
        "page_type": "example",
    },
    {
        "slug": "case-property-management",
        "title": "Flowtica | Property Management Automation",
        "description": (
            "How Flowtica designs and operates AI assistants for property management teams, handling resident questions, work orders, "
            "and workflows across systems."
        ),
        "content": "property-management.html",
        "page_type": "example",
    },
    {
        "slug": "case-service-business",
        "title": "Flowtica | Service Business Co-Pilot",
        "description": (
            "How Flowtica builds AI co-pilots for service businesses to triage inquiries, surface knowledge, and keep operations moving."
        ),
        "content": "service-business.html",
        "page_type": "example",
    },
]

SRC_DIR = pathlib.Path("src/cases")
TEMPLATE_FILE = SRC_DIR / "_case_template.html"
NAV_FILE = pathlib.Path("src/_nav.html")
HEAD_FILE = pathlib.Path("src/_head.html")
FOOTER_FILE = pathlib.Path("src/_footer.html")

HEAD_DEFAULTS = {
    "PAGE_TITLE": "Flowtica | Workflow Automation for Operations Teams (Canada)",
    "PAGE_DESCRIPTION": (
        "Flowtica helps operational teams automate routine work with dependable AI assistants and workflow integrations. "
        "We deliver outcomes quickly, integrating with the tools you already use."
    ),
    "PAGE_KEYWORDS": (
        "Flowtica, workflow automation, operations automation, AI assistants, process automation"
    ),
    "PAGE_CANONICAL": "https://flowtica.ca/",
    "OG_TITLE": "Flowtica | Workflow Automation for Operations Teams (Canada)",
    "OG_DESCRIPTION": (
        "Flowtica designs and operates AI assistants and workflow automation that integrate with your existing tools so teams save time, reduce errors, and move faster."
    ),
    "OG_URL": "https://flowtica.ca/",
    "EXTRA_HEAD": "",
}

GENERATED_PAGE_EXTRA_HEAD = """
    <style>
      .case-section p {
        font-size: 0.95rem;
      }

      .case-section ul,
      .case-section ol {
        font-size: 0.95rem;
      }

      .case-section .section-title h1 {
        font-size: 40px;
        color: var(--text-black-900);
        font-weight: 700;
        position: relative;
        margin: 0;
      }

      .case-section .section-title h1::before {
        content: "";
        height: 4px;
        width: 50px;
        background: var(--skin-color);
        position: absolute;
        left: 0;
        top: 100%;
      }

      .case-section .section-title h1::after {
        content: "";
        height: 4px;
        width: 25px;
        background: var(--skin-color);
        position: absolute;
        left: 0;
        top: 100%;
        margin-top: 8px;
      }

      .case-diagram {
        margin-top: 1.5rem;
        padding: 1.4rem;
        border-radius: 16px;
        background: rgba(0, 0, 0, 0.35);
        border: 1px solid rgba(255, 255, 255, 0.08);
        display: flex;
        flex-wrap: wrap;
        gap: 0.8rem;
        align-items: stretch;
        justify-content: center;
      }

      .case-diagram-node {
        flex: 1 1 210px;
        min-width: 0;
        border-radius: 12px;
        padding: 0.9rem 1rem;
        background: rgba(0, 0, 0, 0.5);
        border: 1px solid rgba(255, 255, 255, 0.1);
        color: #f7f7f7;
        font-size: 0.85rem;
      }

      .case-diagram-node h4 {
        margin-top: 0;
        margin-bottom: 0.45rem;
        font-size: 0.95rem;
      }

      .case-diagram-node ul {
        padding-left: 1.1rem;
        margin: 0;
      }

      .case-diagram-node li {
        margin-bottom: 0.25rem;
      }

      .case-diagram-arrow {
        align-self: center;
        font-size: 1.3rem;
        opacity: 0.85;
        padding: 0 0.3rem;
      }

      @media (max-width: 767px) {
        .case-diagram {
          flex-direction: column;
        }

        .case-diagram-arrow {
          text-align: center;
        }

        .case-section .section-title h1 {
          font-size: 1.5rem;
        }
      }
    </style>
""".strip()


def render_nav(prefix: str, solutions_active: bool) -> str:
    if not NAV_FILE.exists():
        raise FileNotFoundError("Missing nav partial: src/_nav.html")

    nav_template = NAV_FILE.read_text(encoding="utf-8").strip()
    return (
        nav_template.replace("{{PREFIX}}", prefix)
        .replace("{{HOME_ACTIVE}}", "" if solutions_active else " class=\"active\"")
        .replace(
            "{{SOLUTIONS_ACTIVE}}",
            " class=\"active\"" if solutions_active else "",
        )
    )


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


def replace_tokens(text: str, replacements: dict) -> str:
    for key, value in replacements.items():
        text = text.replace(f"{{{{{key}}}}}", value)
    return text


def default_cta_copy(page_type: str) -> tuple[str, str, str]:
    if page_type == "landing":
        return (
            "See how this fits your workflow",
            "Start with a free workflow assessment. If this lane matches a live bottleneck, "
            "we scope the first automation, connect it to your tools, and harden it for day-to-day use.",
            "Request a free workflow assessment",
        )

    return (
        "Want a workflow like this in your environment?",
        "Start with a free workflow assessment. If it’s a fit, we’ll build a focused MVP connected to your "
        "tools so you can validate impact quickly.",
        "Request a free workflow assessment",
    )


def build_page(config: dict, template: str) -> None:
    content_path = SRC_DIR / config["content"]
    if not content_path.exists():
        raise FileNotFoundError(f"Missing generated page content: {content_path}")

    canonical = f"{SITE_URL}/{config['slug']}.html"
    cta_heading, cta_description, default_cta_label = default_cta_copy(
        config["page_type"]
    )
    replacements = {
        "PAGE_TYPE": config["page_type"],
        "EYEBROW_LABEL": config.get("eyebrow_label", ""),
        "CTA_LABEL": config.get("cta_label", default_cta_label),
        "CTA_HREF": "index.html#contact",
        "SITE_URL": SITE_URL,
        "CANONICAL_URL": canonical,
    }

    content = replace_tokens(content_path.read_text(encoding="utf-8").strip(), replacements)
    body = replace_tokens(
        template,
        {
            **replacements,
            "CONTENT": content,
            "CTA_HEADING": cta_heading,
            "CTA_DESCRIPTION": cta_description,
        },
    )

    nav = render_nav(prefix="index.html", solutions_active=True)
    keywords = (
        config.get("keywords")
        or f"Flowtica, workflow automation, {config['slug'].replace('-', ' ')}"
    )
    head = render_head(
        nav=nav,
        asset_prefix="",
        meta={
            "PAGE_TITLE": config["title"],
            "PAGE_DESCRIPTION": config["description"],
            "PAGE_KEYWORDS": keywords,
            "PAGE_CANONICAL": canonical,
            "OG_TITLE": config.get("og_title", config["title"]),
            "OG_DESCRIPTION": config.get("og_description", config["description"]),
            "OG_URL": canonical,
            "EXTRA_HEAD": GENERATED_PAGE_EXTRA_HEAD,
        },
    )
    footer = render_footer(asset_prefix="")

    out_path = pathlib.Path(f"{config['slug']}.html")
    out_path.write_text("\n".join([head, body, footer]) + "\n", encoding="utf-8")
    print(f"Built {out_path}")


def main() -> None:
    if not TEMPLATE_FILE.exists():
        raise FileNotFoundError("Missing generated page template: src/cases/_case_template.html")
    if not NAV_FILE.exists():
        raise FileNotFoundError("Missing nav partial: src/_nav.html")
    if not HEAD_FILE.exists():
        raise FileNotFoundError("Missing head partial: src/_head.html")
    if not FOOTER_FILE.exists():
        raise FileNotFoundError("Missing footer partial: src/_footer.html")

    template = TEMPLATE_FILE.read_text(encoding="utf-8").strip()
    for page in PAGES:
        build_page(page, template)


if __name__ == "__main__":
    main()
