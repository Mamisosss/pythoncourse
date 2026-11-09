import requests
from datetime import datetime
import os
from dotenv import load_dotenv
from decoder import decoder
from doctor import doctor
from config import Sources

load_dotenv()

def main():
    source = Sources[2] 
    if doctor(source) in ["OK (authentifié)","OK (sans clé)"]:
        return parser(source)
    else :
        return []

def parser(s):
    header = {"User-Agent": "jobfeed/0.1 (learning project)",
                "Accept": "application/json"}
    params = {}
    for k, v in s.get("credentials").items():
                if s.get("auth") == "query":
                        params[k] = os.getenv(v)
                else:
                        header[k] = os.getenv(v)
    try:
        response = requests.get(s.get("url"), headers=header, params=params, timeout=(30, 60))
        response.raise_for_status()
        content = response.json()
    except requests.HTTPError:
        print("credentials for Muse are missing or rejected")
        return []
    except requests.Timeout:
        print("Timeout bro")
        return []
    except requests.ConnectionError:
        print("Timeout bro")
        return []

    muselist = []
    for job in content["results"]:
        formatted_date = datetime.strptime(job["publication_date"], "%Y-%m-%dT%H:%M:%SZ")
        try:
            location = job["locations"][0].get("name", "")
        except IndexError:
            location = ""
        description = decoder(job["contents"])
        company = job["company"]
        url = job["refs"]
        muselist.append(
            {
                "title": job["name"],
                "company": company["name"],
                "location": location,
                "remote": "",
                "created_at": formatted_date.strftime("%d/%m/%Y"),
                "source": "muselist",
                "url": url["landing_page"],
                "description": description
            }
        )
    return muselist
if __name__ == "__main__":
    main()