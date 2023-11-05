import instaloader

# Get instance
L = instaloader.Instaloader()
USER = "fapezhgol"
PASSWORD = "5540121341m"
L.login(USER, PASSWORD)        # (login)
L.interactive_login(USER)      # (ask password on terminal)
L.load_session_from_file(USER) 