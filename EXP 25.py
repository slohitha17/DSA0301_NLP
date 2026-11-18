
from openai import OpenAI

api_key = input("Enter your OpenAI API key: ")
client = OpenAI(api_key=api_key)

prompt = input("Enter your prompt: ")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

print("\nGenerated Text:")
print(response.choices[0].message.content)
