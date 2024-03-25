import re
import matplotlib.pyplot as plt



def is_integer(s):
    try: 
        int(s) 
        return True
    except ValueError: 
        return False


with open("Presidential_Debate.txt", "rt") as f: 
    lines = f.readlines()
    highlights = {} # timestamp: count of tweets at timestamp
    for i in range(1, len(lines)):
        line = lines[i]
        suffix = lines[i-1][-5:] # last 4 characters of preceding line
        if is_integer(suffix) and int(suffix) / 2 == 1010 and not is_integer(line): 
            # get timestamp line
            time = lines[i-1].split(" ")[:4]
            minutes = time[-1]

            if re.search("\d{2}:\d{2}:\d{2}", minutes) != None:
                if minutes in highlights: 
                    highlights[minutes] += 1
                else: 
                    highlights[minutes] = 1
            
            

       
                
    print(highlights)
                
def plot_dict(dict): 
    keys = dict.keys()
    values = dict.values()

    plt.bar(keys, values)
    plt.xlabel('Timestamp')
    plt.ylabel('Count')
    plt.title("Tweet-Time Frequency")

    plt.show()


plot_dict(highlights)
