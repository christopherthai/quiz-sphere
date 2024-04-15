from helpers.score_helper import get_user_scores, plot_score_comparison, compare_with_average, print_quiz_details_user
import inquirer

def scores_menu(user):
    user_scores = get_user_scores(user)

    print("Your scores on each quiz:")
    # for idx, (score, quiz_title, date_taken, quiz_id) in enumerate(user_scores, 1):
    #     print(f"{idx}. Quiz: {quiz_title}, Score: {score}, Date Taken: {date_taken}")
    for quiz, score in user_scores:
        print(f"{user_scores.index((quiz, score)) + 1}. Quiz: {quiz.title}, Score: {score.score}\n")

    print("\nOptions:")
    print("Enter the id of the quiz to see more options")
    print("0. Exit")
    choice = input("Enter your choice: ")

    if choice == "0":
        print("Exiting application...")
        exit()
    try:
        choice = int(choice)
        if choice > 0 and choice <= len(user_scores):
            display_quiz_options(user_scores[choice - 1][0].id, user)
        else:
            print("Invalid choice. Please enter a valid option.")
    except ValueError:
        print("Invalid choice. Please enter a valid option.")
        


def display_quiz_options (quiz_id, user):
    from main import main_menu

    questions = [
        inquirer.List(
            "action",
            message="Options for the selected quiz:",
            choices=["Plot score comparison graph", 
                    "View quiz details", 
                    # "View percentage of correct answers",
                    "Exit"
                    ],
        )
    ]
    answer = inquirer.prompt(questions)

    if answer["action"] == "Plot score comparison graph":
        plot_score_comparison(quiz_id, user)
        # Score.compare_with_average(quiz_id, self.user_score)
    elif answer["action"] == "View quiz details":
        print_quiz_details_user(quiz_id, user)
    # elif answer["action"] == "View percentage of correct answers":
    #     view_percentage_correct(quiz_id)
    elif answer["action"] == "Exit":
        print("Exiting to Main Menu...")
        main_menu(user)
        
    
