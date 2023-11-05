import instaloader

# Get instance
L = instaloader.Instaloader()
USER = "fapezhgol"
PASSWORD = "5540121341m"
# Optionally, login or load session
L.login(USER, PASSWORD)
for post in L.get_hashtag_posts("pcmod"):
    L.download_post(post, target='#'+"pcmod")