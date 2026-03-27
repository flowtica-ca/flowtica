/*
Project Name: Flowtica website
Description: Shared interactions for navigation, hero typing, and reveal motion
*/

(() => {
  const typingEl = document.querySelector(".typing");

  if (!typingEl || typeof Typed === "undefined") {
    return;
  }

  // eslint-disable-next-line no-undef
  new Typed(".typing", {
    strings: [
      "reliable workflow automation",
      "operational AI that lasts",
      "document intelligence with citations",
      "intake systems your team can trust",
      "integrations that fit your stack",
    ],
    typeSpeed: 68,
    backSpeed: 34,
    backDelay: 1350,
    loop: true,
    showCursor: false,
  });
})();

const nav = document.querySelector(".nav");
const navLinks = nav ? nav.querySelectorAll("a[href^='#']") : [];
const sections = document.querySelectorAll(".section[id]");
const navTogglerBtn = document.querySelector(".nav-toggler");
const aside = document.querySelector(".aside");

function toggleAside(forceOpen) {
  if (!aside || !navTogglerBtn) return;

  const shouldOpen =
    typeof forceOpen === "boolean" ? forceOpen : !aside.classList.contains("open");

  aside.classList.toggle("open", shouldOpen);
  navTogglerBtn.classList.toggle("open", shouldOpen);
}

function setActiveNav(targetId) {
  navLinks.forEach((link) => {
    const href = link.getAttribute("href");
    if (!href || !href.includes("#")) return;

    const id = href.split("#")[1];
    link.classList.toggle("active", id === targetId);
  });
}

navLinks.forEach((link) => {
  link.addEventListener("click", (event) => {
    event.preventDefault();

    const href = link.getAttribute("href");
    if (!href || !href.includes("#")) return;

    const targetId = href.split("#")[1];
    const targetEl = document.getElementById(targetId);
    if (!targetEl) return;

    targetEl.scrollIntoView({
      behavior: "smooth",
      block: "start",
    });

    setActiveNav(targetId);

    if (window.innerWidth < 1200) {
      toggleAside(false);
    }
  });
});

window.addEventListener("scroll", () => {
  const scrollPos = window.scrollY + window.innerHeight / 3;
  let currentId = null;

  sections.forEach((section) => {
    const top = section.offsetTop;
    const height = section.offsetHeight;

    if (scrollPos >= top && scrollPos < top + height) {
      currentId = section.id;
    }
  });

  if (currentId) {
    setActiveNav(currentId);
  }
});

if (navTogglerBtn) {
  navTogglerBtn.addEventListener("click", () => toggleAside());
}

document.addEventListener("click", (event) => {
  if (!aside || !navTogglerBtn || window.innerWidth >= 1200) return;
  if (!aside.classList.contains("open")) return;

  const clickedInsideAside = aside.contains(event.target);
  const clickedToggler = navTogglerBtn.contains(event.target);

  if (!clickedInsideAside && !clickedToggler) {
    toggleAside(false);
  }
});

document.addEventListener("keydown", (event) => {
  if (event.key === "Escape" && aside && aside.classList.contains("open")) {
    toggleAside(false);
  }
});

window.addEventListener("resize", () => {
  if (window.innerWidth >= 1200) {
    toggleAside(false);
  }
});

(() => {
  const revealTargets = document.querySelectorAll(
    [
      ".section-title",
      ".about-text",
      ".surface-panel",
      ".service-item-inner",
      ".case-card",
      ".offer-card",
      ".career-card-inner",
      ".contact-info-item",
      ".contact-form form",
      ".job-card",
      ".case-diagram-node",
    ].join(",")
  );

  if (!revealTargets.length) return;

  revealTargets.forEach((item, index) => {
    item.classList.add("reveal-on-scroll");
    item.style.setProperty("--reveal-delay", `${Math.min(index * 45, 240)}ms`);
  });

  if (!("IntersectionObserver" in window)) {
    revealTargets.forEach((item) => item.classList.add("is-visible"));
    return;
  }

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;

        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      });
    },
    {
      threshold: 0.18,
      rootMargin: "0px 0px -8% 0px",
    }
  );

  revealTargets.forEach((item) => observer.observe(item));
})();
