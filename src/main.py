# test
# additional print function below to give more space, making the console easier to read.
print()

#Original code of mine
# print("You arrive in a room that is dark with barely any light. You notice that there are four walls surrounding you; behind, front, left and right.\nYou do not immediately feel claustrophobic, however you begin to feel uneasy due to the dark.", end=" ")
# print("In front of you, there are three items.")
# print("1. A dagger to your left, 2. a small triangular bottle with what appears to be red liquid in front, and 3. iron boots to the right.")
#end of original code of mine.

#start of broky's improved f string print function
print(f"You arrive in a room that is dark with barely any light. You notice that there are four walls surrounding you; "
      f"behind, front, left and right.\nYou do not immediately feel claustrophobic, however you begin to feel uneasy due to the dark. "
      f"In front of you, there are three items: \n"
      f"1. A dagger to your left. \n2. A small triangular bottle with what appears to be red liquid in front\n3. iron boots to the right.")

user_choice = int(input("Which item would you like to investigate further? (choices: 1, 2 or 3): "))

#Original code, without Broky's help below.
# item1 = 1
# item2 = 2
# item3 = 3

# if not (user_choice == item1 or user_choice == item2 or user_choice == item3):
#     print(f"I'm pretty sure that's not what was asked. Perhaps try answering the question?")
# elif item1:
#     print(f"You inspect the {item1} and find it to be dull with rust beginning to settle on the blade. ")
# elif item2:
#     print(f"You pick up the {item2} and swish the bottle around. Upon closer inspection, you can't tell if the color of the liquid is due to the bottle, or is it naturally red.")
# elif item3:
#     print(f"You pick up the {item3} and inspect them closer. You're sure that you can fit these boots if you tried them on. They may be a bit loose, but that's better than walking bare-footed.")
# End of original code
# 
# Broky's code below.

items = ["dagger", "bottle", "iron boots"]

while True:
  if user_choice not in [1,2,3]:
      print(f"I'm pretty sure that's not what was asked. Perhaps try answering the question?")
  if user_choice == 1:
      print(f"You inspect the {items[0]} and find it to be dull with rust beginning to settle on the blade. ")
  elif user_choice == 2:
      print(f"You pick up the {items[1]} and swish the bottle around. Upon closer inspection, you can't tell if the color of the liquid is due to the bottle, or is it naturally red.")
  elif user_choice == 3:
      print(f"You pick up the {items[2]} and inspect them closer. You're sure that you can fit these boots if you tried them on. They may be a bit loose, but that's better than walking bare-footed.")
  break 

print("\n")
# print()

# Broky's code below is a LIST COMPREHENSION
#def choices(number: int):
#  return [i for i in range(1, number + 1)]

#if __name__ == "__main__":
#   print(choices(5))

#mychoices = choices(10)
#print(mychoices)

# end of Broky's code for List Comprehension