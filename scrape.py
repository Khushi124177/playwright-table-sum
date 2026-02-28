from playwright.sync_api import sync_playwright

seeds = range(51, 61)

BASE_URL = "https://sanand0.github.io/tdsdata/js_table/?seed=" # <-- yaha actual URL daalo

total_sum = 0

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    for seed in seeds:
        url = f"{BASE_URL}{seed}"
        print("Visiting:", url)

        page.goto(url, timeout=60000)
        page.wait_for_load_state("networkidle")

        cells = page.locator("table td").all_text_contents()

        for cell in cells:
            try:
                total_sum += int(cell.strip())
            except:
                pass

    browser.close()

print("FINAL TOTAL:", total_sum)
