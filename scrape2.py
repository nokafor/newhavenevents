from bs4 import BeautifulSoup
from urllib2 import urlopen

BASE_URL = "http://events.newhavenindependent.org/index.php/calendar/by_date/2015/06/07/" #june 7th

def get_today_events(section_url):
	html = urlopen(section_url).read()
	soup = BeautifulSoup(html, "lxml")
	# calendarToday = soup.find("div", "left") <-- see if beautiful soup can find things by id
	eventTitles = [h2.string for h2 in soup.findAll("h2", "title")]
	eventTimes = [h3.string for h3 in soup.findAll("h3")]
	# todays_events = [div.a.string for div in calendarToday.findAll("div")]
	return {"eventTitles": eventTitles,
			"eventTimes": eventTimes}

if __name__ == '__main__':
	events = get_today_events(BASE_URL)
	print 'Events: ', events