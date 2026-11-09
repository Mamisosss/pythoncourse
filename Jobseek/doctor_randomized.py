import requests
import random
import os
from dotenv import load_dotenv
from config import adzuna_url, arbeit_url, themuse_url

load_dotenv()

sources = [
    {"name": "arbeitnow", "url": arbeit_url, "auth": None, "api_id": None,"api_key":None, "required": False},
    {"name": "adzuna",    "url": adzuna_url, "auth":"idp" , "api_id":os.getenv("ADZUNA_API_ID"),"api_key":os.getenv("ADZUNA_API_KEY"), "required": True},
    {"name": "themuse",    "url": themuse_url, "auth":"query" , "api_id":None,"api_key":os.getenv("THEMUSE_API_KEY"), "required": True}
]

UA_POOL = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
]

def main():
    for source in sources:
        if source["required"] is True and source["api_key"] is None:
            print(source["name"] + " : no key")
        else:
            print(source["name"] + " : " + str(doctor(source)))


def doctor(source):
    session = requests.Session()
    header = {"User-Agent": random.choice(UA_POOL),
              "Accept": "application/json"}
    params = {}
    if source["auth"] == "idp":
        params = {
                    "app_id" : source["api_id"],
                    "app_key" : source["api_key"]
                    }       
    elif source["auth"] == "header":
        params = {"api_key": source["api_key"]}
    elif source["auth"] == "query":
        params = {"api_key": source["api_key"]}
    elif source["auth"] == "header":
        header["api_key"] = source["api_key"]
    try :
        response = session.get(source["url"], headers=header, params=params)
        status = response.status_code
        if status == 200:
            return "OK"
        else:
            return status
    except (requests.ConnectionError, requests.Timeout):
            return "connection issue"     

if __name__ == "__main__":
    main()