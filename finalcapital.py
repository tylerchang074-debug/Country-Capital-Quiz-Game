import random
import tkinter as tk

root = tk.Tk()    
root.title("Capital Quiz")
root.geometry("600x450") 

questionno = 0

introduction = tk.Label(root, text="Welcome to the capital guessing game!", font=("Arial", 20), fg="black")
introduction.pack(pady=10)

diff_frame = tk.Frame(root)
diff_frame.pack()

quiz_frame = tk.Frame(root)

result_frame = tk.Frame(root)

easy_diff_btn = tk.Button(diff_frame, text="Easy", command=lambda: set_difficulty("easy"))
easy_diff_btn.pack(pady=10)

med_diff_btn = tk.Button(diff_frame, text="Medium", command=lambda: set_difficulty("medium"))
med_diff_btn.pack(pady=10)

hard_diff_btn = tk.Button(diff_frame, text="Hard", command=lambda: set_difficulty("hard"))
hard_diff_btn.pack(pady=10)

def play_again():
    global diff_frame, quiz_frame, result_frame, score, questionno
    result_frame.pack_forget()
    diff_frame.pack()
    submit_btn.config(text="Submit", command=check_answer)
    score = 0
    questionno = 0

def see_results():
    global quiz_frame, result_frame
    for widget in result_frame.winfo_children():
        widget.destroy()
    quiz_frame.pack_forget()
    result_frame.pack()
    final_score_label = tk.Label(result_frame, text="", font=("Arial", 14), fg="black")
    final_score_label.pack(pady=20)
    results_label = tk.Label(result_frame, text="", font=("Arial", 14), fg="black")
    results_label.pack(pady=25)
    play_again_btn = tk.Button(result_frame, text="Play Again", command=play_again)
    play_again_btn.pack(pady=10)
    if score == len(questions_list):
        final_score_label.configure(text=f"Wow your final score was {score}/{len(questions_list)}")
        results_label.configure(text="Thats pretty good!")
    elif score <= len(questions_list):
        final_score_label.configure(text=f"Your final score was {score}/{len(questions_list)}")
        results_label.configure(text=f"You suck how'd you not get a {len(questions_list)}")

def set_difficulty(difficulty):
    global questions, questions_list, questionno, score, question_answer
    if difficulty == "easy":
        questions = {"What is the captial of France?": "paris", 
                "What is the captial of Germany?": "berlin", 
                "What is the captial of Italy?": "rome", 
                "What is the captial of Spain?": "madrid", 
                "What is the captial of Portugal?": "lisbon"}
    elif difficulty == "medium":
        questions = {"What is the captial of malta?": "valletta", 
                "What is the captial of Panama?": "panama city", 
                "What is the captial of Brazil?": "brasilia", 
                "What is the captial of Argentina?": "buenos aires", 
                "What is the captial of Papua New Guinea?": "port moresby"}
    elif difficulty == "hard":
        questions = {"What is the captial of Solomon Islands?": "honiara", 
                "What is the captial of Cape Verde?": "cape verde city", 
                "What is the captial of Antigua and Barbuda?": "st. john's", 
                "What is the captial of Bhutan?": "thimphu", 
                "What is the captial of Kiribati?": "tarawa"}
    questions_list = list(questions.items())
    random.shuffle(questions_list)
    questionno = 0
    score = 0
    question_answer = questions_list[0][1]
    question_label.config(text=questions_list[0][0])
    result_label.config(text="")
    diff_frame.pack_forget()
    quiz_frame.pack()



def check_answer():
    global questionno, score, question_answer, answer_entry, question_label, submit_btn, result_label
    if questionno == 0:
        introduction.destroy()
    guess = answer_entry.get().lower().strip()
    if guess == question_answer.lower():
        result_label.config(text="You got it right!", fg="green")
        score += 1
    else:
        result_label.config(text=f"You got it wrong the correct answer was {question_answer}", fg="red")
    answer_entry.delete(0, tk.END)

    questionno += 1
    if questionno < len(questions_list):
        question_label.config(text=questions_list[questionno][0])
        question_answer = questions_list[questionno][1]
        progress_label.config(text=f"Question {questionno+1} of {len(questions_list)}")
    else:
        submit_btn.config(text="Click here to see your result!", command=see_results)


def give_hint():
    global score
    result_label.config(text=f"Hint: starts with '{question_answer[0]}'")
    score -= 1

hint_btn = tk.Button(quiz_frame, text="Hint (-1)", command=give_hint)
hint_btn.pack()
        
progress_label = tk.Label(quiz_frame, text="", font=("Arial", 10))
progress_label.pack()

question_label = tk.Label(quiz_frame, text="", font=("Arial", 14), fg="black")
question_label.pack(pady=20)

answer_entry = tk.Entry(quiz_frame, font=("Arial", 12))
answer_entry.pack(pady=10)

result_label = tk.Label(quiz_frame, text="", font=("Arial", 12), fg="black")
result_label.pack(pady=10)

submit_btn = tk.Button(quiz_frame, text="Submit", command=check_answer)
submit_btn.pack(pady=10)
answer_entry.bind("<Return>", lambda event: check_answer())

root.mainloop() 