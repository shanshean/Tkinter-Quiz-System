import tkinter as tk
from tkinter import messagebox
import random
import os
import sys

# *********** QUIZ DATA ***********
QUESTIONS = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "choices": ["A. func", "B. def", "C. function", "D. define"],
        "answer": "B"
    },
    {
        "question": "What is the correct file extension for Python files?",
        "choices": ["A. .pyt", "B. .pt", "C. .py", "D. .python"],
        "answer": "C"
    },
    {
        "question": "Which symbol starts a single-line comment in Python?",
        "choices": ["A. //", "B. /*", "C. #", "D. --"],
        "answer": "C"
    },
    {
        "question": "What function is used to output text in Python?",
        "choices": ["A. echo()", "B. print()", "C. write()", "D. output()"],
        "answer": "B"
    },
    {
        "question": "Which data type stores True or False values?",
        "choices": ["A. Integer", "B. String", "C. Boolean", "D. Float"],
        "answer": "C"
    },
    {
        "question": "What is the output of: print(2 + 3 * 2)?",
        "choices": ["A. 10", "B. 8", "C. 7", "D. 5"],
        "answer": "B"
    },
    {
        "question": "Which loop is used to iterate over a sequence?",
        "choices": ["A. while", "B. do", "C. for", "D. repeat"],
        "answer": "C"
    },
    {
        "question": "What does the len() function return?",
        "choices": ["A. Length of an object", "B. Last element", "C. List of elements", "D. Number type"],
        "answer": "A"
    },
    {
        "question": "Which keyword is used to import a module?",
        "choices": ["A. load", "B. import", "C. include", "D. require"],
        "answer": "B"
    },
    {
        "question": "What is Python?",
        "choices": ["A. A snake only", "B. A programming language", "C. A database", "D. An operating system"],
        "answer": "B"
    }
]

# *********** SETTINGS ***********
TIME_LIMIT = 15
HIGH_SCORE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "high_score.txt")

# *********** GLOBAL VARIABLES ***********
quiz_questions = []
current_question = 0
score = 0
time_left = TIME_LIMIT
wrong_answers = []
timer_job = None
answered = False
choice_buttons = []
pulse_job = None
player_name = ""

# *********** SOUND FUNCTION ***********
def play_sound(sound_type):
    try:
        if sys.platform == "win32":
            import winsound
            if sound_type == "correct":
                winsound.MessageBeep(winsound.MB_ICONINFORMATION)
            elif sound_type == "wrong":
                winsound.MessageBeep(winsound.MB_ICONHAND)
            elif sound_type == "complete":
                winsound.MessageBeep(winsound.MB_ICONASTERISK)
    except:
        pass

# *********** EXIT FUNCTION ***********
def exit_quiz():
    if messagebox.askyesno("Exit Quiz", "Are you sure you want to exit, dear?\nYour progress will be lost, you know."):
        root.destroy()

# *********** MAIN WINDOW ***********
root = tk.Tk()
root.title("Python Knowledge Quiz")
root.geometry("750x650")
root.resizable(False, False)
root.configure(bg="#E6E6FA")

selected_answer = tk.StringVar()

# *********** TOP BAR WITH EXIT BUTTON ***********
top_bar = tk.Frame(root, bg="#E6E6FA")
top_bar.pack(fill="x", padx=20, pady=8)

exit_btn = tk.Button(
    top_bar,
    text="EXIT",
    font=("Courier", 11, "bold"),
    bg="#D4C1EC",
    fg="#5C4B7A",
    padx=20,
    pady=6,
    command=exit_quiz,
    relief="solid",
    bd=0,
    cursor="hand2"
)
exit_btn.pack(side="right")

main_frame = tk.Frame(root, bg="#E6E6FA")
main_frame.pack(fill="both", expand=True, padx=30, pady=5)

# *********** HIGH SCORE ***********
def get_high_score():
    if os.path.exists(HIGH_SCORE_FILE):
        try:
            with open(HIGH_SCORE_FILE, "r") as file:
                return int(file.read().strip())
        except ValueError:
            return 0
    return 0

def save_high_score(new_score):
    if new_score > get_high_score():
        with open(HIGH_SCORE_FILE, "w") as file:
            file.write(str(new_score))
        return True
    return False

