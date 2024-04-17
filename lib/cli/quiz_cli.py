import random
import inquirer

from helpers.quiz_helper import list_quizzes, list_quizzes_and_select_quiz
from helpers.user_helper import clear_screen
from helpers.question_helper import list_questions_and_answers_of_the_quiz
from helpers.score_helper import submit_score
from datetime import datetime
from PIL import Image

##########################################################################################################################################

# open image file
image_path = "data/quiz_sphere.webp"
image = Image.open(image_path)

# convert image to black and white
image = image.convert("L")

# adjust image size
width, height = image.size
aspect_ratio = height / width
new_width = 100
new_height = int(aspect_ratio * new_width * 0.5)
image = image.resize((new_width, new_height))

# ASCII code
ascii_chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

# convert image to ASCII code
ascii_art = ""
for y in range(new_height):
    for x in range(new_width):
        pixel_value = image.getpixel((x, y))
        ascii_art += ascii_chars[pixel_value // 25]
    ascii_art += "\n"

# print ASCII
print(ascii_art)

# press enter to next page
input("Press Enter to continue...")

##########################################################################################################################################

def quiz_menu(user):
    from main import main_menu

    list_quizzes()
    choices = ["Select Quiz", "Return to Main Menu"]
    choice = inquirer.list_input("Select", choices=choices)
    if choice == "Select Quiz":
        selected_quiz_id = list_quizzes_and_select_quiz()
        # start_quiz(selected_quiz_id)
        question_and_answers = list_questions_and_answers_of_the_quiz(selected_quiz_id)
        quiz_flow(question_and_answers, selected_quiz_id, user)
        quiz_menu(user)
    elif choice == "Return to Main Menu":
        clear_screen()
        main_menu(user)

def quiz_flow(questions_and_answers, selected_quiz_id, user):
    """Starts the quiz flow after selecting a quiz."""
    clear_screen()

    if len(questions_and_answers) > 10:
        questions_and_answers = random.sample(questions_and_answers, 10)

    total_questions = len(questions_and_answers)
    score = 0

    for question in questions_and_answers:
        clear_screen()

        print(f"Question: {question.content}")
        answers = question.answers
        choices = [answer.content for answer in answers]
        random.shuffle(choices)  # shuffle answer randomly
        correct_answer = next(
            (answer.content for answer in answers if answer.is_correct), None
        )

        answer = inquirer.list_input("Choose the correct answer", choices=choices)

        correct_messages = [
            "Excellent work!",
            "Correct! Nice job!",
            "Well done! You got it right!",
            "Perfect! Keep it up!",
            "That's right! You're doing great!",
            "You are a G.E.N.I.U.S.!!",
            "Beautiful answer!!",
            "Fantastic! You nailed it!",
            "Brilliant answer! You really know your stuff!",
            "Superb! Couldn't have done it better myself!"
            "That’s correct! You’re on a roll!",
            "Impressive! Keep up the great work!",
            "Absolutely right! You're doing brilliantly!",
            "Perfect response! You're so sharp!",
            "Great job! I'm so proud of you!",
            "Correct! You have a great understanding!",
            "Outstanding performance! You're a star!",
            "You got it right! You're making great progress!",
            "That's the right answer! You're acing this!",
            "Yes! You did it perfectly right!",
            "Wonderful! You really stood out today!",
            "Marvelous! That was first class work!",
            "Exactly right! You are so thoughtful!",
            "You’ve got it! That was very clever!",
            "Spot on! You're quite the expert!",
            "That's right! What an insightful answer!",
        ]

        if answer == correct_answer:
            print(random.choice(correct_messages))
            score += 10
        else:
            print("Wrong! The correct answer was:", correct_answer)

        input("Press Enter to continue...")

    clear_screen()
    print(f"Your final score is {score}/{total_questions * 10}.")
    handle_score_submission(questions_and_answers, score, selected_quiz_id, user)

def handle_score_submission(questions_and_answers, score, selected_quiz_id, user):
    if score < 60:

##########################################################################################################################################
        
        # open image file
        image_path = "data/pepe.webp"
        image = Image.open(image_path)

        # convert image to black and white
        image = image.convert("L")

        # adjust image size
        width, height = image.size
        aspect_ratio = height / width
        new_width = 100
        new_height = int(aspect_ratio * new_width * 0.5)
        image = image.resize((new_width, new_height))

        # ASCII code
        ascii_chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

        # convert image to ASCII code
        ascii_art = ""
        for y in range(new_height):
            for x in range(new_width):
                pixel_value = image.getpixel((x, y))
                ascii_art += ascii_chars[pixel_value // 25]
            ascii_art += "\n"

        # print ASCII
        print(ascii_art)

        # press enter to next page
        input("Press Enter to continue...")

        clear_screen()

##########################################################################################################################################
        
        retry = inquirer.confirm(
            "Your score is below 60. Do you want to take it again?", default=True
        )

        if retry:
            quiz_flow(
                questions_and_answers, selected_quiz_id, user
            )  # Pass the quiz ID to restart the same quiz
        else:
            quiz_menu(user)
    else:
        
##########################################################################################################################################

        # open image file
        image_path = "data/good_pepe.jpeg"
        image = Image.open(image_path)

        # convert image to black and white
        image = image.convert("L")

        # adjust image size
        width, height = image.size
        aspect_ratio = height / width
        new_width = 100
        new_height = int(aspect_ratio * new_width * 0.5)
        image = image.resize((new_width, new_height))

        # ASCII code
        ascii_chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

        # convert image to ASCII code
        ascii_art = ""
        for y in range(new_height):
            for x in range(new_width):
                pixel_value = image.getpixel((x, y))
                ascii_art += ascii_chars[pixel_value // 25]
            ascii_art += "\n"

        # print ASCII
        print(ascii_art)

        # press enter to next page
        input("Press Enter to continue...")

        clear_screen()

##########################################################################################################################################
        
        submit = inquirer.confirm("Submit score?", default=True)
        if submit:
            submit_score(score, get_formatted_date(), user, selected_quiz_id)
            print("Score was submitted successfully.\n")
            input("Press Enter to continue...")
            clear_screen()
        quiz_menu(user)


def get_formatted_date():
    return datetime.now().strftime("%Y-%m-%d")

if __name__ == "__main__":
    quiz_menu()
