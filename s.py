import instaloader

# Get instance
L = instaloader.Instaloader()
USER = "mupalvan"
PASSWORD = "Muhammad@1379"
# Optionally, login or load session
L.two_factor_login(USER, PASSWORD)        # (login)
L.interactive_login(USER)      # (ask password on terminal)
L.load_session_from_file(USER)