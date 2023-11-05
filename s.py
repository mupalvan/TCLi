from instagrapi import Client

cl = Client()
cl.login("fapezhgol", "5540121341m")

user_id = cl.user_id_from_username("fapezhgol")
medias = cl.user_medias(user_id, 20)
cl.comment_like(17926777897585108)