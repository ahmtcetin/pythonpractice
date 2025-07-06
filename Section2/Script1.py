import re

text = "Hello Fucker !!!"
pattern = r"Hello"

result = re.match(pattern, text)
print(result)

pattern = r"!!!"
result = re.match(pattern, text)
print(result)

pattern = r"Error"
result = re.match(pattern, text)
print(result)

pattern = r"Fucker"
result = re.match(pattern, text)
print(result)

# *********************************

text = "Hello Fucker !!!"
pattern = r"Hello"

result = re.search(pattern, text)
print(result)

pattern = r"!!!"
result = re.search(pattern, text)
print(result)

pattern = r"Error"
result = re.search(pattern, text)
print(result)

pattern = r"Fucker"
result = re.search(pattern, text)
print(result)

if result:
    print(result.group())

result = re.search(r'\d+', 'There are 123 apples')
print(result.group())