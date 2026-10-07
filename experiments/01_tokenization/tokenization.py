import tiktoken


text = "learning Generative AI with Python"

encoding = tiktoken.get_encoding("cl100k_base")

tokens = encoding.encode(text)

print("Original text:")
print(text)

print("\nToken IDs:")
print(tokens)

print("\nNumber of tokens:")
print(len(tokens))

print("\nDecoded tokens:")

for token in tokens:
    print(token, "->", encoding.decode([token]))


#import tiktoken


#encoding = tiktoken.get_encoding("cl100k_base")

###prompts = [
###  "I am a software engineer.",
#  "मैं एक सॉफ्टवेयर इंजीनियर हूँ।
#]

#for text in prompts:
#    tokens = encoding.encode(text)

#    print("-" * 50)
#    print("Text:", text)
#    print("Tokens:", tokens)
#    print("Token count:", len(tokens))