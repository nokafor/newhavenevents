import re

from bs4 import BeautifulSoup
from urllib2 import urlopen

def make_soup(section_url):
	html = urlopen(section_url).read()
	soup = BeautifulSoup(html, "lxml")
	return soup

# info new haven --> scrapes wayy too much, start at event with lowest time
def get_events1():
	BASE_URL = "https://www.google.com/calendar/"
	section_url = BASE_URL + "htmlembed?mode=AGENDA&src=4nlsdjc3i96afa5vkslbfro2gqb4j47c%40import.calendar.google.com&amp;ctz=America/New_York"
	soup = make_soup(section_url)

	today = soup.find("div", "date-section-today")
	# events = [tr for tr in today.findAll("tr", "event")]

	event_times = [td.string for td in today.findAll("td", "event-time")]
	event_names = [span.string for span in today.findAll("span", "event-summary")]
	event_links = [BASE_URL + a['href'] for a in today.findAll("a", "event-link")]
	
	return zip(event_names, event_times, event_links)

# visitor bureau calendar
def get_events2():
	BASE_URL = "http://www.visitnewhaven.com"
	section_url = BASE_URL + "/thingstodo/calevents/day"
	soup = make_soup(section_url)

	events = [div for div in soup.findAll("div", "eventdesc")]

	event_links = [BASE_URL + div.a['href'] for div in soup.findAll("div", "eventdesc")]
	
	event_descr = [div.a.text for div in soup.findAll("div", "eventdesc")]
	event_names = []
	event_times = []

	for description in event_descr:
		strs = re.split(r'[()]', description)
		event_names.append(strs[0].strip())

		times = strs[1].split("-")
		event_times.append(times[0].strip())
	return zip(event_names, event_times, event_links)

# yale calendar
def get_events3():
	section_url = "http://calendar.yale.edu/cal/opa"
	soup = make_soup(section_url)

	today = soup.find("table", "eventList")

	times = [td.text for td in today.findAll("td", "time")]

	# events = [td.ul for td in soup.findAll("td", "description")]
	event_names = [li.a.text for li in today.findAll("li", "titleEvent")]
	event_times = []
	event_links = [li.a['href'] for li in today.findAll("li", "titleEvent")]

	for time in times:
		if '/' in time:
			event_times.append("All day")
			# print 'found'
		else:
			t = time.split("-")
			event_times.append(t[0].strip())
			# event_times.append(time)

	# for event in events:
		# event_names.append([li.a.text for li in event.findAll("li", "titleEvent")])
		# event_links.append([li.a['href'] for li in event.findAll("li", "titleEvent")])
		# ev = [li for li in event.findAll("li", "")]
		# event_locations.append(ev)
	# event_locations = [li for li in events.findAll("li", "")]

	return zip(event_names, event_times, event_links)
