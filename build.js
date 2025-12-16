const fs = require("fs");
const path = require("path");

const parts = [
  "_head.html",
  "home.html",
  "about.html",
  "services.html",
  "portfolio.html",
  "offers.html",
  "career.html",
  "contact.html",
  "_footer.html",
];

const srcDir = path.join(__dirname, "src");
const outFile = path.join(__dirname, "index.html");

let output = "";
for (const file of parts) {
  const filePath = path.join(srcDir, file);
  const contents = fs.readFileSync(filePath, "utf8");
  output += contents.trim() + "\n";
}

fs.writeFileSync(outFile, output.trim() + "\n", "utf8");
console.log("index.html rebuilt from src/*.html");