# *********** CLEAR SCREEN ***********
def clear_screen():
    global pulse_job
    if pulse_job:
        root.after_cancel(pulse_job)
        pulse_job = None
    for widget in main_frame.winfo_children():
        widget.destroy()

# *********** BUTTON ANIMATION ***********
def pulse_button(btn, color1, color2, delay=700):
    global pulse_job
    current = btn.cget("bg")
    next_color = color2 if current == color1 else color1
    btn.config(bg=next_color)
    pulse_job = root.after(delay, lambda: pulse_button(btn, color1, color2, delay))

# *********** PROGRESS BAR ***********
def update_progress_bar():
    progress = (current_question + 1) / len(quiz_questions)
    progress_width = int(650 * progress)
    progress_canvas.delete("progress")
    progress_canvas.create_rectangle(0, 0, progress_width, 25, fill="#6B8E6B", outline="", tags="progress")
    progress_label.config(text=f"Progress: {current_question + 1}/{len(quiz_questions)}")

# *********** NAME ENTRY SCREEN ***********
def show_name_screen():
    clear_screen()
    
    tk.Label(main_frame, text="=====================================", font=("Courier", 13), bg="#E6E6FA", fg="#B4A7C9").pack(pady=(80, 10))
    tk.Label(main_frame, text="        WELCOME TO THE QUIZ!       ", font=("Courier", 24, "bold"), bg="#E6E6FA", fg="#5C4B7A").pack(pady=10)
    tk.Label(main_frame, text="=====================================", font=("Courier", 13), bg="#E6E6FA", fg="#B4A7C9").pack(pady=(10, 40))
    
    tk.Label(main_frame, text="May I know your name, my dear?", font=("Courier", 15), bg="#E6E6FA", fg="#5C4B7A").pack(pady=10)
    
    name_entry = tk.Entry(main_frame, font=("Courier", 16), width=32, bg="#FFFFFF", fg="#5C4B7A", relief="solid", bd=1)
    name_entry.pack(pady=15, ipady=8)
    name_entry.focus()
    
    def start_with_name():
        global player_name
        player_name = name_entry.get().strip()
        if not player_name:
            messagebox.showwarning("Error! Name Required", "Sorry, dear. I need to know your name first ^_-☆.")
            return
        show_start_screen()
    
    tk.Button(main_frame, text="CONTINUE", font=("Courier", 16, "bold"), bg="#FFDFCC", fg="#5C4B7A",
              padx=50, pady=12, command=start_with_name, relief="solid", bd=0, cursor="hand2").pack(pady=20)
    root.bind("<Return>", lambda event: start_with_name())

# *********** START SCREEN ***********
def show_start_screen():
    clear_screen()
    
    tk.Label(main_frame, text="=====================================", font=("Courier", 13), bg="#E6E6FA", fg="#B4A7C9").pack(pady=(30, 5))
    tk.Label(main_frame, text=f"        WELCOME, my dear player {player_name.upper()}!        ", font=("Courier", 20, "bold"), bg="#E6E6FA", fg="#5C4B7A").pack(pady=5)
    tk.Label(main_frame, text="        PYTHON KNOWLEDGE QUIZ        ", font=("Courier", 26, "bold"), bg="#E6E6FA", fg="#5C4B7A").pack(pady=5)
    tk.Label(main_frame, text="=====================================", font=("Courier", 13), bg="#E6E6FA", fg="#B4A7C9").pack(pady=(5, 15))
    
    tk.Label(main_frame, text=f"High Score: {get_high_score()} / {len(QUESTIONS)}", font=("Courier", 15), bg="#E6E6FA", fg="#7A6B96").pack(pady=5)
    
    tk.Label(main_frame, text="-------------------------------------", font=("Courier", 11), bg="#E6E6FA", fg="#D4C1EC").pack(pady=10)
    tk.Label(main_frame, text=f"Time per question:\n you only have {TIME_LIMIT} seconds, my dear!", font=("Courier", 14), bg="#E6E6FA", fg="#5C4B7A").pack()
    tk.Label(main_frame, text=f"Total questions: {len(QUESTIONS)}", font=("Courier", 14), bg="#E6E6FA", fg="#5C4B7A").pack(pady=5)
    tk.Label(main_frame, text="-------------------------------------", font=("Courier", 11), bg="#E6E6FA", fg="#D4C1EC").pack(pady=25)
    
    start_btn = tk.Button(main_frame, text="✨  START QUIZ  ✨", font=("Courier", 20, "bold"), bg="#FFDFCC", fg="#5C4B7A",
                          padx=50, pady=15, command=start_quiz, relief="solid", bd=0, cursor="hand2")
    start_btn.pack(pady=10)
    
    tk.Label(main_frame, text="       Good luck and have fun!       ", font=("Courier", 13, "italic"), bg="#E6E6FA", fg="#B4A7C9").pack(pady=20)
    
    pulse_button(start_btn, "#FFDFCC", "#FFE8B3", 700)
    
