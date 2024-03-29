import urllib2
import sys
import os, socket
from bs4 import BeautifulSoup

socket.setdefaulttimeout(30)

def getTodayIndex():
    url = "http://explosm.net/comics/new"
    r = urllib2.urlopen(url)
    splits = r.geturl().split('/')
    index = splits.index('comics')+1
    today = splits[index]
    return int(today)

def startGrabbing(count):
    day = getTodayIndex()
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
                            splits = image_link.split('/')
                            author_filename = splits[len(splits)-2:]
                            write_file_name = `i`
                            if len(author_filename) == 2:
                                author, filename = author_filename
                                write_file_name = author + "_" + filename
                            f = open(os.path.join("comics",write_file_name), 'wb')
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
    path = r'comics'
    if not os.path.exists(path):
        os.makedirs(path)
    startGrabbing(count)
