import urllib

tweets = open("/media/atanu/New Volume1/Tweet-analysis2/part-00004").read
data = urllib.urlencode({"text": tweets})
u = urllib.urlopen("http://text-processing.com/api/sentiment/", tweets)
the_page = u.read()
print (the_page)