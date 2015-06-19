from bs4 import BeautifulSoup
from urllib2 import urlopen

BASE_URL = "http://calendar.southernct.edu/?d=2015-06-07&m=1" #june 7th
BASE_URL2 = "http://vems.southernct.edu/VirtualEMS/BrowseEvents.aspx"
BASE_URL3 = "http://www.southernctowls.com/calendar.aspx"

def make_soup(section_url):
	html = urlopen(section_url).read()
	soup = BeautifulSoup(html, "lxml")
	return soup

def get_university_events(section_url):
	soup = make_soup(section_url)
	calendar = soup.find("section", id="events")

	events = [ul.li for ul in calendar.findAll("ul")]

	return events

def get_stucenter_events(section_url):
	soup = make_soup(section_url)
	today = soup.find("td", "todayCell")

	events = [ul.li for ul in today.findAll("ul")]
	# return today
	return False

def get_lyman_events(section_url):
	soup = make_soup(section_url)
	return False

def get_residence_events(section_url):
	soup = make_soup(section_url)
	return False

def get_athletic_events(section_url):
	soup = make_soup(section_url)
	today = soup.find("td", "composite_cal_today")

	events = [div for div in today.findAll("div", "composite_cal_item")]

	return events
	# return False

if __name__ == '__main__':
	events = get_university_events(BASE_URL)
	print 'University Events: ', events

	events = get_athletic_events(BASE_URL3)
	print 'Athletic Events: ', events

	# events = get_stucenter_events(BASE_URL)
	# print '\nStudent Center Events: ', events
