const fs = require("fs");
const path = require("path");

const parts = [
  "_head.html",
  "home.html",
  "about.html",
  "services.html",
  "portfolio.html",
  "offers.html",
  "contact.html",
  "_footer.html",
];

const srcDir = path.join(__dirname, "src");
const outFile = path.join(__dirname, "index.html");
const navFile = path.join(srcDir, "_nav.html");

function renderNav(prefix, solutionsActive) {
  const navTemplate = fs.readFileSync(navFile, "utf8").trim();

  return navTemplate
    .replaceAll("{{PREFIX}}", prefix)
    .replace("{{HOME_ACTIVE}}", solutionsActive ? "" : " class=\"active\"")
    .replace("{{SOLUTIONS_ACTIVE}}", solutionsActive ? " class=\"active\"" : "");
}

function loadPart(file) {
  const filePath = path.join(srcDir, file);
  const contents = fs.readFileSync(filePath, "utf8").trim();

  if (file === "_head.html") {
    return contents.replace("{{NAV}}", renderNav("", false));
  }

  return contents;
}

const output = parts.map(loadPart).join("\n");
fs.writeFileSync(outFile, `${output}\n`, "utf8");
console.log("index.html rebuilt from src/*.html");
