text = input("Enter your text: ")
result = ''.join(['E' if char.lower() in 'aeiou' else char for char in text])
print(result)