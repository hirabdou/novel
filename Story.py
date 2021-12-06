print("Welcome to Abandoned House! This is a choice-based story about how four teenagers go in an abandoned house on Halloween, and mysterious things occur.")
print("Directions:\nTo pick a choice, enter the number that is in parentheses next to the choice. There will be two different choices for ALL inputs. Example: If the story tells you 'Left (1) or Right (2)?', you would enter '1' to go left, and vice versa.\n\n")
alive = ['Tyler', 'Sam', 'Reese', 'John']
Sam_key=0

while True:    
    answer = input('After a long night, Tyler, Reese, Samantha and John finally get enough candy to go back home. During their walk, they noticed an abandoned house. "We should go in, see if there is anything interesting to take." John declares. "That is too creepy, what if someone is in there waiting for someone like us to go in?" Samantha warned. The group is indecisive on whether they should go to the house or not.\nPress (1) to go to the abandoned house..\n')
    if answer == '1':
        print('Walking up the eerie steps to the door, the anxious group makes their way into the house.\n\nAs they walk in, the glooming lights flicker a little as they walk on the creaking floorboards. All of them in unison ask, "Do you hear that?", as they all point to different areas of the house. Each person in the group walks toward the sound, but it is coming from different rooms for each of them.\nWill they make it out alive?\n')
        #First character
        answer = input('\n\nTyler...\n\nAs Tyler makes his way to the kitchen, he catches a glimpse of a gloomy shadow passing the entrance. In the kitchen, he notices a note on the wall. It reads.. "Will you run (1) or will you hide (2)?" Suddenly, there is loud screeching heading towards you. What will you do?\n')
        if answer == "1":
            alive.remove("Tyler")
            print("\nTyler runs for his life, as he burst through the back door of the kitchen to the outside!\n\n Tyler hears the sounds getting closer and closer. Too worried about the noise, he was not looking ahead and trips on a branch...\n\n The noise stops. SHIINNNG\n Tyler is stabbed through the chest with a metal sword!\n")
        if answer == "2":
            print("\nTyler looks for the first place to hide... the closet!!\n\n He dashes to the closet and closes the door rapidly. He holds his breath in as the sounds slowly start to get louder. \n\nThere is a brief silence, and the sound of a sword starts again, but slowly starts to fade away.\n\n")
        
                       

    break

        #Second character
        answer=input('\n\nSam...\n\n Sam walks towards the basement in a distracted manner. Since the basement was very dark, Sam could only rely on the faint light of his cell phone to walk down the stairs." clomp" " clomp " " clomp..." When he reached the bottom of the stairs, a light illuminated his eyes, and he took a closer look, "Hey! I found a treasure box!!!" He shouted.\nHe cautiously walked towards the treasure box. It was a box made of gold. Strangely, in this dark basement, this golden box glowed with an extremely shining light. What will you do? (Will Sam ignore the box and continue explore (1) OR Open the golden box (2)?)')
        if answer == '1':
            print('\n\nSam is keep walking foward...')
        if answer =='2':
            answer=input('\n\nSam opens the box and there is a golden key inside. Sam picks up the key, and all of a sudden, dozens of small spiders crawl out from the box. What will you do? (Will you stomp them to death (1) OR Run away (2)?')
            if answer =='1':
                alive.remove("Sam")
                print('\n\nMore little spiders crawl out from under the box and devour you. You are death!')
            if answer == '2':
                        Sam_key=Sam_key+4
                        print('\n\nSam turns around and run frantically toward the stairs. At this point, Sam finds the basement door is locked, Sam kicks the door hard, but unfortunately the door is too strong. Just when Sam is desperate, he finds that the basement becomes very quiet. So, Sam walked down the stairs in fear. Sam finds that the boxes and spiders have disappeared, so Sam turn on his cell phone flashlight and keep moving forward. ')

        #Part two
        answer=input('\n\n\nSam looks around the basement. With the light of his phone, Sam notices a huge cross being hung on the wall. There is a black coffin under the cross. Sam walks over to it. What will you do? (Open the coffin (1) OR Ignore it?')
        if answer =='1':
             answer = input('\n\nSam find a human skeleton. The human skeleton is holding a green gemstone tightly in its hand. What will you do? (Take the gemstone away (1) OR Ignore the gemstone and continue your adventure (2)?)')
             if answer == '1':
                 print('\n\nSam forcibly breaks the hand of skeleton and picks up the gem. At that moment, Sam feels a strong force, which makes Sam faint. After waking up Sam finds himself outside the house, but the jewel in his hand has disappeared. You have escaped!')
                 break
             if answer == '2':
                 print('\n\nSam is keep walking foward...')
        if answer =='2':
             print('\n\nSam is keep walking foward...')

        #Part Three
        answer=input('\n\n\nSam continue his adventure. At this point, Sam find a dusty bookshelf. There are many books on the shelf. What will you do? (Pick up a random book from the bookshelf (1) OR continue his adventure (2)?)')
        if answer =='1':
            print('\n\nSam pick up a book...')
        if answer =='2':
            answer=input('\n\n Select your action: Open Golden box(1) OR Coffin(2) OR Bookshelf(3)')
            if answer =='1':
                alive.remove("Sam")
                print('\n\n Sam walks back to the Golden box. After a few seconds hestitate, he opens the box. Countless spiders crawl out from under the box and devour Sam. You are death!')
            if answer == '2':
                alive.remove("Sam")
                print('\n\n Sam opens the coffin, and he finds a skeleton inside. He looks at this skeleton carefully. Suddenly, the skeleton clutch Sam and pulls him into the coffin. And the coffin magically closed itself.')
            if answer == '3':
                print('\n\nSam pick up a book...')

          #Part Four      
        answer = input('\n\n\n Suddenly, a violent vibration comes from under his feet. The floor Sam were stepping on with both feet suddenly opened and Sam fell. Sam get up from the ground. Fortunately, Sam are not injured. Sam look around and see a ritual platform is placed in the middle of the room. There is a large chalice on the ritual platform, but other than that there is nothing else in the room. Sam walk over to the ritual platform, and Sam notice that there a key-shaped groove carved out of the base of the chalice. What will you do? (Put the key into the groove (1) OR Take up the chalice (2)?)')
        if answer == '1':
              if Sam_key==4:
                  print('The stone walls on the left opens up an exit, which Sam find is a stone stairway. Sam walk over to try to find out the end of the passage and see a beautiful starry sky. Sam know this is the way to outside, so Sam walk up the stair…')
                  break
              else:  
                  print('\n\n Sorry, you don''t have this item, please select another option.')
                  answer = input( '\n\n What will you do? (Take up the chalice (2)?)')
                  if answer == '2':
                      alive.remove("Sam")
                      print('Countless small spiders crawl up from the ground, Sam run away in fear, however, Sam find that he have no way to escape, and finally Sam are swallowed by the spider swarm.')

    
