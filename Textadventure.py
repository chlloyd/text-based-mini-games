firstTurn = True

def survive(a):
    name = a.lower()
    global firstTurn
    if firstTurn == True and name != '/reset':
        firstTurn = False
        return"Welcome to Jurassic Par- Wait thats copyrighted \nWelcome to HackTheMidlands \nYour task is to take part in hack the midlands without angering Tom\n Depending on your choices and options it could mean game over \nto play the game you enter the choice you would like to pick while including any previous choices , so if you pick the third choice after the first you would send 13 just type '/help' for more info \nYour objective should you be bothered is to leave hackthemidlands by learning the door codes \nYou have 3 options to acquire informatin \nYou can take part in the capture the flag with option 1 \nYou can take part in the seminars for option 2\nYou can work on your project for option 3 \nFinally you can try and leave the building with- option 4"
    else:
        if name=="1":
            return"You have decided to take part in the capture the flag and you remember them saying about the awnser being on your lanyard, you have 4 options, 1: you can attemept to brute force you way through the code, 2: you attempt to listen in to other people working on it hoping you hear the awnser , 3: You attempt to work on something from your lanyard , 4: you attempt to intemeditate someone for the password  "

        elif name == "/help":return"The game works by inputing your previous options and your next one for example if you previosuly chose the 3rd option then the 2nd and wish to then choose the 3rd for your current option you should enter 323, if you wish to go back to the previous option just remove the last number and it should bring it back to the previous area"

        elif name=="11":return"Your able to, through your own skils of hacking or maybe you just steal a program off the internet since thats easier, get the password for that challenege sorted , but after a breath of relief as that challenge was so easy , you feel a seperate breath behind you , you turn to see tom, with their  master hacking skills they must have found you brute forcing the website. He is displeased by this infraction and you have been sentenced to the data mines"

        elif name=="12":return"Being a secret slueth and amazing at being stealthy you are able to listen in on some people who give a anwser that comes up correct for the challenge , You return back to your setup and think back maybe they noticed you but thought you was wierd and slightly creepy and didn't want to intervene, You return smuggly and place in the awnser and lean back in your chair as you look up and notice tom staring down at you , he noticed you cheating from another person and is disappointed and you have been sentenced to work the surveilance van for tracking the data from everyone inside hack the midlands"

        elif name=="13":return "as a intelligent indivudal you are able to make your way through the process and determine the clue the badge supplied within the dots its a simple process and succeed with the challenge , a new challenege appears, lunchtime would you like to 1: go when called and listen to the instructions accoridngly , 2: attempt to sneak in early , 3: attempt to run while the doors are open"

        elif name=="14":return"You pull someone aside and threaten to dox them or beat them up if they don't give you the awnser to the challenge, but as soon as you do so , you are lifted up from behind and have been caught by Tom and his bulging muscles , he does not like you bullying other attendees and banishes you to the shadow realm"


        elif name=="131":return "You wait for some time and are summoned to go out for lunch , you try to notice the door codes but are unable to see them enter anything, maybe a different activity will free you"

        elif name=="132":return "As you attempt to sneak into the line for the jabberwocky early , Tom and his all seeing eyes notices your unfairness and proceeds to punish you by forcing you to cook everyones meals , game over"

        elif name=="133":return "You sreturn to leave the building and as you reach the doors, you are stopped by tom and his amazing cardio for dangerous running and are thrown into the time out corner , game over"


        elif name=="2":return "You feel going to the seminars could retreive you some information for the door codes but you have a couple of options \n 1. Enter the seminar early before they start \n 2. Wait for the seminar to start \n 3. Sabotage the seminar \n 4. start a fire "


        elif name == "21":
            return"You sneak into the seminar early and notice a tray of sushi near the entrance as you look at it you feel a presence behind you and see Tom , he looks displeased you have snuck in early and have mere moments to acquire some sushi to please him \n 1. Salmon \n 2. Tuna \n 3.Shrimp \n 4. Banananananana"

        elif name == "22":
            return"You enter the seminar at the correct time and listen through them , you learn a amazing amount of information and appreciate the sponsors but you have not learnt anything about the door codes "

        elif name == "23":
            return"As soon as you think of this idea, you feel a powerful entity behind you , you turn to see Tom, they have sensed your thoughts and has determined you threatened the hackthemidlands , he reaches over and you feel your very essences being changed, you feel productive and stay in hackthemidlands as a volunteer, game over"

        elif name == "24":
            return"As soon as you think of this idea, you feel a powerful entity behind you , you turn to see Tom, they have sensed your thoughts and has determined you threatened the hackthemidlands , he reaches over and you feel your very essences being changed, you feel productive and stay in hackthemidlands as a volunteer, game over"

        elif name == "211":
            return"Tom is displeased of your choice and now must become his personal sushi chef by training in the arts of sushi"

        elif name == "214":
            return"Tom is displeased of your choice and now must become his personal sushi chef by training in the arts of sushi"

        elif name == "213":
            return"Tom is displeased of your choice and now must become his personal sushi chef by training in the arts of sushi"

        elif name == "212":
            return"Tom is pleased by your choice and now must become his personal sushi chef by training in the arts of sushi"


        elif name == "3":
            return"You begin working on your program and feel inspired to copy a game. \n 1.Skyrim \n 2.Tetris \n 3.Mario \n 4.Pokemon"

        elif name=="31":
            return"Suddenely you feel sleepy and your eyes slowly close, suddenly the air is cold and you slowly hearing from the opposite , Hey,you , You're finally awake as you see Tom waking you up as you have slept through all of hackthemidslands , Game Over"

        elif name == "32":
            return"You feel tetris is a great game to copy , after 4 hours of perfect planning and coding , you find Tom in the reflection of your screen , he is not happy with plagarism , He curses you to forever get the wrong tetris piece , Game Over"

        elif name == "33":
            return"You feel Mario is well known but feel if you make them electricians instead it will be fine.after 4 hours of perfect planning and coding , you find Tom in the reflection of your screen , he is not happy with plagarism , he curses you to forver get a static shock everytime you type, Game Over"

        elif name=="34":
            return"Pokemon is a simply process to copy but not wishing to risk copyright decide to name the game digimon , who would name something that bad? after 4 hours of perfect planning and coding , you find Tom in the reflection of your screen , he is happy with the presence of pokemon and leaves you be but you did not learn anything about the door codes."

        elif name=="4":
            return"You walk towards and attempt to pull them open but they do not budge , you see a keypad on the side of a wall but do not know the combination what do you do?"

        elif name=="push":return"You push the door opening forgetting there is no lock as you can leave at anytime and it was a push door you was pulling on"

        elif name=="4push":return"You push the door opening forgetting there is no lock as you can leave at anytime and it was a push door you was pulling on"
        elif name=="/reset":return"/reset"
        else:return"Thats not a option :("


