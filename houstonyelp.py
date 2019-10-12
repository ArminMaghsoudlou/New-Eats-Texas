from bs4 import BeautifulSoup
import requests
import csv

page = requests.get('https://www.yelp.com/search?find_desc=Best+New+Restaurants&find_loc=Houston%2C+TX')
soup = BeautifulSoup(page.content, 'html.parser')
mains = soup.find_all('div', {"lemon--div__373c0__1mboc mainAttributes__373c0__1r0QA arrange-unit__373c0__1piwO arrange-unit-fill__373c0__17z0h border-color--default__373c0__2oFDT"})
secondarys = soup.find_all('div', {"lemon--div__373c0__1mboc secondaryAttributes__373c0__7bA0w arrange-unit__373c0__1piwO border-color--default__373c0__2oFDT"})
#thirds = soup.find_all('p', {"lemon--p__373c0__3Qnnj text__373c0__2pB8f text-color--orange__373c0__3n-R2 text-align--left__373c0__2pnx_ text-size--small__373c0__3SGMi"})

main = mains[1]
bizname = main.find("a").text
print(bizname)

secondary = secondarys[1]
location = secondary.find("span").text
print(location)

#third = thirds[1]
#whenOpened = third.find("span").text
#print(whenOpened)


filename = "yelp_houston.csv"
f = open(filename, "w")
header = "Rest_Name, Street Address, City, State"
f.write(header)

name_list = []
loc_list = []

for main in mains:
    try:
        bizname = main.find("a").text
        #print("Rest_Name: " + bizname)
        name_list.append(bizname)
    except:
        print(None)
for secondary in secondarys:
    try:
        location = (secondary.find("span").text) + "," + " Houston, Texas"
        #print("Location: " + location)
        loc_list.append(location)
    except:
        print(None)

for i in range(len(name_list)):
    f.write("\n" + name_list[i] + "," + loc_list[i])

f.close()


