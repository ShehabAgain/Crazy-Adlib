

name=input("what is the name of your character? ")
age=int(input("pick a number between 2 and 13 " ))
while age < 2 or age> 13:
  print("error, Try again")
  age=int(input("pick a number between 2 and 13 "))
act1= input("pick an extraordinary achievement ")
job=input("pick a dream job ")
age2=int(input("pick a number between 18 and 35 "))
while age2 <18 or age> 35:
  print("error, Try again")
  age2=int(input("pick a number between 2 and 13 "))
item=input("pick a fancy item ")
city=input("pick a random city ")
food=input("pick your favorite food ")
sport_team=input("Pick your favorite sports team ")


print(" ")
print("Ok.. Here goes nothing:")
print("")
  
print("Let's talk about the legend of {0}. At the age of just {1}, {0} was capable of {2}! He was such a good {3} by the time he was {4}, that he was able to invent the {5}! I will never forget what {6} meant to {7}. He even liked to eat {8} and watch the {9} play!".format(name,str(age),act1,job,str(age2),item,name,city,food,sport_team))