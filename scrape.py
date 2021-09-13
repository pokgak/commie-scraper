import jq
import csv
import json
import requests

API_ENDPOINT = "https://shopee.com.my/api/v4/item/get"

with open("targets.csv", newline="") as targetsfile:
    targets = csv.reader(targetsfile, delimiter=",")
    targets.__next__()
    for row in targets:
        r = requests.get(API_ENDPOINT, params={"itemid": row[1], "shopid": row[2]})

        result = jq.compile(".data").input(text=r.text).all()
        with open(f"data/{row[0]}_{row[1]}-{row[2]}.json", "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2)
