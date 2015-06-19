from bs4 import BeautifulSoup
from urllib2 import urlopen

BASE_URL = "https://www.google.com/calendar/htmlembed?mode=AGENDA&src=4nlsdjc3i96afa5vkslbfro2gqb4j47c%40import.calendar.google.com&amp;ctz=America/New_York"

def make_soup(section_url):
	html = urlopen(section_url).read()
	soup = BeautifulSoup(html, "lxml")
	return soup

def get_today_events(section_url):
	soup = make_soup(section_url)

	today = soup.find("div", "date-section-today")
	events = [tr for tr in today.findAll("tr", "event")]
	
	return events

if __name__ == '__main__':
	events = get_today_events(BASE_URL)
	print 'Events: ', events