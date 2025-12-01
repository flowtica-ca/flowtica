/* 
Project Name: Modern Portfolio Website
Description: Flowtica single-page version with smooth scrolling
Author: Md Al Amin Hossen (template) + Flowtica customization
*/

// ---------------- Typing animation ----------------
if (document.querySelector(".typing")) {
  // Typed.js is loaded via script tag in index.html
  // eslint-disable-next-line no-undef
  new Typed(".typing", {
    strings: [
      "",
      "AI systems",
      "AI assistants",
      "workflow automation",
      "document Q&A",
    ],
    typeSpeed: 100,
    BackSpeed: 60,
    loop: true,
  });
}

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

    const y = targetEl.offsetTop;

    window.scrollTo({
      top: y,
      behavior: "smooth",
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

    window.scrollTo({
      top: targetEl.offsetTop,
      behavior: "smooth",
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
