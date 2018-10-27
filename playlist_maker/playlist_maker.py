from apiclient.discovery import build

API_KEY = "your api key here"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
QUERY_TERM = "cat"

def search_by_keyword():
    youtube = build(
      YOUTUBE_API_SERVICE_NAME, 
      YOUTUBE_API_VERSION,
      developerKey=API_KEY
    )
    search_response = youtube.search().list(
      q=QUERY_TERM,
      part="id,snippet",
      maxResults=1
    ).execute()

    videos = []

    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            videos.append("https://www.youtube.com/watch?v=%s" % (search_result["id"]["videoId"]))
    return videos

filename_in = 'playlist.txt'
filename_out = 'playlist _with_links.txt'
print ("File name in: "+filename_in)
print ("File name out: "+filename_out)

fin = open(filename_in, 'r')
fout = open(filename_out, 'w')
print ("Start searching...")
print("========================================")


line = fin.readline()
while line:
    print (line)
    QUERY_TERM = line
    videos = search_by_keyword()
    #print(videos)
    fout.write((str(videos).replace("['", "")).replace("']", "")+'\n')
    line = fin.readline()
	
fin.close()
fout.close()

print("========================================")
print("Files closed")
print("All done!")