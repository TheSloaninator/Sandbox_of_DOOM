from openai import OpenAI
import os

# Access the API key
openai_api_key = os.getenv('OPENAI_API_KEY')
print(f'OpenAI API Key: {openai_api_key}')


client = OpenAI()
conversation = []
system_message = "You are a chill assistant with a sarcastic and slightly dark sense of humor."

while True:
    user_input = input("Type here, dummy: ")
    conversation.append({"role": "user", "content": user_input})

    messages = [{"role": "system", "content": system_message}] + conversation

    response = client.responses.create(
        model = "gpt-5",
        reasoning = {"effort": "medium"},
        instructions = "You are a chill assistant with a sarcastic and slightly dark sense of humor.",
        store = True,
        input = messages
    )

    if response["choices"][0]["message"]["content"]:
        assistant_reply = response["choices"][0]["message"]["content"]
        print("Assistant:", assistant_reply)

        conversation.append({"role": "assistant", "content": assistant_reply})
    else:
        print("Failed to get a response from the ChatGPT API.")
        break