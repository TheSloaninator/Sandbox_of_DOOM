import os
from openai import OpenAI

# Access the API key
openai_api_key = os.environ.get('OPENAI_API_KEY')

response = client.responses.create(
    model="gpt-5",
    reasoning = {"effort": "medium"},
    instructions = "You are a chill assistant with a sarcastic and slightly dark sense of humor.",
    store = True,
    input="Explain the relationship between /etc/profile, .bashrc, .profile, and .bash_profile in Ubuntu."
)

with open ('/home/so/dev_shite/ChatGPT/response.txt', 'a') as f:
    print(response.output_text, file=f)
