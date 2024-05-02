print ("Hi! Welcome to my Artificial Intelligence quiz")

First_Name= input("Enter your first name ") 

Playing= input ("Do you want to play? ")

if Playing.lower() == "yes" :
    print ("Great! " + First_Name + ", " + "let's play :) ")

else:
    quit()

score=0

Question1= input("What does AI stand for? ")
if Question1.lower() == "artificial intelligence" :
    print ("Correct!")
    score+=1

else:
   print ("Incorrect!")


Question2= input("What does ML stand for? ")
if Question2.lower() == "machine learning" :
   print ("Correct!")
   score+=1

else:
   print ("Incorrect!")


Question3= input("Is social media a real life AI application? ")
if Question3.lower() == "yes" :
    print ("Correct!")
    score+=1

else:
   print ("Incorrect!")


print ( "Are the following statements true or false" )

Question4= input("Machine learning uses artificial neural networks to solve complex problems.  ")
if Question4.lower() == "false" :
    print ("Correct!")
    score+=2


else:
   print ("Incorrect!")


Question5= input("Python, c++ and java are AI languages. ")
if Question5.lower() == "true" :
    print ("Correct!")
    score+=2


else:
   print ("Incorrect!")


Question6= input("Deep learning is processing data, learning from it and making informed decisions. ")
if Question6.lower() == "false" :
    print ("Correct!")
    score+=2


else:
    print ("Incorrect!")


Question7= input("Transorflow is an AI development platform ")
if Question7.lower() == "true" :
 print ("Correct!")
 score+=2


else:
   print ("Incorrect!")


Question8= input("Agent and Reward are not necessary in Markov's decision process ")
if Question8.lower() == "false" :
 print ("Correct!")
 score+=2


else:
   print ("Incorrect!")


Question9= input("Mention one type of machine learning ")
if Question9.lower() == "supervised learning":
   if Question9.lower() == "unsupervised learning":
    if Question9.lower() == "Reinforcement learning":
     print ("correct!")
     score+=2

else:
   print ("Incorrect!")


if score> 7:
    print ("well done " + First_Name + ", " + "you got " + str(score) + " questions correct" )

else:
    print ("Oopsie :( " + First_Name + ", " + "you got " + str(score) + " questions correct, better luck next time" )

print ("you got " + str((score/15)*100) + "%")







   




    



 
 
   
 
