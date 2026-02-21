n = input("Enter the duration of the songs: ")
song_duration = n.split()
playlist = [0] * len(song_duration)

total_duration = 0
len_playlist = 0
invalid = False

for i in range(len(song_duration)):
    playlist[i] = int(song_duration[i])

    if playlist[i] <= 0:
        print("Invalid Playlist")
        invalid = True
        break
    else:
        total_duration += playlist[i]
        len_playlist += 1

if not invalid:
    repetitive = False
    for duration in playlist:
        if playlist.count(duration) > 1:
            repetitive = True
            break

    print("Total Duration:", total_duration, "seconds")
    print("Songs:", len_playlist)

    if total_duration < 300:
        print("Category: Too Short Playlist")
        print("Recommendation: Add more songs")

    elif total_duration > 3600:
        print("Category: Too Long Playlist")
        print("Recommendation: Consider reducing playlist length")

    elif repetitive:
        print("Category: Repetitive Playlist")
        print("Recommendation: Add variety")

    elif min(playlist) != max(playlist):
        print("Category: Balanced Playlist")
        print("Recommendation: Good listening session")

    else:
        print("Category: Irregular Playlist")
        print("Recommendation: Modify playlist for better balance")