# *********** SHUFFLE ANSWER CHOICES ***********
def shuffle_choices(question):
    correct_letter = question["answer"]
    correct_text = ""
    for choice in question["choices"]:
        if choice.startswith(correct_letter + "."):
            correct_text = choice[2:].strip()
            break
    choice_texts = [c[2:].strip() for c in question["choices"]]
    random.shuffle(choice_texts)
    letters = ["A", "B", "C", "D"]
    new_choices = []
    new_correct_letter = ""
    for i, text in enumerate(choice_texts):
        new_choice = f"{letters[i]}. {text}"
        new_choices.append(new_choice)
        if text == correct_text:
            new_correct_letter = letters[i]
    return {
        "question": question["question"],
        "choices": new_choices,
        "answer": new_correct_letter
    }


# *********** START QUIZ ***********
def start_quiz():
    global quiz_questions, current_question, score, wrong_answers
    # Shuffle question order
    shuffled_questions = random.sample(QUESTIONS, len(QUESTIONS))
    # Shuffle answer choices for each question
    quiz_questions = [shuffle_choices(q) for q in shuffled_questions]
    current_question = 0
    score = 0
    wrong_answers = []
    show_question()

# *********** SHOW QUESTION ***********
def show_question():
    global time_left, answered, choice_buttons, progress_canvas, progress_label
    clear_screen()
    time_left = TIME_LIMIT
    answered = False
    selected_answer.set("")
    
    question = quiz_questions[current_question]
    
    # Progress Bar
    progress_frame = tk.Frame(main_frame, bg="#E6E6FA")
    progress_frame.pack(fill="x", pady=(0, 15))
    
    progress_label = tk.Label(progress_frame, text="", font=("Courier", 11, "bold"), bg="#E6E6FA", fg="#5C4B7A")
    progress_label.pack(anchor="w")
    
    progress_canvas = tk.Canvas(progress_frame, width=650, height=25, bg="#DDDDDD", highlightthickness=0, relief="flat")
    progress_canvas.pack()
    update_progress_bar()
    
    timer_label_display = tk.Label(main_frame, text=f"You only have {time_left}s remaining, my dear!", font=("Courier", 14, "bold"), bg="#E6E6FA", fg="#D17B7B")
    timer_label_display.pack(pady=5)
    
    tk.Label(main_frame, text="-------------------------------------", font=("Courier", 11), bg="#E6E6FA", fg="#D4C1EC").pack(pady=10)
    tk.Label(main_frame, text=question["question"], font=("Courier", 16, "bold"), bg="#E6E6FA", fg="#5C4B7A", wraplength=680).pack(pady=15)
    tk.Label(main_frame, text="-------------------------------------", font=("Courier", 11), bg="#E6E6FA", fg="#D4C1EC").pack(pady=10)
    
    choice_buttons = []
    for choice in question["choices"]:
        letter = choice[0]
        rb = tk.Radiobutton(main_frame, text=choice, variable=selected_answer, value=letter, font=("Courier", 13),
                            bg="#E6E6FA", fg="#5C4B7A", selectcolor="#FFE8B3", activebackground="#FFE8B3", relief="flat")
        rb.pack(fill="x", padx=30, pady=5)
        choice_buttons.append(rb)
    
    global feedback_label, submit_button, next_button
    feedback_label = tk.Label(main_frame, text="", font=("Courier", 15, "bold"), bg="#E6E6FA")
    feedback_label.pack(pady=12)
    
    btn_frame = tk.Frame(main_frame, bg="#E6E6FA")
    btn_frame.pack(pady=10)
    
    submit_button = tk.Button(btn_frame, text="SUBMIT", font=("Courier", 12, "bold"), bg="#FFE8B3", fg="#5C4B7A",
                              width=16, padx=10, pady=8, command=submit_answer, relief="solid", bd=0, cursor="hand2")
    submit_button.grid(row=0, column=0, padx=15)
    
    next_button = tk.Button(btn_frame, text="CONTINUE", font=("Courier", 12, "bold"), bg="#D4C1EC", fg="#5C4B7A",
                            width=16, padx=10, pady=8, command=next_question, state="disabled", relief="solid", bd=0, cursor="hand2")
    next_button.grid(row=0, column=1, padx=15)
    
    update_timer(timer_label_display)

