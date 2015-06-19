from bs4 import BeautifulSoup
from urllib2 import urlopen

BASE_URL = "https://www.google.com/calendar/htmlembed?src=knd8ekcdkl45ibmr9f84t9jmd4%40group.calendar.google.com&amp;ctz=America/New_York%22%3Ehttps://www.google.com/calendar/htmlembed?src=knd8ekcdkl45ibmr9f84t9jmd4%40group.calendar.google.com&amp;ctz=America/New_York" # html version of park's map

def make_soup(section_url):
	html = urlopen(section_url).read()
	soup = BeautifulSoup(html, "lxml")
	return soup

def get_today_events(section_url):
	soup = make_soup(section_url)
	events = [td.a for td in soup.findAll("td", "cell-today")]
	return events

if __name__ == '__main__':
	events = get_today_events(BASE_URL)
	print 'Events: ', events