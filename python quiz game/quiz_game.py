print("Welcome to your one piece quiz")

playing = input("Do u want to play? ")

if playing.upper()!= "YES":
   quit()

print("Okay! Let's play ^_^ ")

score=0

answer = input("1. What is the name of the Straw hats firt ship? ")
if answer.upper()== "GOING MERRY":
   print("correct answer")
   score+=1
else:
   print("LOL!NOOB")

answer = input("2. Who is Luffy's first crewmate? ")
if answer.upper()== "RORONOA ZORO":
   print("correct answer")
   score+=1
else:
   print("LOL!NOOB")

answer = input("3. Who is the cook in the straw hats crew? ")
if answer.upper()== "VINSMOKE SANJI":
   print("correct answer")
   score+=1
else:
   print("LOL!NOOB")

answer = input("4. Who is the navigator of the straw hats crew? ")
if answer.upper()== "NAMI":
   print("correct answer")
   score+=1
else:
   print("LOL!NOOB")

answer = input("5. What is Usopp's role in the straw hat crew? ")
if answer.upper()== "SNIPER":
   print("correct answer")
   score+=1
else:
   print("LOL!NOOB")


if score>=3:
   print(" Congratulations!! You got " +str(score)+ " questions correct!!")
   print( "You scored " +str((score/5) *100) +"%.")
else:
   print(" Seriously?? You just got " +str(score)+ " questions correct!!")
   print( "You  scored " +str((score/5) *100) +"%.")
   print("Please jump off a Building you useless piece of trash ^_^")
