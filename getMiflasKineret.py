import requests

from bs4 import BeautifulSoup
#
# get page
response = requests.get('http://kineret.org.il/miflasim/')
# let's soup the page
content = BeautifulSoup(response.content, 'html.parser')
# header
height = content.find("span", attrs={"class": "hp_miflas_height"})
height = height.get_text(strip=True)
date = content.find("span", attrs={"class": "hp_miflas_date"})
date = date.get_text(strip=True)
header = date + " " + height

# Get Change
miflas_change = content.find("div", attrs={"id": "hp_miflas_info"})
miflas_change.get_text(strip=True)
today_data = miflas_change.findAll("li")
full_message = header + "\n"
for line in today_data[:-1]:
    full_message = "\n" + full_message + line.get_text(strip=True).replace("❯", "").replace("מאתמול",
                                                                                            " מאתמול").replace(
        "מפלס הכינרת", "מפלס הכינרת ").replace("לדף המפלס המפורט", "").replace("משלשום",
                                                                               " משלשום") + "\n"
print(full_message)
