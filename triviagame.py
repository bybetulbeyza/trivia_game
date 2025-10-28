import random

questions = {
  "What is the keyword to define a function in Python?" : "def",
  "Which data type is used to store True or False values?" : "boolean",
  "What is the correct file extension for Python files?" : ".py",
  "which symbol is used to comment in Python?" : "#",
  "What function is use to get input from the user?" : "input",
  "How do you start a for loop in Python?" : "for",
  "What keyword is used to import a module in Python?" : "import",
  "What does the len() function return?" : "lenght",
  "What is the result of 10//3 in Python?" : "3"
}
def python_trivia_game():
  questions_list = list(questions.keys()) # we convert key into a regular Python list
  total_questions = 5
  score = 0
  selected_questions = random.sample(questions_list,total_questions)
  

  for idx, question in enumerate(selected_questions):
    print(f"{idx+1}.{question}")
    user_answer =input("Your answer: ").lower().strip()

    correct_answer = questions[question]

    if user_answer == correct_answer.lower():
      print("Correct!\n")
      score += 1
    else:
      print(f"Wrong. The correct answer is: {correct_answer}.\n")  
  print(f"your final score is: {score}/{total_questions}")    
    


python_trivia_game()