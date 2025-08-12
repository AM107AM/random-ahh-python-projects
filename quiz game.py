from time import sleep

while True:
    questions = []
    answers = []
    question_num = 0
    score = 0
    question_asked = 1
    while True:
        questions.append(
            input(
                f"Please put in your question({question_asked}) (p to start playing playing): "
            )
        )
        if "p" in questions:
            questions.remove("p")
            break
        if "P" in questions:
            questions.remove("P")
            break
        answers.append(
            input(f"Please select the answer to the question({question_asked}): ")
            .lower()
            .strip()
            .replace(" ", "")
        )
        question_asked += 1

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
    if play_again == "no":
        break
