from random import*

#list of names
names=["Pete", "John", "Mary", "Lenny", "Kathy", "Sarah",]
last_names=["brown", "white", "smith", "johnson", "beiber", "mack"]

#list of names used
names_used=[]
last_names_used=[]

for x in range(len(names)):
    #get a random index for first and last name
    random_first= names[randint(0, len(names)-1)]
    random_last=last_names[randint(0, len(last_names)-1)]

    #if names are already used, repeat the random choosing
    while random_first in names_used:
        random_first=names[randint(0,len(names)-1)]
    while random_last in last_names_used:
        random_last=last_names[randint(0, len(last_names)-1)]

    #add the names onto "names used" list
    names_used.append(random_first)
    last_names_used.append(random_last)

    print(random_first + "  "+random_last)
