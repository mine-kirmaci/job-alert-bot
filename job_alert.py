import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

BASE_URL = "https://www.youthall.com"
URL = "https://www.youthall.com/tr/jobs/"
SEEN_FILE = "seen_jobs.txt"

load_dotenv()
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# Daha önce görülen ilanları oku
if os.path.exists(SEEN_FILE):
    with open(SEEN_FILE, "r") as f:
        seen_links = set(f.read().splitlines())
else:
    seen_links = set()

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

jobs = soup.find_all("div", class_="jobs")

new_jobs = []

for job in jobs:
    a_tag = job.find("a")
    if not a_tag:
        continue

    link = a_tag.get("href")
    title_tag = job.find("h5")

    if not link or not title_tag:
        continue

    if link.startswith("/"):
        link = BASE_URL + link

    title = title_tag.text.strip()

    if link not in seen_links:
        new_jobs.append((title, link))
        seen_links.add(link)

# 📧 Mail gönderme fonksiyonu
def send_email(new_jobs):
    message = MIMEMultipart()
    message["From"] = EMAIL_ADDRESS
    message["To"] = EMAIL_ADDRESS
    message["Subject"] = "Youthall Yeni İlan Bildirimi"

    body = "Yeni ilanlar:\n\n"
    for title, link in new_jobs:
        body += f"{title}\n{link}\n\n"

    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(message)

# Yeni ilan varsa mail gönder
if new_jobs:
    print("Yeni ilan bulundu! Mail gönderiliyor...")
    send_email(new_jobs)
else:
    print("Yeni ilan yok.")

# Güncel listeyi kaydet
with open(SEEN_FILE, "w") as f:
    for link in seen_links:
        f.write(link + "\n")