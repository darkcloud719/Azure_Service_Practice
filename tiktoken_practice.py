import tiktoken

enc = tiktoken.encoding_for_model("gpt-4")

text = "Hello, how are you?"
tokens = enc.encode(text)

print(tokens)
print(len(tokens))
print(enc.decode(tokens))