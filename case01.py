import urllib, urllib2, webbrowser

url = 'https://www.wsb.com/Assignment2/case01.php'
params = { 'age': 100 }
data = urllib.urlencode(params)

request = urllib2.Request(url, data)
response = urllib2.urlopen(request)

with open('results.html', 'w') as f:
	f.write(response.read())

webbrowser.open_new_tab('results.html')
