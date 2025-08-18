from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-5",
    reasoning={"effort": "medium"},
    previous_response_id="resp_68a251508d708196b2e82055f13449d30c9344dde0b20fe4",
    input=[{"role": "user", "content": "The high‑confidence list of the big set‑piece combats will work. Spoilers are fine, I have seen the season already."}],
    store=True,
)

with open ('/home/so/dev/ChatGPT/response.txt', 'a') as f:
    print(response.output_text, file=f)