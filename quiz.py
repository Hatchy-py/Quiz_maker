class Quiz:
    def __init__(self, name):
        self.name = name
        self.questions = []

    def add_question(self, question, options, answer):
        self.questions.append((question, options, answer))

    def run_quiz(self):
        score = 0
        total_questions = len(self.questions)

        print(f"Welcome to the {self.name} Quiz!")
        print("-----------------------------")

        for i, (question, options, answer) in enumerate(self.questions):
            print(f"Question {i+1}: {question}")

            for j, option in enumerate(options):
                print(f"{j+1}. {option}")

            user_answer = input("Enter your answer (number): ")
            if user_answer == str(answer):
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is {answer}.")

            print("-----------------------------")

        print("Quiz Completed!")
        print("-----------------------------")
        print(f"Your score: {score}/{total_questions}")
