import sys
import time
import csv
import os
import requests
from bs4 import BeautifulSoup

def main():
    if len(sys.argv) != 3:
        return
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.exists("cache"):
        os.makedirs("cache")

    with open(input_file, "r", encoding="utf-8") as f:
        countries = [line.strip() for line in f if line.strip()]

    with open(output_file, "w", encoding="utf-8", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["country", "city", "area", "population"])

        for country in countries:
            cache_path = os.path.join("cache", f"{country}.html")
            if os.path.exists(cache_path):
                with open(cache_path, "r", encoding="utf-8") as cf:
                    html = cf.read()
            else:
                try:
                    url = f"https://en.wikipedia.org/wiki/{country.replace(' ', '_')}"
                    resp = requests.get(url)
                    html = resp.text
                    with open(cache_path, "w", encoding="utf-8") as cf:
                        cf.write(html)
                except Exception:
                    writer.writerow([country, "", "", ""])
                    time.sleep(1)
                    continue

            soup = BeautifulSoup(html, "html.parser")
            infobox = soup.find("table", class_="infobox")
            capital = area = population = None

            if infobox:
                for row in infobox.find_all("tr"):
                    th = row.find("th")
                    td = row.find("td")
                    if not th or not td:
                        continue
                    th_text = th.get_text().strip().lower()
                    td_text = td.get_text().strip()

                    if "capital" in th_text and not capital:
                        capital = td_text.split(",")[0].split("(")[0].strip()
                    if "total" in th_text and ("area" in th_text or "km²" in td_text) and not area:
                        for part in td_text.replace(",", "").split():
                            if "km²" in part:
                                area = part.replace("km²", "").replace(" ", "")
                                break
                    if "population" in th_text and not population:
                        for part in td_text.replace(",", "").split():
                            if part.isdigit():
                                population = part
                                break

            writer.writerow([country, capital or "", area or "", population or ""])
            time.sleep(1)

if __name__ == "__main__":
    main()