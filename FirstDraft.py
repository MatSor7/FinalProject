import random

# Define the questions and answers
questions_answers = {
    "In what country did the first Starbucks open outside of North America?": "Japan",
    "In a website browser address bar, what does “www” stand for?": "World Wide Web",
    "Who was the first televised President?": ["Franklin D. Roosevelt", "Roosevelt"],
    "Who painted the Mona Lisa?": "Leonardo Da Vinci",
    "Who was the first woman to win a Nobel Prize?": "Marie Curie",
    "What does SPF in sunscreen stand for?": "Sun Protection Factor",
    "In what year was the internet opened to the public?": "1933",
    "When did Facebook first launch?": "2004",
    "Who won the 2010 World Cup?": "Spain",
    "Who provided the voice of Groot in the Guardians of the Galaxy movies?": "Vin Diesel",
    "In which city is Studio 54 located?": "New York",
    "How many Harry Potter books are there?": "7",
    "What day is known as Star Wars Day?": "May 4th",
    "What singer holds the most Grammy nominations?": "Beyonce",
    "How many years have passed between the release of Avatar and its sequel, Avatar: The Way of Water?": "13",
    "Which country has won the most medals in the winter olympics?": "Norway",
    "What is the signature food dish served at Wimbledon?": "Strawberries and cream"
}


def play_trivia_game(questions_answers):
    questions = list(questions_answers.keys())
    round_number = 1

    while questions:
        # Randomly select a question
        question = random.choice(questions)
        print(f"Round {round_number}: {question}")
        user_answer = input("Your answer: ").strip()

        # Check if the answer is correct
        correct_answer = questions_answers[question]
        if isinstance(correct_answer, list):  # If there are multiple correct answers
            is_correct = user_answer in correct_answer
        else:
            is_correct = user_answer.lower() == correct_answer.lower()

        if is_correct:
            print("Correct! You can give 2 sips to someone else.")
            # Remove the asked question and increment the round number
            questions.remove(question)
            round_number += 1

            if not questions:  # If all questions have been asked
                print("You finished all the questions! Everyone else has to finish their drink.")
                break

            print("\nNext round!\n")
        else:
            print(f"Wrong! Game Over. You have to drink {round_number * 2} sips.")
            break


# Start the game
play_trivia_game(questions_answers)
