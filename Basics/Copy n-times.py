file = "bear1.txt"

with open(file, 'a+') as qwe:
    qwe.seek(0)
    content = qwe.readlines()
    i = 0
    for i in range(2):
        qwe.writelines(content)
    qwe.close()

