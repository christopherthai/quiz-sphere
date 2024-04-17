from helpers.score_helper import (
    get_user_scores,
    get_average_scores,
    plot_score_comparison,
    compare_with_average,
)
from helpers.user_helper import clear_screen
import inquirer
from models.quiz import Quiz
from tabulate import tabulate


from helpers.quiz_helper import print_quiz_details


# Function to display user scores in a table
def display_user_scores(user_scores):
    """Display user scores in a table."""
    table_data = []
    for i, (quiz, score) in enumerate(user_scores, start=1):
        table_data.append([i, quiz.title, score.score, score.date_taken])

    headers = ["#", "Quiz", "Score", "Date Taken"]
    print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))


# Code and logic for the user's scores menu
def scores_menu(user):
    from main import main_menu

    user_scores = get_user_scores(user)

    user_scores = [(quiz, score) for quiz, score in user_scores]

    print("Your scores on each quiz:")
    display_user_scores(user_scores)

    # for quiz, score in user_scores:
    #     print(
    #         f"{user_scores.index((quiz, score)) + 1}. Quiz: {quiz.title} - Score: {score.score} - Date: {score.date_taken}\n"
    #     )

    print("\nOptions:")
    print("Enter the quiz # to see more options")
    print("0. Return to Main Menu\n")
    choice = input("Enter your choice: ")

    if choice == "0":
        clear_screen()
        main_menu(user)
    try:
        choice = int(choice)
        if choice > 0 and choice <= len(user_scores):
            display_quiz_options(user_scores[choice - 1][0].id, user)
        else:
            print("Invalid choice. Please enter a valid option.")
    except ValueError:
        print("Invalid choice. Please enter a valid option.")


def display_quiz_options(quiz_id, user):

    quiz = Quiz.find_by_id(quiz_id)

    user_score, average_score = get_average_scores(quiz_id, user)

    questions = [
        inquirer.List(
            "action",
            message="Options for the selected quiz:",
            choices=[
                "Compare to average score",
                "Plot score comparison graph",
                "Print Quiz Details",
                "Exit",
            ],
        )
    ]
    answer = inquirer.prompt(questions)

    if answer["action"] == "Compare to average score":
        clear_screen()
        comparison_result = compare_with_average(average_score, user_score)
        clear_screen()
        print(comparison_result[0])
        print()
        display_quiz_options(quiz_id, user)
    elif answer["action"] == "Plot score comparison graph":
        clear_screen()
        plot_score_comparison(quiz, user)
        display_quiz_options(quiz_id, user)
    elif answer["action"] == "Print Quiz Details":
        clear_screen()
        print_quiz_details(quiz, user)
        display_quiz_options(quiz_id, user)
    elif answer["action"] == "Exit":
        clear_screen()
        print("Exiting to Scores Menu...")
        scores_menu(user)
