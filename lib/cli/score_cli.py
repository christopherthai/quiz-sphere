<<<<<<< HEAD
from helpers.score_helper import Score


def display_quiz_scores(user):
    user_scores = Score.get_user_scores(user.id)
=======
from helpers.score_helper import get_user_scores, get_average_score, compare_with_average, print_quiz_details


def display_quiz_scores(user):
    user_scores = get_user_scores(user.id)
>>>>>>> 8b49486d836808f377b6c5340a4224287b770f67

    print("Your scores on each quiz:")
    for idx, (score, quiz_name, date_taken, quiz_id) in enumerate(user_scores, 1):
        print(f"{idx}. Quiz: {quiz_name}, Score: {score}, Date Taken: {date_taken}")

    print("\nOptions:")
    print("Enter the number of the quiz to see more options")
    print("0. Exit")
    choice = input("Enter your choice: ")

<<<<<<< HEAD
    if choice == '0':
=======
    if choice == "0":
>>>>>>> 8b49486d836808f377b6c5340a4224287b770f67
        print("Exiting...")
        return
    try:
        choice = int(choice)
        if 1 <= choice <= len(user_scores):
            quiz_id = user_scores[choice - 1][3]
<<<<<<< HEAD
            self.display_quiz_options(quiz_id)
=======
            display_quiz_options(quiz_id)
>>>>>>> 8b49486d836808f377b6c5340a4224287b770f67
        else:
            print("Invalid choice. Please enter a valid option.")
    except ValueError:
        print("Invalid choice. Please enter a valid option.")

<<<<<<< HEAD
def display_quiz_options(user, quiz_id):
=======

def display_quiz_options(quiz_id):
>>>>>>> 8b49486d836808f377b6c5340a4224287b770f67
    print("\nOptions for the selected quiz:")
    print("1. Plot score comparison graph for this quiz")
    print("2. View quiz details")
    print("3. View questions with correct/incorrect answers")
    print("4. View percentage of correct answers for this quiz")
    print("5. Back to main menu")
    choice = input("Enter your choice: ")

<<<<<<< HEAD
    if choice == '1':
        Score.plot_score_comparison(quiz_id, user.id)
        Score.compare_with_average(quiz_id, user.score)
    elif choice == '2':
        print_quiz_details(quiz_id)
    elif choice == '3':
        view_questions_with_answers(quiz_id)
    elif choice == '4':
        view_percentage_correct(quiz_id)
    elif choice == '5':
=======
    if choice == "1":
        plot_score_comparison(quiz_id, user.id)
        # Score.compare_with_average(quiz_id, self.user_score)
    elif choice == "2":
        print_quiz_details(quiz_id)
    elif choice == "3":
        view_questions_with_answers(quiz_id)
    elif choice == "4":
        view_percentage_correct(quiz_id)
    elif choice == "5":
>>>>>>> 8b49486d836808f377b6c5340a4224287b770f67
        display_quiz_scores()
    else:
        print("Invalid choice. Please enter a valid option.")
