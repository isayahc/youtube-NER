import pysrt

def srt_to_list(srt_filename):
    # Open the SubRip file
    subs = pysrt.open(srt_filename, encoding='iso-8859-1')

    # Extract the text from each subtitle
    lines = [sub.text.replace('\n', ' ') for sub in subs]

    # Return the list of subtitles
    return lines

# Convert an example .srt file to a list of strings
subtitles = srt_to_list('example.srt')

# Print the list of subtitles
for subtitle in subtitles:
    print(subtitle)
