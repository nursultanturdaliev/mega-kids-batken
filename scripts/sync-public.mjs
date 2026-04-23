import { cpSync, mkdirSync, rmSync, copyFileSync } from "fs";
import { join, dirname } from "path";
import { fileURLToPath } from "url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const root = join(__dirname, "..");
const pub = join(root, "public");

rmSync(pub, { recursive: true, force: true });
mkdirSync(pub, { recursive: true });
for (const f of ["index.html", "highlights.html", "styles.css", "favicon.svg"]) {
  copyFileSync(join(root, f), join(pub, f));
}
cpSync(join(root, "assets"), join(pub, "assets"), { recursive: true });
console.log("synced -> public/");
