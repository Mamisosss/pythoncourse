import requests
from datetime import datetime

def parser(a):
    params = {
                "page" : 1
                }
    try:
        response = requests.get(a, params=params, timeout=(30, 60))
        response.raise_for_status()
        content = response.json()
    except requests.HTTPError:
        print("HTTP Error")
        return []
    except requests.Timeout:
        print("Timeout bro")
        return []
    except requests.ConnectionError:
        print("Timeout bro")
        return []
    arbeitlist = []
    for job in content["data"]:
        if len(job["job_types"]) == 2:
            contract_type, contract_time = job["job_types"]
        elif len(job["job_types"]) == 1:
            contract_type = job["job_types"]
            contract_time = ""
        else :
            contract_type, contract_time = ["",""]
        formatted_date = datetime.fromtimestamp(job["created_at"])
        arbeitlist.append(
            {
                "title": job["title"],
                "company": job["company_name"],
                "location": job["location"],
                "remote": job["remote"],
                "created_at": formatted_date.strftime("%d/%m/%Y"),
                "source": "arbeit",
                "salary": "",
                "contract_type": contract_type,
                "contract_time": contract_time,
                "url": job["url"],
                "description": job["description"]
            }
        )
    return arbeitlist