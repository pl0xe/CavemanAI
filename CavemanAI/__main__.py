import ollama

prompt = 'What was the last question I asked?'

message = {
    'role':'user',
    'content': prompt,
}

response = ollama.chat(
    model = 'caveman',
    stream = False,
    messages = [message]
)

print(response['message']['content'])
