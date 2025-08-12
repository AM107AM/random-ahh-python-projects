from time import sleep

print("Hello, welcome to the quiz game")
sleep(1.5)
print(
    "First enter the questions and their respective answers then pass the device to your friend"
)
sleep(2)
print("Ready?")
sleep(1)

while True:
    questions = []
    answers = []
    question_num = 0
    score = 0
    question_asked = 1
    while True:
        question = input(
            f"Please put in your question({question_asked}) (p to start playing playing): "
        )

        if question.lower() == "p" or question == "":
            break
        questions.append(question)
        answers.append(
            input(f"Please select the answer to the question({question_asked}): ")
            .lower()
            .strip()
            .replace(" ", "")
        )
        question_asked += 1

    if questions == []:
        print("Oh ...")
        sleep(1)
        print("I guess you don't wanna play then")
        sleep(2)
        print("Goodbye")
        break

    print("And the first question is:...")
    sleep(1)
    for question in questions:
        print(question)
        guess = input("your answer is: ").lower().strip().replace(" ", "")
        if guess == answers[question_num]:
            print("correct answer")
            question_num += 1
            score += 1
            sleep(2)
            print("OK, next question")
            sleep(2)
        else:
            print("Incorrect answer")
            print(f"the correct answer is: {answers[question_num]}")
            question_num += 1
            sleep(2)
            print("OK, next question")
            sleep(2)
    print("Wait ...")
    sleep(2)
    print("It seems that's all the questions for now")
    score_percent = score / question_num * 100
    print(f"The score you got is:{score_percent:.2f}%")
    play_again = input("Play again? (Yes or No): ").lower().strip().replace(" ", "")
    while True:
        if play_again not in {"yes", "no"}:
            play_again = input(("please select either (Yes or No)"))
        else:
            break

    if play_again == "no":
        print("Well, have a good day")
        sleep(3)
        break
