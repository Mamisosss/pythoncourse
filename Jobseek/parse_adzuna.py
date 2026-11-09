import requests
from datetime import datetime
import os
from dotenv import load_dotenv
from decoder import decoder
from doctor import doctor
from config import Sources

load_dotenv()

def main():
    source = Sources[0] 
    if doctor(source) == "OK (authentifié)":
        return parser(source)
    else :
        return []

def parser(s):
    header = {"Accept": "application/json"}
    params = {
            "what" : "project manager implementation",
            "max_days_old" : 5
            }

    for k, v in s.get("credentials").items():
        if s["auth"] == "query":
                params[k] = os.getenv(v)
        else:
                header[k] = os.getenv(v)
    try:
        response = requests.get(s.get("url"), headers=header, params=params, timeout=(30, 60))
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
        description = decoder(job["description"])
        company = job["company"]
        adzunalist.append(
            {
                "title": job["title"],
                "company": company["display_name"],
                "location": area["display_name"],
                "remote": "",
                "created_at": formatted_date.strftime("%d/%m/%Y"),
                "source": "adzuna",
                "salary": job.get("salary_min", 0),
                "contract_type": job.get("contract_type"),
                "contract_time": job.get("contract_time"),
                "url": job["redirect_url"],
                "description": description
            }
        )
    return adzunalist
if __name__ == "__main__":
    main()