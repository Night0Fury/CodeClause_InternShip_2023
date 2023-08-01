import pyshorteners

def shortenurl(url):

    s = pyshorteners.Shortener()
    return s.tinyurl.short(url)

url = input('Enter the URL: ')

short_url = shortenurl(url)
print("The shortened URL is:", short_url)