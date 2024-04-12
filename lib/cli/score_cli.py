import inquirer
from score_controller import show_scores


def score_menu():
    questions = [
        inquirer.List(
            "action",
            message="Score tasks - select an option:",
            choices=["Show Scores", "Exit"],
        ),
    ]
    answer = inquirer.prompt(questions)
    if answer["action"] == "Show Scores":
        user_id = input("Enter the user ID to show scores for: ")
        print(show_scores(user_id))
    elif answer["action"] == "Exit":
        return
