phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for i in phone_numbers.values():
    i = i.replace('+','00')
    print("{}".format(i))