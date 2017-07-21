

list_alpha=["a", "b", "c", "d", "e", "f", "g"]
new_list=[]

for letter in range(0, len(list_alpha), 3):
    new_list.append(list_alpha[letter])
    print(new_list)
