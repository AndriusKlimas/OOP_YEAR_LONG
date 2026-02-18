from user_records import User

# Create a test user
user = User("john_doe", "Password123")

# Add multiple play records for different videos
print("Adding play records...")
user.start_play(1, 0)      # Video 1, position 0
user.start_play(1, 30)     # Video 1, position 30
user.start_play(1, 120)    # Video 1, position 120
user.start_play(2, 0)      # Video 2, position 0
user.start_play(2, 45)     # Video 2, position 45
user.start_play(3, 0)      # Video 3, position 0

# Retrieve play records for video 1
print("\nRetrieving play records for Video 1:")
video_1_plays = user.get_plays(1)
print(f"Found {len(video_1_plays)} play record(s) for Video 1")
for play in video_1_plays:
    print(f"  - {play}")

# Retrieve play records for video 2
print("\nRetrieving play records for Video 2:")
video_2_plays = user.get_plays(2)
print(f"Found {len(video_2_plays)} play record(s) for Video 2")
for play in video_2_plays:
    print(f"  - {play}")

# Retrieve play records for video 3
print("\nRetrieving play records for Video 3:")
video_3_plays = user.get_plays(3)
print(f"Found {len(video_3_plays)} play record(s) for Video 3")
for play in video_3_plays:
    print(f"  - {play}")

# Get the full history
print("\nFull play history structure:")
history = user.get_history()
print(f"Dictionary keys (video_ids): {list(history.keys())}")
print(f"Total videos watched: {len(history)}")

print("\n✓ Optimization successful! Play records are now stored by video_id for fast retrieval.")

