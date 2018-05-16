# By: Morgan Hurley 5/9/18
answer1 = input("Would you like to complete story 1, 2, 3 or 4? ")
if (answer1 == "1"):
    noun1 = input("enter a noun: ")
    profession1 = input("name a profession: ")
    noun2 = input("enter a noun: ")
    noun3 = input("enter another noun: ")
    noun4 = input("enter another noun: ")
    noun5 = input("enter another noun: ")
    bodypart1 = input("enter a body part: ")
    animal1 = input("enter a type of animal: ")
    bodypart2 = input("enter another body part: ")
    noun6 = input("enter a plural noun: ")

    print ("Madame Consuela had a dilemma! She couldn't seem to find her prized " + noun1 + " to wear around her neck for the Opera this evening. She had the " + profession1 + " check everywhere in her mansion for it, and when the " + profession1 + " came up with nothing, she began to search for it alone. She checked the " + noun2 + " and it's gone, the " + noun3 + " and the " + noun4 + " and she even checked the " + noun5 + "! Yet the " + noun1 + " was nowhere to be found! She had just given up when she noticed something poking her " + bodypart1 + ". When she looked down, there was her favorite " + animal1 + ", the " + noun1 + " around its " + bodypart2 + "! Madame Consuela couldn't bring herself to take the " + noun1 + " from the " + animal1 + ", and decided she had plenty of " + noun6 + " to wear anyways."    ) 

elif (answer1 == "2"):
    noun1 = input("enter a noun: ")
    verb1 = input("enter a verb: ")
    noun2 = input("enter another noun: ")
    place1 = input("enter a place: ")
    noun3 = input("enter a plural noun: ")
    place2 = input("enter another place: ")
    time1 = input("enter a time of day: ")
    activity1 = input("enter a type of activity: ")
    noun4 = input("enter another plural noun: ")
    time2 = input("enter an amount of time: ")
    place3 = input("enter another place: ")

    print ("Josephine hardly had time to complete her homework yesterday. When she first sat down to do her work, her " + noun1 + " needed her to " + verb1 + " the " + noun2 + ". Once she had finally finished, it was time to take her sister to " + place1 + ". On her way home, her " + noun1 + "  asked her to pick up some " + noun3 + " from the " + place2 + ". By the time Josephine finally got home, it was " + time1 + ", leaving hardly any time before " + activity1 + ". Josephine hurried and got out her " + noun4 + " and set to work, luckily she was able to complete her homework in " + time2 + ". When Josephine got to " + place3 + " the next morning, she was glad to have taken the time to complete her work.")
  
elif (answer1 == "3"):
    noun1 = input("enter a noun: ")
    place1 = input("enter a place: ")
    verb1 = input("enter a past tense verb: ")
    noun2 = input("enter a noun: ")
    noun3 = input("enter a plural noun: ")
    noun4 = input("enter another plural noun: ")
    noun5 = input("enter a plural noun: ")
    noun6 = input("enter a singular noun: ")
    noun7 = input("enter a plural noun: ")
    yes1 = input("yes or no? ")

    print ("Addie had decided to take her " + noun1 + " to the " + place1 + ". She, however, immediately knew that this was a bad decision since her "  + noun1 + " would be intent on taking a pet home. To Addie’s amazement, as they " + verb1 + " by the " + noun2 + " section, her " + noun1 + " did not ask to take one home. The day progressed and her "  + noun1 + " had still not said anything. They had passed the " + noun3 + ", the " + noun4 + ", and even the " + noun5 + ". Addie was beginning to think that something was wrong, but right as they were about to leave and get into the " + noun6 + ", her " + noun1 + " asked to see the " + noun7 + ". Relieved that her " + noun1 + " had come back to their senses she, of course said " + yes1 + " when they asked to take one home." )   
    
elif (answer1 == "4"):
    verb3 = input("enter a past tense verb: ")
    place1 = input("enter a place: ")
    verb1 = input("enter a past tense verb: ")
    place2 = input("enter another place: ")
    profession1 = input("enter a profession: ")
    verb2 = input("enter a present tense verb: ")
    noun1 = input("enter a noun: ")
    noun2 = input("enter another noun: ")

    print ("Lauren was an artist with no muse. Desperate to find one, she traveled the world. She " + verb3 + " in " + place1 + " she " + verb1 + " in autralia, and lived with a buddhist monk in " + place2 + ". But still no muse. Frustrated, she decided to go home and change her profession to a " + profession1 + ". Just as she was " + verb2 + " on the " + noun1 +  " to get home, she saw it. The perfect muse! A " + noun2 + ".")   
    
    
    
else:
    print ("That is not a valid response please enter from 1 to 4. ")


