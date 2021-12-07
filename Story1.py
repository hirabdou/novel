print("Welcome to Abandoned House! This is a choice-based story about how four teenagers go in an abandoned house on Halloween, and mysterious things occur.")
print("Directions:\nTo pick a choice, enter the number that is in parentheses next to the choice. There will be at least two different choices for ALL inputs. Example: If the story tells you 'Left (1) or Right (2)?', you would enter '1' to go left, and vice versa.\n\n")
ending = {"Secret" : 0, "Bad" : 0, "Good":0, "Best":0}
choices = ['1','2','3']

while True:
    alive = ['Tyler', 'John', 'Reese', 'Sam']
    dead = []
    Sam_key = 0
    answer = input('\n\nAfter a long night, Tyler, Reese, Samantha and John finally get enough candy to go back home. During their walk, they noticed an abandoned house on Elm Street. "We should go in, see if there is anything interesting to take." John declares. "That is too creepy, what if someone is in there waiting for someone like us to go in?" Samantha warned. The group is indecisive on whether they should go to the house or not.\nPress (1) to go to the abandoned house..\n')
    while answer not in choices:
        answer = input("Please try again.\n")
    if answer == '1':
        print('\nWalking up the eerie steps to the door, the anxious group makes their way into the house.\n\nAs they walk in, the glooming lights flicker a little as they walk on the creaking floorboards. All of them in unison ask, "Do you hear that?", as they all point to different areas of the house. Each person in the group walks toward the sound, but it is coming from different rooms for each of them.\nWill they make it out alive?\n')

        #First character
        answer = input('\n\nTyler...\n\nAs Tyler makes his way to the kitchen, he catches a glimpse of a gloomy shadow passing the entrance. In the kitchen, he notices a note on the wall. It reads.. "Will you run (1) or will you stay (2)?" Suddenly, there is loud screeching heading towards you. What will you do?\n')
        while answer not in choices:
            answer = input("Please try again\n")
        if answer == "1":
            alive.remove("Tyler")
            dead.append("Tyler")
            print("\nTyler runs for his life, as he burst through the unhinged back door of the kitchen to the outside!\n\nTyler hears the sounds getting closer and closer. Too worried about the noise, he was not looking ahead and trips on a branch...\n\nThe noise stops. SHIINNNG\n Tyler is stabbed through the chest with a metal sword!\n")
        if answer == "2":
            print("\nTyler looks for the first place to hide... the closet!!\n\nHe dashes to the closet and closes the door rapidly. He holds his breath in as the sounds slowly start to get louder and closer. \n\nThere is a brief silence...")
            answer = input("Should Tyler come out (1) or wait a little longer (2)?")
            while answer not in choices:
                answer = input("Please try again.\n")
            if answer == '1':
                alive.remove("Tyler")
                dead.append("Tyler")
                print("Tyler thinks the entity is not there anymore, and proceeds to open the door, when all of a sudden... A sword impales him through the closet door, and retracts, leaving Tyler in a pool of blood in the closet!\n")
            if answer == '2':
                print("Tyler not trying to make any noise, not even breathing. The sound of a sword starts again, but slowly starts to fade away. Tyler survives the pursuit!\n\n")


        #Second character
        while True:
            
            #Part One
            
            answer=input('\n\nSam...\n\nSam walks towards the basement in a distracted manner. Since the basement was very dark, Sam could only rely on the faint light of his cell phone to walk down the stairs." clomp" " clomp " " clomp..." When he reached the bottom of the stairs, a light illuminated his eyes, and he took a closer look, "Hey! I found a treasure box!!!" He shouted.\nHe cautiously walked towards the treasure box. It was a box made of gold. Strangely, in this dark basement, this golden box glowed with an extremely shining light. What will you do? (Will Sam ignore the box and continue explore (1) OR Open the golden box (2)?)\n')
            while answer not in choices:
                answer = input("Please try again.\n")
            if answer == '1':
                print('\n\nSam is keep walking foward...')
            if answer =='2':
                answer=input('\n\nSam opens the box and there is a golden key inside. Sam picks up the key, and all of a sudden, dozens of small spiders crawl out from the box. What will you do? (Will you stomp them to death (1) OR Run away (2)?\n')
                while answer not in choices:
                    answer = input("Please try again.\n")
                if answer =='1':
                    alive.remove("Sam")
                    dead.append("Sam")
                    print('\n\nMore little spiders crawl out from under the box and devour her. Sam courageously died!')
                    break
                if answer == '2':
                    Sam_key = 1
                    print('\n\nSam turns around and run frantically toward the stairs. At this point, Sam finds the basement door is locked, Sam kicks the door hard, but unfortunately the door is too strong. Just when Sam is desperate, he finds that the basement becomes very quiet. So, Sam walks back down the stairs in fear. Sam finds that the spiders have disappeared as well as the golden box. Sam is startled, but he turns on his cell phone flashlight and keeps moving forward. ')

            #Part Two
        
            answer=input('\n\n\nSam looks around the basement. With the light of his phone, Sam notices a huge cross being hung on the wall. There is a black coffin under the cross. Sam walks over to it. What will you do? (Open the coffin (1) OR Ignore it (2))\n')
            while answer not in choices:
                answer = input("Please try again")
            if answer =='1':
                 answer = input('\n\nSam find a human skeleton. The human skeleton is holding a green gemstone tightly in its hand. What will you do? (Take the gemstone away (1) OR Ignore the gemstone and continue the adventure (2)?)\n')
                 while answer not in choices:
                     answer = input("Please try again")
                 if answer == '1':
                     print('\n\nSam forcibly breaks the hand of skeleton and picks up the gem. At that moment, Sam feels a strong force, which makes Sam faint. After waking up Sam finds himself outside the house, but the jewel in his hand has disappeared. Sam have escaped!')
                     break
                 elif answer == '2':
                     print('\n\nThe coffin magically closes after Sam leaves. He keeps walking foward...')
            elif answer =='2':
                 print('\n\nSam keeps walking foward...')

            #Part Three
                 
            answer=input('\n\n\nSam continues his adventure. At this point, Sam finds a dusty bookshelf. There are many books on the shelf, but one book catches his eyes. This is the only book that has no dust on it, as if it was recently moved. What will you do? (Pick up the book from the bookshelf (1) OR continue his adventure (2)?)\n')
            while answer not in choices:
                answer = input("Please try again")
            if answer =='1':
                print('\n\nSam picks up a book...')
            if answer =='2':
                answer=input('\n\n Select your action: Open Golden box(1) OR Coffin(2) OR Bookshelf(3)\n')
                while answer not in choices:
                    answer = input("Please try again")
                if answer =='1':
                    alive.remove("Sam")
                    dead.append("Sam")
                    print('\n\n Sam walks back to the Golden box. After a few seconds hestitate, he opens the box. Countless spiders crawl out from under the box and devour Sam. Sam has died!')
                    break
                if answer == '2':
                    alive.remove("Sam")
                    dead.append("Sam")
                    print('\n\n Sam opens the coffin, and he finds a skeleton inside. He looks at this skeleton carefully. Suddenly, the skeleton clutch Sam and pulls him into the coffin. And the coffin magically closed itself.')
                    break
                if answer == '3':
                    print('\n\nSam picks up a book...')

            #Part Four
                    
            answer = input('\n\n\nSuddenly, a violent vibration comes from under his feet. The floor Sam were stepping on with both feet suddenly opened and Sam fell. Sam get up from the ground. Fortunately, Sam is not injured. Sam looks around and sees a ritual platform is placed in the middle of the room. There is a large chalice on the ritual platform, but other than that there is nothing else in the room. Sam walk over to the ritual platform, and Sam notice that there a key-shaped groove carved out of the base of the chalice. What will you do? (Put the key into the groove (1) OR Take up the chalice (2)?)')
            while answer not in choices:
                answer = input("Please try again")
            if answer == '1':
                  if Sam_key == 1:
                      print('\n\nThe stone walls on the left opens up an exit, which Sam find is a stone stairway. Sam walk over to try to find out the end of the passage and see a beautiful starry sky. Sam know this is the way to outside, so Sam walk up the stair…')
                      break
                  else:  
                      print('\n\n Sam checks his pockets, but he seems to have no key. Please select another option.')
                      answer = input( '\n\n What will you do? (Take up the chalice (2)?)')
                      while answer not in choices:
                          answer = input("Please try again")
                      if answer == '2':
                          alive.remove("Sam")
                          dead.append("Sam")
                          print('Countless small spiders crawl up from the ground, Sam run away in fear, however, Sam find that he have no way to escape, and finally Sam are swallowed by the spider swarm.')
            elif answer == '2':
                alive.remove("Sam")
                dead.append("Sam")
                print('Countless small spiders crawl up from the ground, Sam run away in fear, however, Sam find that he have no way to escape, and finally Sam are swallowed by the spider swarm.')
                
                        
            break

        #Third character
        
        print("\n\nReese...\n\nReese walks uncontrollably into the bedroom. It is a small, old bedroom. The twin-size bed covered in dust makes Reese realize that this might be the children's room. At this moment, the pumpkin on the table catch Reese attention. Compared with the whole room, this pumpkin carving is very new, without a trace of dust. But its creepy smile gives Reeze a sense of fright.\n")
        answer = input('\n\nReese walks over by the pumpkin...(Smash the pumpkin(1) OR Put a candy into the pumpkin(2)) What will you do?\n')
        while answer not in choices:
            answer = input("Please try again")
        if answer == "1":
            alive.remove("Reese")
            dead.append("Reese")
            print("\n\nReese smashes his hand hard into the pumpkin. Suddenly, a ghost emerges from the crumbling pumpkin. It is holding a huge scythe in its hand and slashes hard at Reese's head...\n")   
        if answer == "2":
            print('\n\nReese takes out a cute little candy from her pocket and slowly puts it into the pumpkin. Just then, a feeling of numbness goes through her body, forcing her slowly lie down on the bed. She is smiling and the dream is begin...\n')

        #Fourth character
        
        answer = input('\n\nJohn...\n\nAs John slowly walks into the dining room... On the dining table is a feast of everything you could ever dream of. Across the table sits a ghost like figure of an old man...John is faced with two choices " run and stay hungry for the remainder of the game (1) or sit and feast with me (2)" Suddenly,the ghost like figure reaches out encouraging John to sit down and feast with him. What will you do?\n')
        while answer not in choices:
            answer = input("Please try again")
        if answer == "1":
            alive.remove("John")
            dead.append("John")
            print("\nJohn screams and runs for his life too terrified to eat with the ghost.\n\nAs he's running, John quickly realizes he made a big  mistake.\n\nThe old ghost flies above him and snatches him up, and drops him into spikes. \n\n")                       
        if answer == "2":
            print("\nJohn decides to sit and feast with the old man. \n\nHe tastes evrything on the table while trying not to look at the old man. \n\nOnce he's done eating he chugs some water and anxiously begins to get up from the table.\n\n")
  
    elif answer == '2':
        alive.append('i')

    
    
    if len(alive) == 5:
        print("\n\nSecret Ending: Everyone agrees to go home, and they all make it safe with their candy. The End.")
        if ending["Secret"] == 0:
            ending["Secret"] += 1
    elif len(alive) == 4:
        print("After surviving the troubles of the House, they all meet up on the front porch of the House. With horrid looks in all their eyes, they vowed to never speak about what happened there. They all pick up the candy where they left, and leave off to their houses, never forgetting on what occurred on Elm Street...\n\n")
        if ending["Best"] == 0:
            ending["Best"] += 1
    elif len(alive) > 0:
        print("With", ', '.join(alive), "still alive, they all gather outside the house, and notices that", ', '.join(dead), "have/has not been seen, or met up with them. Still trembling in fear, they all run home and call the cops. When the cops arrive, there is no bodies to be found. Where did they go....\n\n")
        if ending["Good"] == 0:
            ending["Good"] += 1
    else:
        print("---------------------------")
        print("Four came into the house, none left out. Each person... Sam, John, Tyler, Reese... was consumed by the terrors of the Abandoned House. \n\nAfter all that was said and done, was there another way?....\n\n ")
        if ending["Bad"] == 0:
            ending["Bad"] += 1
            
    values = sum(ending.values())
    if values == 4:
        print("\n\nYou have gotten all the endings in the game! Congratulations on finding every one of them, we hope you had a fun time playing!")
        break
    else:
        ask = input("\n\nYou have gotten "+ str(values) + " of 5 endings, would like you to retry the game? Y/N\n")
        if ask.upper() == 'Y':
            continue
        elif ask.upper() == 'N':
            print("\n\nGAME OVER")
            break
