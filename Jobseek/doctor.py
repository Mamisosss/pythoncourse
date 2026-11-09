import requests
import os
from dotenv import load_dotenv
from config import Sources

load_dotenv()


def main():
    for s in Sources:
        missing = []
        for param, var in s.get("credentials").items():
            if os.getenv(var) is None:
                missing.append(var)
        if s.get("type") == "mandatory" and missing:
                print(s["name"] + " : no key " + " , ".join(missing))
        else:
            print(s["name"] + " : " + str(doctor(s)))


def doctor(source):
    header = {"User-Agent": "jobfeed/0.1 (learning project)",
                  "Accept": "application/json"}
    params = {}
    if not source.get("auth") is None:
        for k, v in source.get("credentials").items():
            if source["auth"] == "query":
                    params[k] = os.getenv(v)
            else:
                    header[k] = os.getenv(v)
    try :
        response = requests.get(source["url"], headers=header, params=params, timeout=(30, 60))
        status = response.status_code
        if status != 200:
             return status
        elif status == 200 and source.get("type") == "mandatory":
            return "OK (authentifié)"
        elif status == 200 and source.get("type") == "optional":
            missing = []
            for param, var in source.get("credentials").items():
                if os.getenv(var) is None:
                    missing.append(var)
            if missing:
                return "Ok (sans clé)"
            else:
                return "OK (authentifié)"
        else:
            return "OK"
    except (requests.ConnectionError, requests.Timeout):
            return "connection issue"     

if __name__ == "__main__":
    main()