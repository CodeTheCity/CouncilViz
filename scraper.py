from collections import defaultdict
import requests, json
from bs4 import BeautifulSoup
from dataclasses import dataclass, field, InitVar
from typing import List

@dataclass
class Meeting:
    title: str
    datetime: str
    detail_link: str
    webcast_link: str

@dataclass
class CommMember:
    name: str
    page_link: str = ""
    image_link: str = ""

@dataclass
class Committee:
    name: str
    category: str = ""
    link: str = ""
    council_description: str = ""
    members: List[CommMember] = field(default_factory=list)
    meetings: List[Meeting] = field(default_factory=list)
    
with open("public/council_committee_JSON.json") as f:
    committee_list = json.load(f)

cat_comm = defaultdict(lambda: [])
comm_cat = {}

for c in committee_list:
    cat_comm[c["Category"]].append(c["Committee"])
    comm_cat[c["Committee"]] = c["Category"]
    
# for cat, comm in cat_comm.items():
#     print(f"{cat} {len(comm)} {comm}")

def get_members(link, domain):
    l = []
    r = requests.get(link)
    soup = BeautifulSoup(r.content, "html.parser")
    if m_title := soup.find("a", attrs={"name": "#MEM"}):
        m_list = m_title.find_next("ul")
        print(m_list)
        for m in m_list.find_all("li"):
            if lnk := m.find("a"):
                cm = CommMember(lnk.text)
                cm.page_link = domain+lnk.get("href")
            else:
                cm = CommMember(m.text)
            l.append(cm)
    return l

# def get_meetings(

start = "https://committees.aberdeencity.gov.uk/mgListCommittees.aspx?bcr=1"
domain = "https://committees.aberdeencity.gov.uk/"
r = requests.get(start)
comm_soup = BeautifulSoup(r.content, "html.parser")
content_div = comm_soup.find("div", attrs={"class": "mgContent"})
#print(content_div)

committees = []
for comm in content_div.find_all("li"):
    a = comm.find("a")
    c = Committee(name=a.text)
    if c.name == "Council":
        #TODO: decide how we want to handle full council
        continue
    
    c.link = domain+a.get("href")
    if c.name in comm_cat.keys():
        c.category = comm_cat[c.name]
    else:
        c.category = "Other"
    c.members = get_members(c.link, domain)
    committees.append(c)

for c in committees:
    print(c)


