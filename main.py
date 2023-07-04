from NER import entity_recognition, alt_entity_recognition
from srt_to_text import srt_to_list
from keyword_analysis import get_trends, plot_trends

import pandas as pd
from pytrends.exceptions import ResponseError
from pytrends.request import TrendReq

def get_trends(keywords):
    # Build the payload
    pytrends = TrendReq(hl='en-US', tz=360)

    try:
        pytrends.build_payload(keywords, cat=0, timeframe='today 5-y', geo='', gprop='')
    except ResponseError as e:
        print(f'Error: {e}')
        return None

    # Get the trends data
    trends_data = pytrends.interest_over_time()

    return trends_data


data = srt_to_list("example.srt")

data = " ".join(data)
entity_recognition(data)
data = alt_entity_recognition(data,entity_types=['PERSON','ORG',"GPE","PRODUCT"])
# keywords = data[:4]
keywords = data

# Split the list into chunks of 5 keywords each
chunks = [keywords[i:i+5] for i in range(0, len(keywords), 5)]

# Get the trends data for each chunk of keywords
trends_data = pd.DataFrame()
for chunk in chunks:
    chunk_data = get_trends(chunk)
    if chunk_data is not None:
        trends_data = pd.concat([trends_data, chunk_data], axis=1)

# Sort the data by popularity
# trends_data = trends_data.sum().sort_values(ascending=False)



# Get the trends data
# trend_data = get_trends(keywords)

# Plot the trends data
plot_trends(trends_data)

x=0