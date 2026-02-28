from playwright.sync_api import sync_playwright

seeds = range(51, 61)
base_url = "https://24f2004980@ds.study.iitm.ac.in?seed="

total_sum = 0

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    for seed in seeds:
        url = f"{base_url}{seed}"
        page.goto(url)
        page.wait_for_selector("table")

        numbers = page.locator("table td").all_text_contents()
        
        for num in numbers:
            try:
                total_sum += int(num.strip())
            except:
                pass

    browser.close()

print("FINAL TOTAL:", total_sum)
