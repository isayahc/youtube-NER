from youtube_transcript_api import YouTubeTranscriptApi

video_id = "Nui4l9Z0kpU"
transcript = YouTubeTranscriptApi.get_transcript(video_id)

if transcript:
    print(transcript)
else:
    print("User-generated transcript does not exist")

