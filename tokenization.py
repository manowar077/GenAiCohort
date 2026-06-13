import tiktoken

encoding = tiktoken.encoding_for_model('gpt-3.5-turbo')

print("vocab size ",encoding.n_vocab) #1,00,277

text="the cat sat on the mat" #
token=encoding.encode(text)
print(token)

print("Token ",token) #6
my_token=[1820, 8415, 7731, 389, 279, 5634]
my_token=encoding.decode([1820, 8415, 7731, 389, 279, 5634])
print("Decoded token ",my_token) #the cat sat on the mat