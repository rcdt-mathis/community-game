#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#intro
print("""\N{BEAMED EIGHTH NOTES} Gimme some rope
Tie me to dream
Gimme the hope
to run outta steam \N{BEAMED EIGHTH NOTES}
""")
print("Welcome! It's time to choose your own Community adventure.") 

print('How old are you?')
age = input()
print("""

The year is 2009. You've just been fired from your job waiting tables at The Greasy Fork. 
You spent the last of your money on Serbian rum and a bag of Let's Potato Chips, because your mom wouldn't make you any buttered noodles. 
Judge Judy is on. You don't think she'd take your side. 
You're starting to feel really sorry for yourself, when a Greendale Community College commercial comes on the TV. 
It's a super cheesy commercial that would have been outdated 10 years ago, but it gets you thinking.

You gotta do something with your life, right? After all, you're""",age, 'years old.')
stillplaying = True
while stillplaying:
    response = input("""Press 1 to enroll in community college so you can learn. And think. And get a student loan. And grind your own coffee. And understand HBO. 
Rress 2 start looking for a job tomorrow.""")
    if response == '2':
        print ('Well, you get fired again and your mom kicks you out. Now you live in a van down by the river. you maybe wanna try that again?')
        response =input('Press 1 to try again, or press 2 to accept your fate.')
        if response == '2':
            print("Fine. Bye.")
            stillplaying = False
    else: 
        print ('Good choice! I think.')
        print("""So far, you are enjoying Greendale Community College. Or something like that. You joined a Spanish study group and you've made several new friends. 
Everything seems to be going fine until...

        
\N{CROSSED SWORDS} Some really mean teenagers make fun of you for being""", age, """years old and going to community college. \N{CROSSED SWORDS}
        
        Plus they laugh at your friend's Discman
        """)
        response = input("""Press 1 to decide that a grown adult should not be engaging in petty conflict with teenagers and ignore them until they go away.
        Press 2 to give into your insecurities and pwn these loser children.""")
        if response == '1':
            print ("""I guess you forgot how persistently obnoxious teenagers can be. 
            Thanks to your pride, you and all your friends are driven to insanity. 
            You've been institutionalized. 
            
            Want to try again?""")
            response =input('Press 1 to try again, or press 2 to accept your fate.')
            if response == '2':
                print("Fine. Bye.")
                stillplaying = False
                break
            else: 
                stillplaying=True
                continue
        else:
            print("Uhhh, good job, I guess. You totally pwned those children.")
            print("""
--------------------------

Anyway, some time passes, and now it's Halloween! \N{JACK-O-LANTERN}
The dean throws a party. You go, because you're a """, age, """year-old community college student, so what else do you have to do? 

The playlist is a lot of ABBA, the food is kinda questionable, and the vibe is a little weird. Pretty much your typical Greendale party, until a couple people start getting really sick.
It turns out that the dean bought a lot of real sketchy taco meat from an army surplus store.
You didn't eat any of that, did you?""")
            response = input('Press 1 for no, press 2 for yes')
            if response == '2':
                print("Wow, you're really not that smart, are you?")
            else:
                print("""Oh thank goodness. Things are looking pretty bad, though. People are turning into actual zombies. Like, literally biting each other. Wtf. 
            

You and the other uninfected decide to lock yourselves in a room where the zombies can't get you. 
But it turns out that a couple people lied about being bitten. They really thought they were special somehow.""")
            print("""
      
Now the whole school has been turned into zombies, including you.
                        
But wait... The air conditioner starts blowing freezing cold air, lowering everyone's body temperature. Your symptoms start to subside, and you begin to shiver. 
            
By the time the army arrives, there's nothing left for them to do besides wipe all your memories... Thankfully.
""")
            print("""You and all your friends think it's weird that nobody remembers anything from the night of the Halloween party, but that's probably for the best (I heard a rumor that Shirley hooked up with Chang).

-------------------------------

In your third season... I mean year... at Greendale, your friends Troy and Abed get an apartment together. The whole group comes over for a housewarming party. Y'all decide to order a pizza.

When the pizza arrives, Jeff suggests rolling a die to see who should go get it. Starting from his left with 1, if your number comes up, you go get the pizza. 
Abed: 'Just so you know, Jeff, you are now creating six different timelines.'
Jeff: 'Of course I am, Abed.

Jeff throws the die.

""")
            response=input('Type STOP to catch the die before it lands or press a number between 1 and 6 to see what he rolled.')
            try:
                int_value = int(response)
                if int_value in range(7):
                    print("""Troy sighs and runs to get the pizza, slamming the door on his way out.
The force of the door slamming causes a boulder to fall off Abed's Indiana Jones diorama. Shirley leaves the table to check on her pies in the kitchen. 
Jeff stops Britta from singing Roxanne, and she goes to the bathroom to light up a joint. 
Pierce asks Jeff about his father, causing Jeff to get up from the table to get a drink. Jeff hits his head on the ceiling fan, and Annie offers to take a look at his injury in the bathroom. 
On the way there, Annie trips on the still rolling boulder and falls onto the coffee table.
Pierce's bottle of Serbian rum, which was resting on top of it, goes flying. It crashes, spilling rum all over the floor. 
After seeing Annie's fall, Pierce quickly stands up to offer assistance and kicks his rude housewarming present, the Norwegian troll doll, across the floor. 
Annie's purse lands on the ground, and the jolt causes the gun inside to discharge and shoot Pierce in the leg. 
Britta hears the commotion and stumbles out of the bathroom, dropping the joint she was smoking onto the floor. 
The joint lands in the puddle of Serbian rum, igniting it and causing a fire to break out. 
Annie tries to help Pierce as blood sprays out of his wound.
The blood covers Shirley, who had just exited the kitchen with her finished pies. 
Jeff tries to put out the fire while Britta runs to the kitchen to get water to help him. 
Troy returns with the pizzas. 
Shocked at the scene in front of him, he notices the Norwegian Troll staring at him, surrounded by flames and the remnants of its burnt box. 

Pierce later dies from his leg wound. 
Annie is institutionalized due to her guilt.
Jeff lost an arm after trying to put out the fire.
Troy damaged his larynx trying to destroy the Norwegian troll by eating it while it was on fire. If you think that's stupid, you don't know anything about trolls.
Shirley has become an alcoholic.
Also Britta got a blue streak in her hair. 


This is the darkest timeline.
Abed suggests committing to being evil now. He makes you a fake goatee to wear until you can grow your own.

""")
                    response =input('Press 1 to start over, or press 2 to accept your fate.')
                    if response == '2':
                        print("Okay, have fun being evil!")
                        stillplaying = False
                        break
                    else: 
                        stillplaying=True
                        continue
            except ValueError:
                   print("""Ok, well, timelines are probably stupid, but it's best not to let Jeff get away with trickery. 
Turned out to be a pretty good party. 

---------------------

In the fourth year of your two-year degree, you mention how excited you are that it's been one year since the first time you watched Freaky Friday with your best friend, Abed. 
Somebody points out that you and Britta have been dating for one year. You both kinda forgot, but now you're feeling a lot of pressure to celebrate. 

You find yourself torn between prioritizing your somewhat lackluster relationship and having a fun body-switching adventure with your best friend Abed.


""")
            
            response = input('Press 1 to prioritize your relationship or press 2 to switch bodies with Abed for just one day.')
            if response == '1':
                print("""You have lunch with Britta for your anniversary. The meal would be completely forgettable if not for the feeling that you squandered a perfect opportunity to end this stagnant relationship.
You do love Britta, but platonically, and you don't want to hurt her feelings or ruin the friendship, but now you're stuck. You're stuck, and you're dead inside. 

You'd do anything to escape. Except, you know, tell Britta you don't want to date her anymore.

So you allow yourself to be recruited into Greendale's secretive and weirdly sinister air conditioning repair school. 

You pack up and move out of your apartment, never to be seen again. 

You'll miss your friends and family, but at least you didn't have to have an awkward conversation.

""")
                response =input('Press 1 to start over, or press 2 to become the Truest Repairman and never be seen again.')
                if response == '2':
                    print("Okay, have fun fixing air conditioners!")
                    stillplaying = False
                    break
                else: 
                    continue       
            else: 
                print("""You and Abed grasp your Director's Cut of Freaky Friday DVD and say in unison, I wish I could trade places with you for just one day!
The camera pans in circles around you, and a janitor chooses that moment to perform a routine light switch check. 
At first you think nothing happened, but you wake up in the morning as Abed. Or pretend to, or whatever.

Jeff, annoyed by this, demands that you switch back. Unfortunately the DVD has been misplaced. He drags you along to find it. 

Meanwhile, Abed (as you) goes to lunch with Britta and does your dirty work for you. It actually works out well. You and Britta remain friends. 

Life goes on.


--------------

It was a dark and stormy day sometime during your fifth year, when the whole campus erupted in a panicked frenzy. 

The lurking weirdo known only as the Ass Crack Bandit has returned to Greendale, dropping quarters down the ass cracks of unsuspecting victims.

For some reason, it's up to you to find out who the Ass Crack Bandit is.
So far all you know is that he hates money or loves it or doesn't care about money and hates butts or loves them. And he likes Dave Matthews Band.

Honestly, you're not that invested. It could be anyone. But there are a couple of suspects that stand out to you. Let's blame one of them and call it a day.

1. Star-Burns, the weirdo who staged a meth lab explosion and faked his death, but whom you discovered living in the school's stables and working on some ridiculous invention.
2. Annie, who has been known to contrive any possible excuse to team up with Jeff on some cutesy caper.
""")
                response = input('Press 1 to blame it on Star-Burns or press 2 to accuse Annie')
                if response == '2':
                    print("""You accused Annie of being the Ass Crack Bandit, but you really didn't have any evidence. And honestly, she's not even old enough to like Dave Matthews like that. 
                    So now you just look like a jealous creep. 
When you show up to study Spanish with the group, they ask you to leave and you make a scene. It's super embarrassing.""")
                    response = input('Press 1 to start over or press 2 to change your name and move away forever.')
                    if response == '2':
                        print('Ok, bye creep.')
                        stillplaying=False
                        break
                    else: 
                        continue  
                else:
                    print("""Well, you weren't able to save Troy from getting cracked. 
                    
                    Or Vicky. 
                    
                    Or Professor Duncan. 

                    
So it probably wasn't Star-Burns. But the Bandit eventually fades back into the background, and life goes on.

-------

You're THIS CLOSE to graduating, but there's one more crisis to deal with. 
Greendale's rival institution, City College, is running an attack ad that may ruin Greendale for good.
The ad says that Ruffles, who is a dog, received a college degree from Greendale. The implication, if you're slow, is that Greendale's standards are so low that a degree from there is useless.

What are you going to do to save Greendale?

Press 1 to run a commercial acknowledging that a dog was once enrolled at Greendale, explaining that Greendale really needs to get its shit together. Coin a new slogan: "You're already accepted."
or
Press 2 to run an attack ad against the dog, citing her multiple litters of puppies with different fathers. Accuse her of killing squirrels.
""")
                    response = input()
                    if response == '2':
                        print("""Wow. That was really petty. Maybe you shouldn't make important business decisions late at night. 
Now everyone hates Greendale. Annie was so ashamed that she transferred to City College. You're definitely not getting renewed for another season. 
Everyone is sad.  

The end.

""")
                        stillplaying=False
                    else:
                        print("""Yay! You saved Greendale! 
                        Now everyone is happy. 
                        Next stop, graduation! 
                        Or... IDK, maybe change your major and start over.


----------------------------


\N{BEAMED EIGHTH NOTES} \N{BEAMED EIGHTH NOTES}\N{BEAMED EIGHTH NOTES}
donde
esta
la biblioteca
me llamo t-bone
la araña discoteca...
\N{BEAMED EIGHTH NOTES} \N{BEAMED EIGHTH NOTES}\N{BEAMED EIGHTH NOTES}


Thanks for playing. :)""")
                        stillplaying=False
                        

