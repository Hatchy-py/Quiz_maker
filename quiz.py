class Quiz:
    def __init__(self, name):
        self.name = name
        self.questions = []
        self.ponderations = []

    def add_question(self, question, options, answer, ponderation = 1):
        self.questions.append((question, options, answer, ponderation))
        self.ponderations.append(ponderation)

    def run_quiz(self):
        score = 0
        total_questions = sum(self.ponderations)

        print(f"Welcome to the {self.name} Quiz!")
        print("-----------------------------")

        for i, (question, options, answer, ponderation) in enumerate(self.questions):
            print(f"Question {i+1}: {question}")

            for j, option in enumerate(options):
                print(f"{j+1}. {option}")

            user_answer = input("Enter your answer (number): ")
            if user_answer == str(answer):
                print("Correct!")
                score += ponderation
            else:
                print(f"Wrong! The correct answer is {answer}.")

            print("-----------------------------")

        print("Quiz Completed!")
        print("-----------------------------")
        print(f"Your score: {score}/{total_questions}")
        print("Your Grade: ", score/total_questions*100, "%")
