name = input("what is your name ")
greeting = "hello"
seperator = " "
dont_like = "I do not like"
i_like = "I like"
print (greeting + seperator + name)

color = input("what is your favorite color ")
if color == "blue":
    print ("I don't like Blue")
elif color == "Blue":
    print ("I don't like Blue")
elif color == "red":
    print ("I like Red")
elif color == "Red":
    print ("I like Red")
else:
    print (dont_like + seperator + color)
    
animal = input("what is your favorite animal ")
if animal == "cats":
    print ("I don't like Cats")
elif animal == "Cats":
    print ("I don't like Cats")
elif animal == "cat":
    print ("I don't like Cats")
elif animal == "Cat":
    print ("I don't like Cats")
else:
    print (i_like + seperator + animal)
    
candy = input("do you like snikers ")
if candy == "yes":
    print ("I hate snikers")
elif candy == "Yes":
    print ("I hate snikers")
elif candy == "no":
    print ("same I hate snikers")
elif candy == "No":
    print ("same I hate snikers")

tv = input("do you like to watch tv ")
if tv == "yes":
    print ("same i like to watch tv")
elif tv == "Yes":
    print ("same i like to watch tv")
elif tv == "no":
    print ("okay")
elif tv == "No":
    print ("okay")
    
friend = input("do you want to be friends ")
if friend == "yes":
    print ("yay")
elif friend == "Yes":
    print ("yay")
elif friend == "no":
    print ("okay")
elif friend == "No":
    print ("okay")
    
    
print ("lets play a game this is how the game works i will ask you which direction you want to go you chose one then i will tell you what you find to attack any monsters you find you have to say hit your goal is to save the frog")
stage_1 = input("do you want to go left right or forwards ")
if stage_1 == "left":
    print ("you find nothing")
elif stage_1 == "Left":
    print ("you find nothing")
    
elif stage_1.lower() == "forwards":
    stage_1 = input("you have found a goblin you must attack it ")
    if stage_1 == "hit":
        print ("you have defeted the goblin")
elif stage_1 == "Hit":
    print ("you have defeted the goblin")
    
elif stage_1 == "right":
    print ("you find nothing")
elif stage_1 == "Right":
    print ("you find nothing")


stage_2 = input("do you want to go left right or forwards ")
if stage_2 == "forwards":
    print ("you find nothing")
elif stage_2 == "Forwards":
    print ("you find nothing")
    
elif stage_2.lower() == "left":
    stage_2 = input("you have found a goblin you must attack it ")
    if stage_2 == "hit":
        print ("you have defeted the goblin")
elif stage_2 == "Hit":
    print ("you have defeted the goblin")
    
elif stage_2 == "right":
    print ("you find nothing")
elif stage_2 == "Right":
    print ("you find nothing")


stage_3 = input("do you want to go left right or forwards ")
if stage_3 == "forwards":
    print ("you find nothing")
elif stage_3 == "Forwards":
    print ("you find nothing")
    
elif stage_3.lower() == "right":
    stage_3 = input("you have found a goblin you must attack it ")
    if stage_3 == "hit":
        print ("you have defeted the goblin")
elif stage_3 == "Hit":
    print ("you have defeted the goblin")
    
elif stage_3 == "left":
    print ("you find nothing")
elif stage_3 == "Left":
    print ("you find nothing")
    
print ("you saved the frog")
