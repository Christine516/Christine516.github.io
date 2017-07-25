
#boy or girl?
 #include a syntax to ask "please type boy or girl" if user types in other things
gender=input("You are a newborn cow on Douglaston farm. Are you a 'boy' or a 'girl'?")
while gender!="boy" and gender!="girl":
    gender=input("Type boy or girl-sorry for the limited gender options :()")

if gender == "boy":
    print("You are sent to a special farm to get fattened up!")
#boy-food choice
    food_choice=input("You have a choice to eat 'corn' or 'grass', what do you choose?")
    while food_choice!="corn" and food_choice!="grass":
        food_choice=input("Stop being picky, chose either 'corn' or 'grass'!")
    if food_choice=="corn":
        print("The corn was genetically modified and the scientists that genetically modified it messed up the corn's DNA. The corn has formed a mutation that makes it deadly if consumed. You are dead.")
    elif food_choice=="grass":
        print("You chose a healthy life of natural leafy greens! However, with grass being the only food in your diet, you have to eat an immense amount of grass. You missed the cow biology lesson last semester due to the flu so you never realized that plants have a natural sugar, glucose. With all the glucose you have consumed you contract diabetes." )
        medical_choice=input("The only way to maintain your diabetes is to take shots but you do not like sharp needles. Do you 'take shots' anyway or 'refuse shots")
        while medical_choice!="take shot" and medical_choice!="refuse shots":
            medical_choice=input("FOLLOW DIRECTIONS AND CHOOSE EITHER 'take shots or'refuse shots'")
        if medical_choice=="take shots":
            print("You live a long but painful life, full of needles and suffering. THE END")
        elif medical_choice=="refuse shots":
            print("You die, but at least youre no longer struggling...")
elif gender == "girl":
    print("You are sent to a special farm to be well taken care of! 5 YEARS LATER!You are in a field, just grazing on some grass. From the corner of your eye you see a floral Gucci scarf laying in the field. ")
#girl-scarf choice
    scarf_choice=input("You walk over to it, do you 'eat it' or 'wear it'?")
    if scarf_choice == "eat it":
        print("The scarf was delicious, but 24 hours later, your owner finds you laying in a heap by the side of the barn, the scarf did not digest well. The farm's doctor informs you that if the scarf is not removed from your stomach in 2 hours, you will die. Do you...'poop out the scarf' or 'leave it'?")
        if scarf_choice=="poop out the scarf":
            print("Good choice, you live, however, you are emotionally scarred. You decide to just stick to eating cow food")
        elif scarf_choice=="leave it":
            print("You made a horrible life decision. You die...")
    elif scarf_choice =="wear it":
        print("It just so happens that Vicbeefia Secret's manager was visiting the farm that day. She sees you with the scarf on and is impressed. She asks if you want to sign onto Vicbeefia Secret's cow modeling company." )
        modeling_choice=input("Do you 'accept' the offer or 'decline'?")
        if modeling_choice=="accept":
            print ("Wow your famous but fame comes with a cost... You become anorexic and die.")
        elif modeling_choice=="decline":
            print ("You're not famous but that is alright because you just dogded higher chances of eating disorders. You continue being a happy go lucky cow and end up having many cute babies!THE END")
