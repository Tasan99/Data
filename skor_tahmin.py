import requests
from bs4 import BeautifulSoup as bs

url = "https://www.mackolik.com/futbol/canli-sonuclar"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = bs(response.content, 'html.parser')

    # Örnek olarak, canlı maç verilerini çekelim.
    live_matches = soup.find_all("div", class_="match-row__main-info")

    for match in live_matches:
        home_team = match.find("span", class_="home-team").text.strip()
        away_team = match.find("span", class_="away-team").text.strip()
        score = match.find("span", class_="score").text.strip()

        print(f"{home_team} vs {away_team}: {score}")
else:
    print("Sayfa yüklenirken bir hata oluştu. Hata kodu:", response.status_code)
