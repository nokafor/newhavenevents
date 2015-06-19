from bs4 import BeautifulSoup
from urllib2 import urlopen

BASE_URL = "http://www.visitnewhaven.com/thingstodo/calevents/day"

def get_today_events(section_url):
	html = urlopen(section_url).read()
	soup = BeautifulSoup(html, "lxml")
	# calendar = soup.find("td", "bodytext")

	events = [div for div in soup.findAll("div", "eventdesc")]

	return events

if __name__ == '__main__':
	events = get_today_events(BASE_URL)
	print 'Events: ', events
