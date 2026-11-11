import csv
from datetime import datetime


def reject(job):
    with open("rejected.csv", "a", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(
            file, fieldnames=["title", "company", "location", "remote","created_at","source","salary","contract_type","contract_time","description","url","reason"]
        )
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(
                {
                    "title": job["title"],
                    "company": job["company"],
                    "location": job["location"],
                    "remote": job["remote"],
                    "created_at": datetime.strptime(job["created_at"], "%d/%m/%Y").strftime("%d/%m/%Y"),
                    "source": job["source"],
                    "salary": job.get("salary", None),
                    "contract_type": job.get("contract_type", None),
                    "contract_time": job.get("contract_time", None),
                    "url": job["url"],
                    "reason": job["reason"]
                }
            )