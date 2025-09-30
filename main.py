# our beautiful story
# (description, option 1, option 2)
stages = [
    # () = tuplies inside list, cant removed no matter what
#1
    ("You wake up. you decided to:", 
     "get out of bed",
     "stay in bed"),
#2
    ("congrats on leaving bed, you finally get to: ",
     "Brush teeth",
     "ignore your golden chompers"),
#3
    ("congrats on your beautiful whites, you go to: ",
     "the boring school",
     "that funny building"),
#4
    ("OOOOOOO boring man"," "," "),
#5
    ("Turns out it was a slaugther house and you are the victim T_T"," "," "),
#6
    ("Wow, lazy, what will you do now?",
     "continue sleeping",
     "Hope on phone"),
#7
     ("zzz"," "," "),
#8
     ("on them phone, what website now?:", 
      "Youtube",
      "The Hub"),
#9 
    ("ok you are normal"," "," "),
#10 
    ("GOONER!!!!!"," "," ")
]

#connects each stage together
routes = {
    0: (1,5),
    1: (2,5),
    2: (3,4),
    6: (7,8),
    8: (9,10)
}

current_stage_number = 0

#lets play it out
while True:

    #sets up current stage
    current_stage = stages[current_stage_number]

    #prints description
    print(current_stage[0])

    if current_stage_number not in routes.keys():
        break

    #prints out options
    print(f"[1] {current_stage[1]}\t[2] {current_stage[2]}")

    #self explanatory
    choice = int(input())

    #first one
    if choice == 1:
        current_stage_number = routes[current_stage_number][0]
    elif choice ==2 :
        current_stage_number = routes[current_stage_number][1]