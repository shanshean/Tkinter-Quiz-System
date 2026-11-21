Here's the fully formatted, ready-to-copy README.md version! ✨
 
 
 
markdown  
# 📖 Python Knowledge Quiz — README

## 📌 About the Project
Python Knowledge Quiz is a desktop quiz application built with Python and Tkinter. It tests your basic Python knowledge through 10 carefully selected questions — with both question order AND answer choices shuffled randomly every time you play! 🎲✨ Complete with a countdown timer, score tracking, high score system, and a friendly interface.

## ✨ Features
- 👋 Player Name Entry — Personalized welcome screen
- 🎲 Randomized Questions — Questions appear in different order each time
- 🔀 Shuffled Answer Choices — A/B/C/D options are mixed up every game
- ⏱️ Time Limit — 15 seconds per question
- 📊 Progress Bar — Shows how far you are in the quiz
- 🏆 High Score System — Automatically saves your best score
- 🔊 Sound Effects — Different sounds for correct, wrong, and complete (Windows only)
- 📝 Answer Review — Scrollable review of wrong answers
- 💖 Friendly Messages — Sweet encouragement throughout the game
- 🔁 Play Again / Exit — Easy restart or close options

## 📂 Files Included
 
 
project-folder/
├── quiz.py           # Main Python quiz program
├── high_score.txt    # Auto-created file to store high score
└── README.md         # This file
 
plaintext  

## 🚀 How to Run

### Requirements
- Python 3.x installed on your computer
- Tkinter (usually comes pre-installed with Python)

### Step-by-Step
1. Copy the code into a file named `quiz.py`
2. Open Command Prompt (Windows) or Terminal (Mac/Linux)
3. Navigate to where your file is saved:
```bash
cd path/to/your/folder
 
 
4. Run the program:
 
bash  
python quiz.py
 
 
💡 On some systems you may need to use  python3 quiz.py  instead.
 
📋 How to Play
 
1. Enter your name and click CONTINUE
2. Read the instructions on the start screen, then click ✨ START QUIZ ✨
3. Select the best answer for each question — options are shuffled every time!
4. Click SUBMIT to lock in your answer — the timer stops
5. Click CONTINUE for the next question
6. If time runs out, you'll see a "Time's up" message and the quiz will end
7. At the end, view your score, percentage, and review any wrong answers
8. Choose PLAY AGAIN (questions and choices reshuffle automatically) or EXIT
 
🧠 Topics Covered
 
# Topic 
1 Functions ( def  keyword) 
2 Python file extension ( .py ) 
3 Comments ( # ) 
4 Output function ( print() ) 
5 Boolean data type 
6 Operator precedence 
7 For loops 
8  len()  function 
9 Importing modules 
10 What Python is 
 
💡 How Shuffling Works
 
- Questions:  random.sample()  shuffles the order of the 10 questions each game
- Answer Choices: The  shuffle_choices()  function mixes up A/B/C/D options while keeping track of the correct answer — so you can't memorize the letter position! ✨
 
⚠️ Important Notes
 
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
