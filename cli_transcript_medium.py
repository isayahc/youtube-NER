import argparse
from youtube_transcript_api import YouTubeTranscriptApi

def main():
    parser = argparse.ArgumentParser(description='Check if the transcript of a YouTube video is auto-generated or user-generated')
    parser.add_argument('video_id', type=str, help='the ID of the YouTube video')
    args = parser.parse_args()

    transcript_list = YouTubeTranscriptApi.list_transcripts(args.video_id)

    for transcript in transcript_list:
        if transcript.is_generated:
            print("Auto-generated transcript")
        else:
            print("User-generated transcript")

if __name__ == '__main__':
    main()

