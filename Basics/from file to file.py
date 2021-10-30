with open('bear1.txt', 'r') as rbear:
    content = rbear.read()

first_90_characters = content[0:90]

with open('first.txt', 'w') as new:
    new_content = new.write(first_90_characters)

help(open)

with open("bear1.txt", "r") as qwe:
    content = qwe.read()
    qwe.seek(0)
with open("bear2.txt", "a") as qwe2:
    content2 = qwe2.write(content)



