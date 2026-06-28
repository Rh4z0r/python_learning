print("Hello User!")
namenseingabe = input("What is your name? ")
name = namenseingabe
age = int(input("How old are you? "))
voting_age = 18

if age < voting_age:
    print("Sorry (name), you are not old enough to vote yet.")
elif age == 18:
    print("Congratulations (name), it is your first year of being able to vote!")
else:
    print("Hello (name), you are old enough to vote.")