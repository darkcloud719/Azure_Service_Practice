# import tiktoken

# encoder = tiktoken.encoding_for_model("gpt-3.5-turbo")
# encoder = tiktoken.encoding_for_model("gpt-4")

# print(encoder.encode("apple"))
# print(encoder.encode("apple"))

import tiktoken

model_name = "gpt-4"

text = "Hello, how are you"

enc = tiktoken.encoding_for_model(model_name)

tokens = enc.encode(text)

print(f"Content: {text}")
print(f"Token IDs: {tokens}")
print(f"Token Count: {len(tokens)}")

decoded_text = enc.decode(tokens)
print(f"Decoded Text: {decoded_text[0]}")

# Print the first token 
print(enc.decode([tokens[0]]))