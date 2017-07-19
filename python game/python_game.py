
print("You are a newborn cow on Douglaston farm. Are you a 'boy' or a 'girl'?")

#boy or girl?
gender=input()  #include a syntax to ask "please type boy or girl" if user types in other things
if gender == "boy":
    print('''You are sent to a special farm to get fattened up! You have a
    choice to eat 'corn' or 'grass', what do you choose?''')
elif gender == "girl":
    print('''You are sent to a special farm to be well taken care of!
5 YEARS LATER!You are in a field, just grazing on some grass.
From the corner of your eye you see a floral Gucci scarf laying in the
field. You walk over to it, do you 'eat it' or 'wear it'?''')

#girl-scarf choice
scarf_choice=input()
if scarf_choice == "eat it":
    print('''The scarf was delicious, but 24 hours later, your owner finds you
laying in a heap by the side of the barn, the scarf did not digest well. The
farm's doctor informs you that if the scarf is not removed from your stomach in
2 hours, you will die. Do you...'poop out the scarf' or 'leave it'?''')
elif scarf_choice =="wear it":
    print('''It just so happens that Vicbeefia Secret's manager was visiting
the farm that day. She sees you with the scarf on and is impressed. She asks
if you want to sign onto Vicbeefia Secret's cow modeling company.''' )

#boy-food choice
food_choice=input()
if food_choice=="corn":
    print("u die")
elif food_choice=="grass":
    print("u live")
