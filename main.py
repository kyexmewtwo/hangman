import time
print("Welcome to hangman.")
time.sleep(1)
print("This is a two player plus game.")
time.sleep(1)
yes_or_no= input("Do you have a friend with you? (y/n)")
if yes_or_no == "y":
  print("Okay, decide which one of you will make the word.")
  time.sleep(3)
  y_or_n = input ("Made up your mind? (y/n)")
  if y_or_n == "y":
    word = input ("Tell your friend to look away as you type in the word they are trying to guess.")
    topic = input("Tell us a hint for the word.")
  elif y_or_n == "n":
    word = input ("Pathetic. Tell your friend to look away as you type in the word they are trying to guess.")
    topic = input("Tell us a hint for the word.")
  else:
    print("...")
elif yes_or_no == "n":
  print("Find one, and start this code over.")
else:
  print("This is a college class how can you not read. Start the code over and enter either y or n to the input.")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
no_spaces = word.replace(" ", "")
def split(no_spaces):
    return [char for char in word]  
word = split(no_spaces)
letter_count = len(no_spaces)
turns = 10
time.sleep(2)
print("You can tell your friend to look back now.\n")
time.sleep(4)
print("Friend who is trying to guess. You have 10 guesses.\n")
time.sleep(1.5)
print("If you get a letter correct, you don't lose the guess.\n")
time.sleep(1.5)
print("However if you don't, you will lose one guess.\n")
time.sleep(1.5)
print("Guess a single letter. \n The topic is " + topic + ". The word is " + str(letter_count) + " letters long.\n Spaces count as letters.")
guesses = ''
turns = 10
while turns > 0:
  failed = 0
  for char in word:
    if char in guesses:
      print (char,)
    else:
      print ("_", )
      failed += 1
  if failed == 0:
    print ("You won")
    break
  guess = input("guess a character:")
  guesses += guess
  if guess not in word:
    turns -= 1
    print ("Wrong")
    print ("You have", + turns, 'more guesses' )
    if turns == 0:
      print ("You Lose")