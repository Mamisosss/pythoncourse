import csv
import re
from config import Title, Location
from datetime import datetime, timedelta, time
from accepted import accept
from rejected import reject

def main():
    cutoff = datetime.strptime(((datetime.today() - timedelta(hours=48)).strftime("%d/%m/%Y")), '%d/%m/%Y')
    with open("joboffers.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                total_title = 0
                total_location = 0
                converted_date = datetime.strptime(row["created_at"], '%d/%m/%Y')
                if converted_date >= cutoff :
                    for title in Title:
                        if not re.search(title, row["title"].lower().strip()):
                            total_title += 1
                    for location in Location:
                        if not re.search(location, row["location"].lower().strip()):
                            total_location += 1        
                    if total_title == len(Title):
                        row["reason"] = "title"
                        reject(row)
                    elif total_location == len(Location):
                        row["reason"] = "location"
                        reject(row)
                    else :
                        accept(row)
                else :
                    row["reason"] = "old"
                    reject(row)

main()