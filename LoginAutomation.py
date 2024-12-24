from playwright.sync_api import sync_playwright
import json

def login_and_handle_prompt():
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=False, args=[
            '--disable-blink-features=AutomationControlled',
            '--disable-software-rasterizer',
            '--no-sandbox',
            '--disable-gpu'
        ])

        # Create a new browser context and page
        context = browser.new_context()
        page = context.new_page()

        # Go to the login page
        page.goto('https://www.suno.com/login')

        # Perform login steps
        page.click('img[alt="Sign in with Google"]')
        page.fill('input[type="email"]', 'harshithasamudrala2@gmail.com')
        page.click('text=Next')
        page.fill('input[type="password"]', 'H@numanthudu14')
        page.click('text=Next')



        # Wait for the banner's close button (X symbol) to appear and click it
        try:
            page.wait_for_selector('svg[class*="stroke-current"]', timeout=10000)  # SVG with 'stroke-current' class
            page.click('svg[class*="stroke-current"]')  # Click the SVG element
            print("Banner closed successfully.")
        except Exception as e:
            print(f"Error closing the banner: {e}")
            return



        # Save session cookies to a file
        cookies = context.cookies()
        with open("cookies.json", "w") as f:
            json.dump(cookies, f)

        print("Session saved successfully.")
        browser.close()

if __name__ == '__main__':
    login_and_handle_prompt()
