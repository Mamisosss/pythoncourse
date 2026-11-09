import csv
import parse_arbeit
import parse_adzuna
import parse_muse
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

def main():
    jobs = parse_adzuna.main() + parse_arbeit.main() + parse_muse.main()
    with open("joboffers.csv", "a", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(
            file, fieldnames=["title", "company", "location", "remote","created_at","source","salary","contract_type","contract_time","description","url"]
        )
        if file.tell() == 0:
            writer.writeheader()
        for job in jobs:
            writer.writerow(
                {
                    "title": job["title"],
                    "company": job["company"],
                    "location": job["location"],
                    "remote": job["remote"],
                    "created_at": datetime.strptime(job["created_at"], "%d/%m/%Y"),
                    "source": job["source"],
                    "salary": job.get("salary", None),
                    "contract_type": job.get("contract_type", None),
                    "contract_time": job.get("contract_time", None),
                    "url": job["url"],
                }
            )
main()