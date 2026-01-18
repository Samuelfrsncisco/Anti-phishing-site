import re

def check_url(url):
    score = 0

    if not url.startswith("https"):
        score += 1

    if len(url) > 75:
        score += 1

    if re.search(r"\d+\.\d+\.\d+\.\d+", url):
        score += 1

    keywords = ["login", "verify", "secure", "update", "account", "bank"]
    for k in keywords:
        if k in url.lower():
            score += 1

    if score >= 3:
        print("🚨 HIGH RISK PHISHING SITE")
    else:
        print("✅ LOW RISK")

url = input("Enter URL: ")
check_url(url)