# *********** LOCK CHOICES ***********
def lock_choices():
    for btn in choice_buttons:
        btn.config(state="disabled")

# *********** TIMER FUNCTIONS ***********
def update_timer(timer_label_display):
    global time_left, timer_job, answered
    if answered:
        return
    timer_label_display.config(text=f"You only have {time_left}s remaining, my dear!")
    if time_left == 0:
        time_up()
        return
    time_left -= 1
    timer_job = root.after(1000, lambda: update_timer(timer_label_display))

def stop_timer():
    global timer_job
    if timer_job is not None:
        root.after_cancel(timer_job)
        timer_job = None

# *********** TIME UP ***********
def time_up():
    global answered
    answered = True
    stop_timer()
    lock_choices()
    submit_button.config(state="disabled", bg="#E0D8CC")
    
    feedback_label.config(text="⏰ Oh no! Time's up, my dear! Thank you for playing. 💛", 
                          fg="#D17B7B", bg="#FFE4E4", padx=15, pady=10)
    play_sound("wrong")
    
    # Auto exit after 2 seconds
    def show_goodbye_and_exit():
        messagebox.showinfo("Goodbye", f"My dear {player_name.upper()}, thank you for playing! 💐\nSee you next time! ✨")
        exit_quiz()
    
    root.after(2000, show_goodbye_and_exit)

# *********** SUBMIT ANSWER ***********
def submit_answer():
    global score, answered
    if answered:
        return
    choice = selected_answer.get()
    if choice == "":
        messagebox.showwarning("No answer", "You need to select an answer first, my dear!")
        return
    answered = True
    stop_timer()
    lock_choices()
    submit_button.config(state="disabled", bg="#E8E0CC")
    
    question = quiz_questions[current_question]
    if choice == question["answer"]:
        score += 1
        feedback_label.config(text="That's right! Great job, my dear!", fg="#2E7D32", bg="#E8F5E9", padx=15, pady=8)
        play_sound("correct")
    else:
        wrong_answers.append({
            "question": question["question"],
            "your_answer": choice,
            "correct_answer": question["answer"]
        })
        feedback_label.config(text="Oopsie! Wrong answer, dearie!", fg="#C62828", bg="#FFEBEE", padx=15, pady=8)
        play_sound("wrong")
    
    next_button.config(state="normal")
    next_button.config(bg="#FFDFCC")

# *********** NEXT QUESTION ***********
def next_question():
    global current_question
    current_question += 1
    if current_question < len(quiz_questions):
        show_question()
    else:
        show_result()

