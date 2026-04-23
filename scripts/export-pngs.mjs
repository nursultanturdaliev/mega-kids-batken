import sharp from "sharp";
import { join, dirname } from "path";
import { fileURLToPath } from "url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const assets = join(__dirname, "..", "assets");

/** @type {readonly [string, string, number][]} */
const jobs = [
  ["mega-kids-logo.svg", "mega-kids-logo.png", 2048],
  ["mega-kids-logo-mono-black.svg", "mega-kids-logo-mono-black.png", 2048],
  ["mega-kids-logo-mono-white.svg", "mega-kids-logo-mono-white.png", 2048],
  ["banner-outdoor.svg", "banner-outdoor.png", 4200],
  ["instagram-1080x1350.svg", "instagram-1080x1350.png", 1080],
  ["instagram-1080x1080.svg", "instagram-1080x1080.png", 1080],
  ["instagram-1080x1920-story.svg", "instagram-1080x1920-story.png", 1080],
  ["sticker-hours.svg", "sticker-hours.png", 2000],
  ["price-tag-generic.svg", "price-tag-generic.png", 960],
];

for (const [svgName, pngName, width] of jobs) {
  const input = join(assets, svgName);
  const output = join(assets, pngName);
  await sharp(input).resize({ width }).png({ compressionLevel: 9 }).toFile(output);
  console.log("OK", pngName);
}
