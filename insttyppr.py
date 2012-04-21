from Instapaper import Instapaper

# Load consumer_key and consumer_secret from disk
secrets_file = open('secrets.txt')

consumer_key = secrets_file.readline()
consumer_secret = secrets_file.readline()

instapaper = Instapaper(consumer_key, consumer_secret)
#instapaper.login("","")
#instapaper.list_bookmarks()

quit()
