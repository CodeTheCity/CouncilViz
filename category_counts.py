import json
from collections import defaultdict

with open("public/council_committee_JSON.json") as f:
    committee_list = json.load(f)

cat_comm = defaultdict(lambda: [])
comm_cat = {}

for c in committee_list:
    cat_comm[c["Category"]].append(c["Committee"])
    comm_cat[c["Committee"]] = c["Category"]

cat_comm_count = {}

for cat, comm in cat_comm.items():
    cat_comm_count["cat"] = len(comm)
    print(f"{cat} {len(comm)} {comm}")

with open("category_committee_count.json", "w") as f:
    f.write(json.dumps(cat_comm_count))
