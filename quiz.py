questions = ("Who was South Africa's first black president?: ",
             "What is the capital city of South Africa?: ",
             "How many official languages does Suid Africa have?: ",
             " What is the name of the highest mountain in Mzansi?: ",
             "In which year did Africa Borwa host the FIFA world cup?: ")

options = (("A. Cyril Ramaphosa ", "B. Thabo Mbeki ", "C. Jacob Zuma ", "D. Nelson Mandela "), 
           ("A. Durban ", "B. Polokwane", "C. Pretoria ", "D. Kimberly"),
           ("A. 1", "B. 11 ", "C. 30", "D. 50"),
           ("A. Magaliesberg", "B. Table Mountain", "C. Drakensburg", "D.Thabana Ntlenyana "),
           ("A. 2010", "B. 1994", "C. 2021", "D. 1985"))

answers = ("D", "C", "B", "B", "A")

guesses = []

score = 0

question_num = 0

for question_num in enumerate(questions):
    print("--------------------")
    print(questions)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
       score += 1
       print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")

    question_num += 1
print("--------------------")
print("       RESULTS      ")
print("--------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

final_score = int(score / len(questions) * 100)
print(f"Your score is: {final_score}%")