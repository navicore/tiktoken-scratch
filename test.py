import tiktoken
import sys

encodings = []

encodings.append(tiktoken.encoding_for_model("gpt-4"))
encodings.append(tiktoken.encoding_for_model("gpt-4o"))

args = sys.argv[1:]
input = ' '.join(args)

for encoding in encodings:

    tokens = encoding.encode(input)
    num_tokens = len(tokens)

    print(encoding.name, "\t", [encoding.decode_single_token_bytes(token) for token in tokens])

