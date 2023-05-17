# Quiz Maker

This is a simple Python class that allows you to create and run quizzes. It provides methods for adding questions, options, answers, and ponderations. Users can participate in the quiz by answering the questions, and their score will be calculated based on the ponderations assigned to each question.

## Installation

1. Clone the repository or download the `quiz.py` file.

2. Make sure you have Python installed on your system. This code is compatible with Python 3.

## Usage

1. Import the `Quiz` class into your Python script or interactive Python environment.

```python
from quiz import Quiz
```

2. Create an instance of the `Quiz` class, providing a name for your quiz.

```python
my_quiz = Quiz("My Quiz")
```

3. Add questions to your quiz using the `add_question` method. Each question should include the question itself, a list of options, the index of the correct answer, and an optional ponderation (default is 1).

```python
my_quiz.add_question("What is the capital of France?", ["Paris", "London", "Berlin"], 1, 2)
```

4. Run the quiz using the `run_quiz` method. This will display each question, prompt the user for their answer, and provide feedback on their performance. The user's score will be calculated based on the ponderations assigned to each question.

```python
my_quiz.run_quiz()
```

5. After the quiz is completed, the user's score and the total score based on ponderations will be displayed.

## About the Programmer

This program was developed by Hatchy. Hatchy has been coding in Python since 2021 and this quiz maker is his first repository. For more information about Hatchy, you can visit their [GitHub profile](https://github.com/Hatchy-py).

## Example

Here's an example usage of the quiz maker:

```python
from quiz import Quiz

# Create a quiz
my_quiz = Quiz("Geography Quiz")

# Add questions with ponderations
my_quiz.add_question("What is the capital of France?", ["Paris", "London", "Berlin"], 1, 2)
my_quiz.add_question("What is the largest continent?", ["Africa", "Asia", "Europe"], 2, 3)

# Run the quiz
my_quiz.run_quiz()
```

## Contributing

Contributions to this project are welcome. Feel free to open issues and submit pull requests to suggest improvements or report bugs.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to modify and distribute this code for personal or commercial use.
