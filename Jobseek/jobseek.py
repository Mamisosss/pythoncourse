import csv
import parse_arbeit
import parse_adzuna
from dotenv import load_dotenv

load_dotenv()

URL_arbeit = "https://www.arbeitnow.com/api/job-board-api?"
URL_adzuna = "https://api.adzuna.com/v1/api/jobs/fr/search/1?"


def main():
    jobs = parse_adzuna.parser(URL_adzuna) + parse_arbeit.parser(URL_arbeit)
    with open("joboffers.csv", "a", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(
            file, fieldnames=["title", "company", "location", "remote","created_at","source","salary","contract_type","contract_time","description","url"]
        )
        writer.writeheader()
        for job in jobs:
            writer.writerow(
                {
                    "title": job["title"],
                    "company": job["company"],
                    "location": job["location"],
                    "remote": job["remote"],
                    "created_at": job["created_at"],
                    "source": job["source"],
                    "salary": job["salary"],
                    "contract_type": job["contract_type"],
                    "contract_time": job["contract_time"],
                    "url": job["url"],
                    "description": job["description"]
                }
            )


if __name__ == "__main__":
    main()
