# Python Knowledge Quiz

## About the Project
Python Knowledge Quiz is a desktop quiz application built with Python and Tkinter. <br>It tests your basic Python knowledge through 10 carefully selected questions — with both question order AND answer choices shuffled randomly every time you play!<br> Complete with a countdown timer, score tracking, high score system, and a friendly interface.

## Features
- Player Name Entry — Personalized welcome screen
- Randomized Questions — Questions appear in different order each time
- Shuffled Answer Choices — A/B/C/D options are mixed up every game
- Time Limit — 15 seconds per question
- Progress Bar — Shows how far you are in the quiz
- High Score System — Automatically saves your best score
- Sound Effects — Different sounds for correct, wrong, and complete (Windows only)
- Answer Review — Scrollable review of wrong answers
- Friendly Messages — Sweet encouragement throughout the game
- Play Again / Exit — Easy restart or close options

## 📂 Files Included

project-folder/ 
├── quiz.py           # Main Python quiz program
├── high_score.txt    # Auto-created file to store high score
└── README.md         # This file

## How to Run

### Requirements
- Python 3.x installed on your computer
- Tkinter (usually comes pre-installed with Python)

### Step-by-Step
- 1. Copy the code into a file named `quiz.py`
- 2. Open Command Prompt (Windows) or Terminal (Mac/Linux)
- 3. Navigate to where your file is saved: <br>cd path/to/your/folder
- 4. Run the program:
 
> [View python script](def_function.py)
  On some systems you may need to use  python3 quiz.py  instead.

#How It Works
 
1. Questions
 
- Storage: All 10 questions are stored in a list of dictionaries. Each dictionary contains three parts: the question text, a list of four answer choices labeled A–D, and a single letter that represents the correct answer.
​
- Shuffling the order: When the quiz starts,  random.sample()  creates a new random order of the questions without removing any. This means every game starts with a different question first.
​
- Shuffling the choices: The  shuffle_choices()  function takes each question, removes the A/B/C/D labels from the choices, mixes the texts randomly, reassigns new A/B/C/D labels, and keeps track of where the correct answer moved to. This ensures the correct answer is never always in the same position.
 
2. Timer
 
- Counting down: When a question is displayed, the timer starts at 15 seconds. The  update_timer()  function shows the remaining time on the screen, subtracts 1 second every 1,000 milliseconds using  root.after() , and calls itself again. It repeats until time reaches 0.
​
- Stopping: When you click SUBMIT, the  stop_timer()  function cancels the scheduled countdown so the number stops decreasing. An  answered  flag is also set to  True  so the timer function knows to exit early.
​
- Time's up: If the timer reaches 0 before you submit, the quiz automatically ends and shows a "Time's up" message.
 
3. Correct Answer
 
- Each question stores the correct answer as a single letter, such as  "B" .
​
- When you click SUBMIT, the program reads which letter you selected using  selected_answer.get() .
​
- It compares your selected letter against the question's stored answer value. If they match, your score increases by 1. If they don't match, your answer and the correct answer are saved to a list so you can review them at the end.
 
Score and Percentage
 
- Score: Starts at 0. It increases by exactly 1 point each time you submit a correct answer. The  answered  flag prevents the score from being increased multiple times for the same question.
​
- Percentage: Calculated at the end by dividing your final score by the total number of questions, then multiplying by 100:  (score / total) × 100 . The result is displayed with one decimal place.
 
High Score
 
- Reading: When the program starts,  get_high_score()  checks if a file named  high_score.txt  exists. If it does, it reads the number stored inside and displays it on the welcome screen. If the file doesn't exist or is empty, it shows 0 as the default high score.
​
- Saving: When you finish a quiz,  save_high_score()  compares your score<br> to the previously saved high score. Only if your new score<br> is higher does it overwrite the file with your new score. If it's equal <br>or lower, the file stays unchanged.
​
- Persistence: Because the high score is stored in a separate text file, <br> it remains on your computer even after you close the program.<br> When you reopen the program later, it reads that same file again <br>and shows your best score from before.
​
- Proof: After achieving a high score, closing the program completely and reopening <br> it shows the same high score on the start screen — confirming the data was <br> saved correctly to the external file.
 
# How to Play
 
1. Enter your name and click CONTINUE <br>
2. Read the instructions on the start screen, then click START QUIZ <br>
3. Select the best answer for each question — options are shuffled every time! <br>
4. Click SUBMIT to lock in your answer — the timer stops <br>
5. Click CONTINUE for the next question <br>
6. If time runs out, you'll see a "Time's up" message and the quiz will end <br>
7. At the end, view your score, percentage, and review any wrong answers <br>
8. Choose PLAY AGAIN (questions and choices reshuffle automatically) or EXIT <br>
 
# Topics
 
- Functions ( def  keyword) 
- Python file extension ( .py ) 
- Comments ( # ) 
- Output function ( print() ) 
- Boolean data type 
- Operator precedence 
- For loops 
- len()  function 
- Importing modules 
- What Python is 
 
# How Shuffling Works
 
- Questions:  random.sample()  shuffles the order of the 10 questions each game
- Answer Choices: The  shuffle_choices()  function mixes up A/B/C/D options <br> while keeping track of the correct answer — so you can't memorize the letter position!
 
# Important Notes
 
- The  high_score.txt  file is automatically created when you get a new high score
- Sound effects work on Windows only — they won't cause errors on other systems
- Clicking the X (close button) safely exits the program
- Your progress is not saved if you exit mid-quiz
- Both questions AND answer choices are in different positions every time you play

#Functions

| Function | Purpose | Called when |
|----------|---------|-------------|
| start_quiz() | Resets the variables and shuffles the questions | Start or Restart is clicked |
| update_timer() | Shows the time left and counts down every second | A question is displayed |
| submit_answer() | Checks the answer and updates the score | Submit is clicked |
| save_high_score() | Writes the score to the text file if it is higher | The results screen is shown |
| show_result() | Displays score, percentage, message, and review | After question 10 |
| shuffle_choices() | Mixes up A–D options while keeping track of the correct answer | When starting the quiz |
 
#Author
 
Name: Sheannen Gleih E. Alerta<br>
Course/Year/Section: INFOTECH SE - 3A<br>
Subject: CT5