# *********** RESULT SCREEN ***********
def show_result():
    clear_screen()
    stop_timer()
    play_sound("complete")
    
    total = len(quiz_questions)
    percentage = (score / total) * 100
    new_record = save_high_score(score)
    
    tk.Label(
    	main_frame, 
    	text="=====================================", 
    	font=("Courier", 13), 
    	bg="#E6E6FA", 
    	fg="#B4A7C9").pack(pady=(30, 5))
    	
    tk.Label(
    	main_frame, 
    	text=f"        CONGRATULATIONS, my dear {player_name.upper()}!        ", 
    	font=("Courier", 20, "bold"), 
    	bg="#E6E6FA", 
    	fg="#5C4B7A").pack(pady=5)
    
    tk.Label(
    	main_frame, 
    	text="        QUIZ COMPLETE!(((o(*> - <*)o)))        ", 
    	font=("Courier", 17, "bold"), 
    	bg="#E6E6FA", 
    	fg="#5C4B7A").pack(pady=5)
    
    tk.Label(
    	main_frame, 
    	text=f"        I knew it! Learning did looks good on you! Keep it up! o(^▽^)o        ", 
    	font=("Courier", 15, "bold"), 
    	bg="#E6E6FA", 
    	fg="#5C4B7A").pack(pady=5)
    
    tk.Label(
    	main_frame, 
    	text="=====================================", 
    	font=("Courier", 13), 
    	bg="#E6E6FA", 
    	fg="#B4A7C9").pack(pady=(5, 20))
    
    if new_record:
        tk.Label(
        	main_frame, 
        	text="NEW HIGH SCORE!", 
        	font=("Courier", 14, "bold"), 
        	bg="#E6E6FA", 
        	fg="#E07A5F").pack(pady=10)
    
    tk.Label(
    	main_frame, 
    	text=f"Your Score:  {score} / {total}", 
    	font=("Courier", 12, "bold"), 
    	bg="#E6E6FA", 
    	fg="#5C4B7A").pack()
    	
    tk.Label(
    	main_frame, 
    	text=f"Percentage:   {percentage:.1f}%", 
    	font=("Courier", 12), 
    	bg="#E6E6FA", 
    	fg="#7A6B96").pack(pady=5)
    
    tk.Label(
    	main_frame, 
    	text="-------------------------------------", 
        font=("Courier", 10), 
        bg="#E6E6FA", 
        fg="#D4C1EC").pack(pady=15)
    
    if percentage >= 90:
        message = "Wow! Excellent work, my dear! You're amazing!"
        msg_color = "#6B8E6B"
    elif percentage >= 70:
        message = "That's a good job, my dear! Keep it up!"
        msg_color = "#5C4B7A"
    elif percentage >= 50:
        message = "Not bad, dearie — keep practicing!"
        msg_color = "#B4A7C9"
    else:
        message = "Don't give up, my dear — let's try again!"
        msg_color = "#C86B6B"
    
    tk.Label(
    	main_frame, 
    	text=message, 
    	font=("Courier", 15, "italic"),
        bg="#E6E6FA", 
        fg=msg_color).pack(pady=10)
    
    tk.Label(
    	main_frame, 
    	text="-------------------------------------", 
        font=("Courier", 11), 
        bg="#E6E6FA", 
        fg="#D4C1EC").pack(pady=15)
    
    if wrong_answers:
        tk.Label(
        	main_frame, 
        	text="You can review your answers here, my dear!:",
            font=("Courier", 14, "bold"), 
            bg="#E6E6FA", 
            fg="#5C4B7A").pack(pady=(0, 10))
        
        # Create frame which holds the text and the scrollbar
        review_frame = tk.Frame(
        	main_frame, 
        	bg="#9A94BC")
        review_frame.pack(pady=5)
        
        # Scrollbar
        review_scroll = tk.Scrollbar(review_frame)
        review_scroll.pack(side="right", fill="y")
        
        # Text box with scroll support
        review_box = tk.Text(
            review_frame,
            height=10,
            width=72,
            font=("Courier", 11),
            bg = "#FFFFFF",
            fg="#5C4B7A",
            relief="flat",
            padx=10,
            pady=10,
            yscrollcommand=review_scroll.set
        )
        review_box.pack(side="left", fill="both")
        review_scroll.config(command=review_box.yview)
        
        for number, item in enumerate(wrong_answers, start=1):
            review_box.insert("end", f"Q{number}: {item['question']}\n")
            review_box.insert("end", f"   Your answer: {item['your_answer']}\n")
            review_box.insert("end", f"   Correct:   {item['correct_answer']}\n\n")
        
        review_box.config(state="disabled")
    
    btn_frame = tk.Frame(main_frame, bg="#E6E6FA")
    btn_frame.pack(pady=20)
    
    tk.Button(btn_frame, text="PLAY AGAIN", font=("Courier", 12, "bold"),
              bg="#FFDFCC", fg="#5C4B7A", width=15, command=start_quiz,
              relief="solid", bd=0, cursor="hand2").grid(row=0, column=0, padx=10)
    tk.Button(btn_frame, text="EXIT", font=("Courier", 12, "bold"),
              bg="#E8C5C5", fg="#5C4B7A", width=15, command=exit_quiz,
              relief="solid", bd=0, cursor="hand2").grid(row=0, column=1, padx=10)

# *********** WINDOW CLOSE HANDLER ***********
def on_close():
    global pulse_job
    if pulse_job:
        root.after_cancel(pulse_job)
    stop_timer()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)

# *********** START THE QUIZ ***********
show_name_screen()
root.mainloop()
