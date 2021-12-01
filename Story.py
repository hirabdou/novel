print("Welcome to Abandoned House! This is a choice-based story about how four teenagers go in an abandoned house on Halloween, and mysterious things occur.")
print("Directions:\nTo pick a choice, enter the number that is in parentheses next to the choice. There will be two different choices for ALL inputs. Example: If the story tells you 'Left (1) or Right (2)?', you would enter '1' to go left, and vice versa.\n\n")
alive = ['Tyler', 'Sam', 'Reese', 'John']

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
