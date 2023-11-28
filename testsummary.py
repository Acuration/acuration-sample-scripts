import transformers
text_example = "The tower is 324 meters (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. Its base is square, measuring 125 meters (410 ft) on each side. During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world, a title it held for 41 years until the Chrysler Building in New York City was finished in 1930. It was the first structure to reach a height of 300 meters. Due to the addition of a broadcasting aerial at the top of the tower in 1957, it is now taller than the Chrysler Building by 5.2 meters (17 ft). Excluding transmitters, the Eiffel Tower is the second tallest free-standing structure in France after the Millau Viaduct."
from transformers import pipeline
summarizer = pipeline("summarization", model = "google/pegasus-xsum")
test = summarizer(text_example)
print(test)

print("USING MODEL: facebook/bart-large-cnn")
from transformers import pipeline
summarizer = pipeline("summarization", model = "facebook/bart-large-cnn")
test = summarizer(text_example)
print(test)

print("USING MODEL: google/pegasus-xsum")

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model = AutoModelForSeq2SeqLM.from_pretrained('google/pegasus-xsum')
tokenizer = AutoTokenizer.from_pretrained('google/pegasus-xsum')

tokens_input = tokenizer.encode("summarize: "+ text_example, return_tensors='pt', max_length=512, truncation=True)
ids = model.generate(tokens_input, min_length=80, max_length=120)
summary = tokenizer.decode(ids[0], skip_special_tokens=True)

print(summary)

print("USING MODEL: facebook/bart-large-cnn")
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")

tokens_input = tokenizer.encode("summarize: "+text_example, return_tensors='pt', max_length=512, truncation=True)
ids = model.generate(tokens_input, min_length=80, max_length=120)
summary = tokenizer.decode(ids[0], skip_special_tokens=True)

print(summary)




