import csv
from config import Title, Location
from datetime import datetime, timedelta, time

def main():
    accepted = []
    with open("joboffers.csv", "r") as file:
        reader = csv.DictReader(
            file)
        for row in reader:
            for value in Title and location in Location:
                if value in row["title"].lower().strip() and row["location"] in Location and row["created_at"] >= ((datetime.today() - timedelta(hours=48)).strftime("%d/%m/%Y")) :
                    accepted.append(row)
    print(accepted)


main()