try:
    import yt_dlp
    from datetime import timedelta
except ImportError as e:
    print(f"Error: {e.name} module is not installed. Please install it using the following command:")
    if e.name == 'yt_dlp':
        print("pip install yt-dlp")
    elif e.name == 'datetime':
        print("The datetime module is part of the Python standard library and should be available by default.")
    exit(1)

def get_playlist_duration(playlist_url):
    # Define the options for yt-dlp
    ydl_opts = {
        'quiet': True,  # Suppresses standard output messages
        'no_warnings': True,  # Suppresses warning messages
        'extract_flat': True,
        'force_generic_extractor': True,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Fetch playlist information
        playlist_info = ydl.extract_info(playlist_url, download=False)
        
        if 'entries' not in playlist_info:
            raise ValueError("Could not retrieve playlist information.")
        
        # Calculate the total duration
        total_duration = timedelta()
        for entry in playlist_info['entries']:
            duration = entry.get('duration', 0)
            total_duration += timedelta(seconds=duration)
    
    return total_duration

def format_duration(duration):
    total_seconds = duration.total_seconds()
    
    days, remainder = divmod(total_seconds, 86400)  # 86400 seconds in a day
    hours, remainder = divmod(remainder, 3600)      # 3600 seconds in an hour
    minutes, seconds = divmod(remainder, 60)        # 60 seconds in a minute
    
    total_hours = total_seconds / 3600

    return (f"{int(days)} days, {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds", 
            f"{total_hours:.2f} hours")

if __name__ == "__main__":
    playlist_url = input("Enter the YouTube playlist URL: ")
    try:
        total_duration = get_playlist_duration(playlist_url)
        duration_days_hours = format_duration(total_duration)
        print("Total Playlist Duration:", duration_days_hours[0])
        print("Total Playlist Duration in Hours:", duration_days_hours[1])
    except Exception as e:
        print("Error:", e)
