import os
import json
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

#structure it
from pydantic import BaseModel
class Complaint(BaseModel):
    name: str
    product: str
    issue: str
    request: str
    order_number: str
    email: str
    phone_number: str
    address: str
schema = Complaint.model_json_schema()

response_format ={"type": "json_object"}

system_prompt = f"""
You are a helpful assistant that extracts information from customer complaints.
The extracted information should be based on the following schema and give a valid JSON response.
{schema}
"""

messages_system = {
    "role": "system",
    "content": system_prompt
}

text = "Hello, my name is Pankaj Bori. I bought a macbook from your store. it is not working properly. i want to return it and get a refund. Please help me with the process. My order number is 123456789. My email address is abc@def.com. My phone number is 1234567890. My address is 123 Main Street, City, State, ZIP Code."
prompt = f"""
The following is a customer complaint. Please extract the following information from the complaint.
{text}
"""
#message me role and content
message = {
    "role": role,
    "content": prompt
}

#sytem message and user message
messages = [messages_system, message]
respone = client.chat.completions.create(model=model, messages=messages, response_format=response_format)
# print(respone)


# print("##############")
answer = respone.choices[0].message.content
print(answer)

#how to study it
raw_json = answer
data_file = json.loads(raw_json)
complaint = Complaint(**data_file)

# Print the extracted information
print(complaint.name)
print(complaint.product)
print(complaint.issue)
