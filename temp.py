import lxml.html
from urllib.request import urlopen

tree = lxml.html.parse(urlopen('https://tenki.jp/forecast/6/31/6310/28100/'))
html = tree.getroot()

for a in html.xpath('//dd[@class="high-temp temp"]/span[@class="value"]'):
    today_max = a.text
    break

for a in html.xpath('//dd[@class="low-temp temp"]/span[@class="value"]'):
    today_low = a.text
    break

print("Today's Kobe's ")
print("Max_temp:", today_max)
print("Low_temp:", today_low)