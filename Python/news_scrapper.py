import requests
from bs4 import BeautifulSoup
import MySQLdb

"""
Depreciated Database access.

"""
host = "mock.host"
user = "mock.user"
password = "mock.password"
database = "mock.database"
db = MySQLdb.connect(host, user, password, database)

"""
You need to make your class do this:
class def:
title
author
picture
short description
link
"""
query = db.cursor()
class News:
	def __init__(self, title):
		self.title = title.replace("\'", "\\\'")
		self.author = ""
		self.picture = ""
		self.shortdesc = ""
		self.link = ""
	def createAuthor(self, author):
		self.author = author
	def createPicture(self, picture):
		self.picture = picture
	def createShortDesc(self, shortdesc):
		self.shortdesc = shortdesc.replace("\'", "\\\'")
	def createLink(self, link):
		self.link = link
	def printTitle(self):
		return 'Title is: %s' % self.title + '\nAuthor is: %s' % self.author + '\nPicture is: %s' % self.picture + '\nShortDesc is: %s' % self.shortdesc + '\nLink is: %s' % self.link
	def recordNews(self, City_ID):
		return "INSERT INTO NEWS (city_id, author, title, picture_link, short_description, link) VALUES ('%s','%s','%s','%s','%s','%s');" % (City_ID, self.author, self.title, self.picture, self.shortdesc, self.link)
def scrapNews(url, city_Id):
	r = requests.get(url)
	soup = BeautifulSoup(r.content, "html.parser")
	increment = 0
	newsID = 0	
	dict = {}
	
	# get title.
	for title in soup.findAll("title"):
		if increment < 2:
			increment += 1
			# Trying to exclude CDATA's "<City name>'s patch" in the first two iterations.
		else:
			dict[newsID] = News(title.text)
			newsID += 1
		# We want to increment the python dictionary containing different class instances.

	# get author.
	newsID = 0
	for author in soup.findAll("dc:creator"):
		dict[newsID].createAuthor(author.text)
		newsID += 1
	newsID = 0
	
	# get picture link
	for picturelink in soup.findAll("media:thumbnail"):
		dict[newsID].createPicture(picturelink.get("url"))
		newsID += 1
	newsID = 0
	increment = 0

	# get short description
	for shortDesc in soup.findAll("description"):
		if increment < 2:
			increment += 1
		else:
			dict[newsID].createShortDesc(shortDesc.text)
			newsID += 1
	newsID = 0
	# get link
	for link in soup.findAll("guid"):
		dict[newsID].createLink(link.text)
		newsID += 1

	for k,v in dict.items():
		query = db.cursor()
		insertSQL = v.recordNews(city_Id)
		query.execute(insertSQL)
"""
Now, we need to find out the number of news instances we will need.
The RSS feed will collect a couple of news.
"""

url_dict = {"annandale":"http://patch.com/feeds/virginia/annandale", 
"arlington":"http://patch.com/feeds/virginia/arlington-va",
"ashburn":"http://patch.com/feeds/virginia/ashburn",
"burke":"http://patch.com/feeds/virginia/burke",
"centreville":"http://patch.com/feeds/virginia/burke",
"chantilly":"http://patch.com/feeds/virginia/chantilly",
"clarendon":"http://patch.com/feeds/virginia/clarendon",
"dale city":"http://patch.com/feeds/virginia/dalecity",
"del ray":"http://patch.com/feeds/virginia/delray",
"fairfax":"http://patch.com/feeds/virginia/fairfaxcity",
"falls church":"http://patch.com/feeds/virginia/fallschurch",
"fredericksburg":"http://patch.com/feeds/virginia/fredericksburg", 
"herndon":"http://patch.com/feeds/virginia/herndon",
"lake ridge":"http://patch.com/feeds/virginia/lakeridge",
"leesburg":"http://patch.com/feeds/virginia/leesburg",
"lorton":"http://patch.com/feeds/virginia/lorton",
"manassas":"http://patch.com/feeds/virginia/manassas",
"manassas park":"http://patch.com/feeds/virginia/manassaspark",
"mclean":"http://patch.com/feeds/virginia/mclean",
"mount vernon":"http://patch.com/feeds/virginia/mountvernon",
"oakton":"http://patch.com/feeds/virginia/oakton", 
"reston":"http://patch.com/feeds/virginia/reston",
"tysons corner":"http://patch.com/feeds/virginia/tysonscorner",
"vienna":"http://patch.com/feeds/virginia/vienna",
"woodbridge":"http://patch.com/feeds/virginia/woodbridge-va",
"alexandria":"http://patch.com/feeds/virginia/greateralexandria",
"kingstowne":"http://patch.com/feeds/virginia/kingstowne",
"occoquan": "http://patch.com/feeds/virginia/lakeridge"
}


query.execute("SELECT * FROM CITY")
for row in query.fetchall():
	city_name = row[1].lower()
	print city_name
	if url_dict.has_key(city_name):
		scrapNews(url_dict[city_name], row[0])

db.commit()
db.close()