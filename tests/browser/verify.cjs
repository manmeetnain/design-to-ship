const { chromium } = require("playwright");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");

const baseURL = process.env.DTS_BASE_URL || "http://127.0.0.1:4173";
const artifacts = path.resolve(process.env.DTS_ARTIFACTS || "artifacts/browser");
fs.mkdirSync(artifacts, { recursive: true });

(async () => {
  const browser = await chromium.launch({ headless: true });
  try {
    const desktop = await browser.newPage({ viewport: { width: 1440, height: 1000 } });
    await desktop.goto(baseURL, { waitUntil: "networkidle" });
    assert.equal(await desktop.locator("h1").textContent(), "What needs attention now");
    assert.match(await desktop.locator("#incident-queue li").first().textContent(), /Critical/);
    await desktop.getByRole("button", { name: "Acknowledge" }).first().click();
    assert.equal(await desktop.locator("#detail-status").textContent(), "Acknowledged");
    assert.match(await desktop.locator("#status-message").textContent(), /INC-248 acknowledged/);
    await desktop.screenshot({ path: path.join(artifacts, "beacon-desktop.png"), fullPage: true });

    const mobile = await browser.newPage({ viewport: { width: 375, height: 812 }, isMobile: true });
    await mobile.goto(baseURL, { waitUntil: "networkidle" });
    const overflow = await mobile.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
    assert.ok(overflow <= 1, `mobile horizontal overflow: ${overflow}px`);
    await mobile.locator("#priority-filter").selectOption("critical");
    assert.equal(await mobile.locator("#incident-queue li:visible").count(), 1);
    await mobile.screenshot({ path: path.join(artifacts, "beacon-mobile.png"), fullPage: true });
    console.log(`Browser verification passed. Evidence: ${artifacts}`);
  } finally {
    await browser.close();
  }
})().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});

