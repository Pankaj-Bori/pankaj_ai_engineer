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
#3 prompt
prompt1="Hi"
prompt2="Explain time travel in detail under 100 words."
prompt3="Write a essay on mechine learning under 100 words."
prompts=[prompt1,prompt2,prompt3]
for prompt in prompts:
    message = {
        "role": role,
        "content": prompt
    }
    messages = [message]
    response = client.chat.completions.create(model=model, messages=messages, max_tokens=5000)
    usage = response.usage
    print(f"Prompt Tokens: {prompt}-->your_total_tokens: {usage.prompt_tokens}, Completion Tokens: {usage.completion_tokens}, Total Tokens: {usage.total_tokens}, finished_reason: {response.choices[0].finish_reason}")

# prompt = "Do you know Pankaj Bori ?"
# #message me role and content
# message = {
#     "role": role,
#     "content": prompt
# }

# messages = [message]
# respone = client.chat.completions.create(model=model, messages=messages)
# print(respone)

