import json

with open('config.json', 'r') as f:
    config = json.load(f)


Sources = config["api"]
Title = config["title"]
Location = config["location"]