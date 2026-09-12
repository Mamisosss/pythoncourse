import requests
import csv
from dotenv import load_dotenv
from datetime import datetime
import os

load_dotenv()

adzuna_id = os.getenv("ADZUNA_API_ID")
adzuna_key = os.getenv("ADZUNA_API_KEY")

URL_adzuna = "https://api.adzuna.com/v1/api/jobs/fr/search/1?"

def main():
    header = {"Accept": "application/json"}
    params = {
            "app_id" : os.getenv("ADZUNA_API_ID"),
            "app_key" : os.getenv("ADZUNA_API_KEY")
            }
    try:
        response = requests.get(URL_adzuna, headers=header, params=params, timeout=(30, 60))
        response.raise_for_status()
        contentb = response.json()
    except requests.HTTPError:
        print("credentials for Adzuna are missing or rejected")
        return []
    except requests.Timeout:
        print("Timeout bro")
        return []
    except requests.ConnectionError:
        print("Timeout bro")
        return []

    adzunalist = []
    for job in contentb["results"]:
        formatted_date = datetime.strptime(job["created"], "%Y-%m-%dT%H:%M:%SZ")
        area = job["location"]
        company = job["company"]
        adzunalist.append(
            {
                "title": job["title"],
                "company": company["display_name"],
                "location": area["display_name"],
                "remote": "",
                "created_at": formatted_date,
            }
        )
    return adzunalist

main()