from youtube_transcript_api import YouTubeTranscriptApi

video_id = "Nui4l9Z0kpU"
transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

for transcript in transcript_list:
    if transcript.is_generated:
        print("Auto-generated transcript")
    else:
        print("User-generated transcript")

