/* 
Project Name: Modern Portfolio Website
Description: Flowtica single-page version with smooth scrolling
Author: Md Al Amin Hossen (template) + Flowtica customization
*/

// ---------------- Typing animation ----------------
(() => {
  const typingEl = document.querySelector(".typing");
  if (!typingEl) return;

  // Ensure Typed.js is available (loaded via script tag in index.html)
  if (typeof Typed === "undefined") return;

  // If the element already has text, Typed.js will overwrite it.
  // Prefer keeping the HTML as: <span class="typing"></span>
  // eslint-disable-next-line no-undef
new Typed(".typing", {
  strings: [
"reliable workflow automation",
"operational automation that lasts",
"document intelligence with citations",
"intake systems your team can trust",
"integrations that fit your stack",

  ],
  typeSpeed: 70,
  backSpeed: 35,
  backDelay: 1400,
  loop: true,
  showCursor: false,
});
})();

// ---------------- Smooth scroll & scroll spy ----------------
const nav = document.querySelector(".nav");
const navLinks = nav ? nav.querySelectorAll("a[href^='#']") : [];
const sections = document.querySelectorAll(".section");

// Smooth scroll on nav click
navLinks.forEach((link) => {
  link.addEventListener("click", (e) => {
    e.preventDefault();

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

    // Close aside on small screens
    if (window.innerWidth < 1200) {
      toggleAside();
    }
  });
});

// Optional: if there's a ".hire-me" button, make it scroll to its target
const hireMeBtn = document.querySelector(".hire-me");
if (hireMeBtn) {
  hireMeBtn.addEventListener("click", (e) => {
    e.preventDefault();
    const href = hireMeBtn.getAttribute("href") || "#contact";
    const targetId = href.split("#")[1];
    const targetEl = document.getElementById(targetId);
    if (!targetEl) return;

    targetEl.scrollIntoView({
      behavior: "smooth",
      block: "start",
    });

    setActiveNav(targetId);
  });
}

// Highlight nav item based on scroll position (scroll spy)
function setActiveNav(targetId) {
  navLinks.forEach((link) => {
    const href = link.getAttribute("href");
    if (!href || !href.includes("#")) return;
    const id = href.split("#")[1];

    if (id === targetId) {
      link.classList.add("active");
    } else {
      link.classList.remove("active");
    }
  });
}

window.addEventListener("scroll", () => {
  const scrollPos = window.scrollY + window.innerHeight / 3; // middle-ish of viewport
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

// ---------------- Aside nav toggler ----------------
const navTogglerBtn = document.querySelector(".nav-toggler");
const aside = document.querySelector(".aside");

function toggleAside() {
  if (aside) {
    aside.classList.toggle("open");
  }
  if (navTogglerBtn) {
    navTogglerBtn.classList.toggle("open");
  }
}

if (navTogglerBtn) {
  navTogglerBtn.addEventListener("click", toggleAside);
}
