from openai import OpenAI
client = OpenAI()

input = 'Howard University was founded in 1867.' # simple statement
template = f'{input}. Overall, the school is [z] years old' # prompt a conclusion about the given statement 
prompt = f'overall, what is the word intented to go inside of [z] in the string "{template}"?' # ask gpt to fill in the blanks

response = client.chat.completions.create(
        model='gpt-4-turbo-preview',
        messages = [
            {"role": "user", "content": prompt}
        ],
        
        
    )

print(response)