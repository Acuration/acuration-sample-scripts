from litellm import completion

response = completion(
            model="ollama/mistral:7b-instruct", 
            messages = [{ "content": "list top 10 climate tech companies in JSON format","role": "user"}], 
            api_base="http://localhost:11434",
            stream=False
            )
print(response)
for chunk in response:
  print(chunk)
