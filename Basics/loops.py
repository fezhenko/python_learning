colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]

#for i in colors:
    #if i>50:
        #print(i)

for i in colors:
    if isinstance(i, int):
        print(i)

colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]
for i in colors:
    if type(i) == int:
        print(i)