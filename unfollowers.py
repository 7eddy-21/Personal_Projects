import instaloader

# 1. Setup
L = instaloader.Instaloader()
USER = "teddyindetie"

try:
    # 2. Use the session file we created in Step 1
    print(f"Attempting to load session for {USER}...")
    L.load_session_from_file(USER)
    print("Session loaded successfully!\n")

    # 3. Load your profile
    profile = instaloader.Profile.from_username(L.context, USER)

    # 4. Fetch Followers
    print("Fetching your followers... (this takes time if you have many)")
    followers = set()
    for follower in profile.get_followers():
        followers.add(follower.username)

    # 5. Fetch Following
    print("Fetching the accounts you follow...")
    following = set()
    for followee in profile.get_followees():
        following.add(followee.username)

    # 6. Compare lists
    not_following_back = following - followers

    # 7. Print Results
    print(f"\n--- DONE! {len(not_following_back)} accounts don't follow you back ---")
    for username in sorted(not_following_back):
        print(f" - {username}")

except Exception as e:
    print(f"\nERROR: {e}")
    print("Tip: If you see '401 Unauthorized', wait 30 minutes and try Step 1 again.")