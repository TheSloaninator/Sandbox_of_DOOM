from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-5",
    input="A full, spoiler-heavy list of the major battles from Dimension 20's Fantasy High: Freshman Year. Including every significant combat encounter from the core season only."
)

with open ('/home/so/dev/ChatGPT/response.txt', 'a') as f:
    print(response.output_text, file=f)
