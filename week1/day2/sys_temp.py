import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")
client = Groq(api_key=my_api_key)
model = "openai/gpt-oss-20b"
role = "user"
#prompt = "i love you baby!"
prompt = "suggest me a good name for my clothing company."
#message me role and content
message_system = {
    "role": "system",
   # "content": "You are my strict office colleague and who is also my manager."
    "content": "you are a brand manager who suggests name for my clothing company.suggest only one name."
}
message = {
    "role": role,
    "content": prompt
}

messages = [message_system, message]
#temperture by default is 0, means safe.
respone = client.chat.completions.create(model=model, messages=messages, temperature=0)
print(respone)


print("##############")
answer = respone.choices[0].message.content
print(answer)