import random
random_set=set()
number_set=set()
guesses=set()
#the purpose
print("welcome to my lottery game")
print("I have chosen 6 random numbers between 1 and 59")
print("Will you able to guess all the 6?")
print("Would you like to play with random generated numbers, or would you like to guess the numbers?")
random_q=input("Enter yes if you choose to play with random numbers:").lower()
if random_q=="yes":
  random_set=set()
  while len(random_set)<=5:
    r_number=random.randint(1, 59)
    if r_number not in random_set:
      random_set.add(r_number)
  print("Your numbers are: ", random_set)    
  number_set=set()
  while len(number_set)<=5:
    number=random.randint(1, 59)
    if number not in number_set:
      number_set.add(number)
  print("The winning numbers are:", number_set)


else:  

#build a list of six numbers between 1 and 59
  guesses=set()
  while len(guesses)<=5:
    guess=int(input("please enter a number:"))
    if guess<1 or guess>59:
      print("Your numbers should be between 1 and 59, please enter another number!")

    elif guess in guesses:
      guess=int(input("Your numbers should not repeat, please enter another number:"))
    else:
      guesses.add(guess)

  print("Your numbers are:", guesses)

  print("Let's see the winning numbers!")

#build a random list of 6 numbers 1-59 without repeating
  number_set=set()
  while len(number_set)<=5:
    number=random.randint(1, 59)
    if number not in number_set:
      number_set.add(number)

  print("The winning numbers are:", number_set)

# find the intersection of the two lists
matches=list(set(guesses) & set(number_set)) or list(set(random_set) & set(number_set))
print("The matches are:", matches)    
if len(matches)==0:
  print("You have no matches. Next time maybe you will have more luck!")
else:  
  print("Congrats! You have", len(matches), "match(es)")

