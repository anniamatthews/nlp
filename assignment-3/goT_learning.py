from openai import OpenAI
client = OpenAI()
import hashlib

# remove duplicate lines
# path of the input and output files
Outlist = []
InFile = r'goT_highlight1.txt'
# holding the line which is already seen
lines_present = set()
# opening the output file in write mode to write in it


# turn file into array of unique lines
for l in open(InFile, "r"):
   # finding the hash value of the current line
      # Before performing the hash, we remove any blank spaces and new lines from the end of the line.
      # Using hashlib library determine the hash value of a line.
      hash_value = hashlib.md5(l.rstrip().encode('utf-8')).hexdigest()
      if hash_value not in lines_present:
         Outlist.append(l)
         lines_present.add(hash_value)


listToStr = ' '.join([str(elem) for elem in Outlist])



with open("goT_highlight1.txt", "rt") as f: 
    
    # zero shot using GPT3
    response = client.chat.completions.create(
        model='gpt-3.5-turbo-1106',
        messages = [
            {"role": "user", "content": f"Using zero shot can you use the Tweets from ${listToStr} to summarize what happened during this scene?"},
        ],
        
        
    )
    sentiment_3_zeroShot = response.choices[0].message.content

    # zero shot using GPT4
    response2 = client.chat.completions.create(
        model='gpt-4-1106-preview',
        messages = [
            {"role": "user", "content": f"Using zero shot can you use the Tweets from ${listToStr} to summarize what happened during this scene?"},
        ],
        max_tokens=100
        
        
    )
    sentiment_4_zeroShot = response2.choices[0].message.content



    # comparison
    response3 = client.chat.completions.create(
        model='gpt-4-vision-preview',
        messages = [
            {"role": "user", "content": f"Can you compare the results from ${sentiment_3_zeroShot} and ${sentiment_4_zeroShot}?"},
        ],
        max_tokens=100
        
        
    )
    comparison = response3.choices[0].message.content



# uncomment whichever one you want to see 
# print(sentiment_3_zeroShot)
# print(sentiment_4_zeroShot)
# print(comparison)







