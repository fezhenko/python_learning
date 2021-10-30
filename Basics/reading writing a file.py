with open("C:/python_create_a_file_pls.txt", "w") as new_file:
    new_content = new_file.write("Hello world!\nsecond row\nthird row")

with open("C:/python_create_a_file_pls.txt", "r") as content_file:
    content = content_file.read()

print(content)

with open("bear1.txt", "r") as bear:
    content = bear.read()

print(content[0:90])

with open("bear1.txt", "r") as bear:
    content = bear.read()
