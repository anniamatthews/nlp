# Joe Biden, Chris wallace, Donald Trump
# first names, last names, @ symbols
#typos
import re

# some helper methods 
def is_integer(s):
    try: 
        int(s) 
        return True
    except ValueError: 
        return False
    
def regex_check(tweet):
    res = []
    # remove spaces
    x = re.sub("\s", "", tweet)

    # check for biden
    b = re.search("joebiden|joe|biden", x, re.IGNORECASE)
    if b: 
        res.append('b')

    # check for wallace
    cw = re.search("chriswallace|chris|wallace", x, re.IGNORECASE)
    if cw: 
        res.append('cw')
    
    t = re.search("trump|donald|donaldtrump", x, re.IGNORECASE)
    if t: 
        res.append('t')

    return res


with open("Presidential_Debate.txt", "rt") as f: 
    # keep track of counts 
    counts = {'b':0,'t':0,'cw':0} 
    lines = f.readlines()
    for i in range(1, len(lines)):
        line = lines[i]
        suffix = lines[i-1][-5:] # last 4 characters of preceding line
        if is_integer(suffix) and int(suffix) / 2 == 1010 and not is_integer(line): 
            # print('suffix: ', suffix, 'corresponding line: ', line)
            matches = regex_check(line)
   
            if matches: 
                print('tweet: ', line, 'matches: ', matches ) # comment this if you only want to see number of matches
                for item in matches:
                    counts[item] +=1


    print(counts)

            
                

            




            


        





# print('number of lines in pres debate txt file: ', num_lines)



# a good way to find the line that has the exact tweet is to look at the line before it 
# if the line before it ends in 2020, and it's not a line of only the tweet id (large integer), then it's a tweet 

# either just the tweet itself 
# starts with "RT @username: "
# for this just use re.split(":", txt) to get the tweet by itself





# for i, line in enumerate(range(1, num_lines)):
#     # if the line before it ends in 2020 (txtfile[line_index -1] endsin('2020) && check if it's an interger number somehow)
#     print(txt_file[i])
#     # if txt_file[i - 1][-4:] == '2020' and not is_integer(line):
#     #    print(line)
       
    






# Donald Trump
'''
in any capacity of the string, even if surrounded by other characters (if there's an @ before it, will be counted)
Donald | Trump | DonaldTrump 
'''


# txt_file.close()