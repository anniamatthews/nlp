import pandas as pd
from openai import OpenAI
client = OpenAI()

df1 = pd.read_csv('/Users/test/Desktop/openai-env/assignment-1/four_star_reviews_sample.csv') # four star reviews 
df2 = pd.read_csv('one_star_reviews_sample.csv') # one star reviews 

def get_sentiment(text): 
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages= [
            {"role": "user", "content": f"Sentiment analysis of the following text:\n{text}\n"}
        ],
        max_tokens= 15
    )
    
    #completion.choices[0].message
    sentiment = response.choices[0].message.content
    return sentiment 


# comment either one out to focus on one dataframe
# for index, row in df1.iterrows():
#     res = get_sentiment(row['Reviews'])
#     print(f'{res}\n')


for index, row in df2.iterrows():
    res = get_sentiment(row['Reviews'])
    print(f'{res}\n')


