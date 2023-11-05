import instaloader

# Get instance
L = instaloader.Instaloader()
USER = "fapezhgol"
PASSWORD = "5540121341m"
# Optionally, login or load session
L.two_factor_login(USER, PASSWORD)        # (login)
L.interactive_login(USER)      # (ask password on terminal)
L.load_session_from_file(USER)