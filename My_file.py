str = input("Enter the string here: ")

dic = {}  # empty dict created

for i in str:
    if i in dic:
        dic[i] += 1  # if item is already inside dict then latest data updated

    else:
        dic[i] = 1


print(dic)

#print(a)
