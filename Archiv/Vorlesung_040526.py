
#wenn jmd unter 6 jahren, dann kann er/sie umsonst rein
#bis 12 jahre bekommt jmd 50% Rabatt
#Studenten bis 27 Jahre 20% Rabatt
#ab 18 kein Rabatt


age = int(input("How old are you: "))
student_answer = input("Are you a student? [Yes/No]")

is_student = False
if student_answer == "Yes":
    is_student = True
elif student_answer == "No":
    is_student = False

if age < 6:
    print("guest does not have to pay!")
elif age < 12:
    print("guest gets 20% discount")
elif is_student and age < 27 :
    print("student discount")
else: 
    print("no discount")