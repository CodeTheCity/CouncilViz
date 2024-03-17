from collections import defaultdict
import requests, json
from bs4 import BeautifulSoup
from dataclasses import dataclass, field, InitVar, asdict
from typing import List

@dataclass
class Meeting:
    title: str
    detail_link: str = ""
    webcast_link: str = ""

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

def soupify(link):
    r = requests.get(link)
    return BeautifulSoup(r.content, "html.parser")
    
def get_members(link, domain):
    l = []
    s = soupify(link)
    if m_title := s.find("a", attrs={"name": "#MEM"}):
        m_list = m_title.find_next("ul")
        for m in m_list.find_all("li"):
            if lnk := m.find("a"):
                cm = CommMember(lnk.text)
                cm.page_link = domain+lnk.get("href")
            else:
                cm = CommMember(m.text)
            l.append(cm)
    return l
def get_meeting_link(s):
    for lnk in s.find_all("a"):
        if "Browse meetings and agendas for this committee" in lnk.text:
            return lnk.get("href")

def get_meetings(link, domain):
    meetings = []
    s = soupify(link)
    if m_title := s.find("div", {"class": "mgTableTitleTxt"}):
        m_list = m_title.find_next("ul")
        for m in m_list.find_all("li"):
            lnk = m.find("a")
            metg = Meeting(lnk.text)
            metg.detail_link = domain+lnk.get("href")
            meetings.append(metg)
    return meetings

start = "https://committees.aberdeencity.gov.uk/mgListCommittees.aspx?bcr=1"
domain = "https://committees.aberdeencity.gov.uk/"
comm_soup = soupify(start)
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
    c.meetings = get_meetings(domain+get_meeting_link(soupify(c.link)), domain)
    committees.append(c)
    print(".", end="", flush=True)
print("")

cmt_json = json.dumps([asdict(c) for c in committees], indent=4)
with open("committees.json", "w") as f:
    f.write(cmt_json)
    

