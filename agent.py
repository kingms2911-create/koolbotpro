import os
import asyncio
from playwright.async_api import async_playwright
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-2.0-flash-exp')

async def execute_task(prompt: str):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        print(f"Task Started: {prompt}")
        await page.goto("https://www.google.com")
        await page.fill("textarea[name='q']", prompt)
        await page.keyboard.press("Enter")
        await page.wait_for_timeout(3000)
        
        screenshot_bytes = await page.screenshot()
        await browser.close()
        
        return {"status": "completed", "task": prompt, "message": "Browser task executed on Render virtual environment."}
