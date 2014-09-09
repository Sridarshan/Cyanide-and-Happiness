import urllib2
import sys
import os, socket
from bs4 import BeautifulSoup

socket.setdefaulttimeout(10)

def startGrabbing(count):
    day = 3677
    for i in xrange(count):
        url = "http://explosm.net/comics/" + `day`
        try:
            response = urllib2.urlopen(url)
            data = response.read()
            soup = BeautifulSoup(data)
            images = soup.find_all('img')
            for image in images:
                if image.has_attr('alt'):
                    image_link = image['src']
                    if "play-button" not in image_link:
                        try:
		            print "image link : " + image_link
		            image_response = urllib2.urlopen(image_link)
		            image_data = image_response.read()
		            f = open(os.path.join("comics",`i`), "w")
		            f.write(image_data)
		            f.close()
		        except:
		            pass
                        print "+"
        except:
            pass
        day -= 1
    
	

if __name__ == "__main__":
    count = 10
    if len(sys.argv) > 1:
        count = int(sys.argv[1])
    startGrabbing(count)
