import feedparser as fp
link1 = "http://rlsbb.to/feed/"
rss = fp.parse(link1)

# print number of entries in feed
print('total entries:', len(rss.entries))

# print publish dates and feed URLs
for i in rss.entries:
	print('published:', i['published'][0:10])  # print date published
	print(i['title'])
  #Seems to be some issues around the links.. might be the feeds itself.
  for j in i.links:
		print(j['href'])  # print URLs
	print('-------------------------------------------------')
