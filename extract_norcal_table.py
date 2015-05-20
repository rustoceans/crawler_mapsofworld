import urllib2

from bs4 import BeautifulSoup

url = ("http://www.mapsofworld.com/usa/states/california/"
       "map-of-northern-california.html")

page = urllib2.urlopen(url)
soup = BeautifulSoup(page)

tables = soup.findAll("table")
tables[3].find_all('td')

file_ = open('county.txt', 'w')
counties = [file_.write(td.text) for td in tables[3].find_all('td')]
