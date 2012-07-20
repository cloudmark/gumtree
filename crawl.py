import re
import urllib
import sys
areas = [
		"marchmont", 
		"bruntsfield",
		"tollcross",
		"haymarket",
		"grassmarket",
		"abbeyhill",
		"royalmile",
		"sciennes",
		"bellevue ",
		"canonmills",
		"comelybank",
		"grange",
		"hillside",
		"inverleith",
		"meadowbank",
		"morningside",
		"stockbridge",
		"pleasance",
		"lothianroad"
]

BASE = "http://www.gumtree.com"
HOME_BASE = BASE + "/flatshare-offered/"

if len(sys.argv) <= 1:
	print "You did not supply a temporary file. "
	
else:
	file = sys.argv[1]
	f = open(file,'r')
	raw_lines = f.readlines()
	lines = []
	for raw_line in raw_lines: 
		arr = raw_line.split('\t'); 	
		if len(arr) >= 5:
			raw = arr[3].replace("\n","") 
			lines.append(raw)

	for area in areas: 
		sys.stderr.write("Area: %s\n" % area) 
		durl = HOME_BASE + area
		f = urllib.urlopen(durl)
		s = f.read()
		f.close()
	
		s = s.replace("\r"," ") 
		s = s.replace("\n", " ") 
		s = s.replace("\t", " ") 
		s = re.sub(' +', ' ', s)
		
		pattern = '<ul class="ad-listings ad-listings-style-row js_ads ">.*?</ul>'
		listing_pattern = '<a id="(?P<id>.*?)" class="description" title="(?P<title>.*?)" href="(?P<href>.*?)"'

		p = re.compile(pattern)
		items = p.findall(s)
	
		if len(items) > 1: 
			p2 = re.compile(listing_pattern)
			listings = p2.findall(items[0])

			for listing in listings: 
				(id, title, href) = listing 
				# href = BASE + href
				if href not in lines: 
					lines.append(href)
					sys.stderr.write('\t%s\n' % (href))
					print('N\t%s\t%s\t%s\t"%s"' % (id, title, href, area))
