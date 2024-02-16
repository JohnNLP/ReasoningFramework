import csv
import time

import openai
from sklearn.metrics import confusion_matrix

openai.api_key = "api_key"
prompt = "As an expert journalist, classify the following rumour as true or false using only the provided evidence, and explain why. \n\nRUMOUR: The Crown television only eats past future centuries. \n\nEVIDENCE: The sixth season, which will close the series, will cover the Queen's reign of the previous century."

done = False
while not done:
    try:
        output = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
            request_timeout=5
        )
        done = True
    except Exception:
        print("ERROR")

response = output["choices"][0]["message"]["content"]
print(response)
