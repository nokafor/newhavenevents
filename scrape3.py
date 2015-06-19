from bs4 import BeautifulSoup
from urllib2 import urlopen

BASE_URL = "http://www.newhavenarts.org/calendar/calendar_embed.php"

def get_today_events(section_url):
	html = urlopen(section_url).read()
	soup = BeautifulSoup(html, "lxml")
	# calendar = soup.find("td", "bodytext")

	events_header = [div.strong for div in soup.findAll("div", "cal_header_title")]
	events_who = [div for div in soup.findAll("div", "cal_column_1")]
	events_when = [div for div in soup.findAll("div", "cal_column_2")]
	events_where = [div for div in soup.findAll("div", "cal_column_3")]

	return {"events_header": events_header,
			"events_who": events_who,
			"events_when": events_when,
			"events_where": events_where}

if __name__ == '__main__':
	events = get_today_events(BASE_URL)
	print 'Events: ', events
