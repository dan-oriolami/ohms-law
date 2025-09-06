from tkinter import Tk, Label, Button, Radiobutton, StringVar

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mixed Format Quiz")
        self.root.geometry("500x300")

        # Mixed questions: some multiple choice, some true/false
        self.questions = [
            {"type": "mcq", "question": "What is the capital of France?",
             "options": ["London", "Berlin", "Paris", "Rome"], "answer": "Paris"},
            {"type": "tf", "question": "The sun rises in the west.",
             "options": ["True", "False"], "answer": "False"},
            {"type": "tf", "question": "Python is a programming language.",
             "options": ["True", "False"], "answer": "True"},
            {"type": "mcq", "question": "Which is a mammal?",
             "options": ["Shark", "Eagle", "Whale", "Frog"], "answer": "Whale"},
            # Add more questions as needed up to 20
        ]

        while len(self.questions) < 20:
            i = len(self.questions) + 1
            self.questions.append({
                "type": "tf" if i % 2 == 0 else "mcq",
                "question": f"Sample question {i}?",
                "options": ["True", "False"] if i % 2 == 0 else ["Option A", "Option B", "Option C", "Option D"],
                "answer": "True" if i % 2 == 0 else "Option A"
            })

        self.q_index = 0
        self.score = 0
        self.var = StringVar()

        self.question_label = Label(root, text="", wraplength=400, font=('Arial', 12))
        self.question_label.pack(pady=10)

        self.option_buttons = []
        for i in range(4):  # enough for both T/F and MCQ
            rb = Radiobutton(root, text="", variable=self.var, value="", font=('Arial', 10))
            rb.pack(anchor="w")
            self.option_buttons.append(rb)

        self.next_button = Button(root, text="Next", command=self.next_question)
        self.next_button.pack(pady=10)

        self.display_question()

    def display_question(self):
        q = self.questions[self.q_index]
        self.var.set(None)
        self.question_label.config(text=f"Q{self.q_index+1}: {q['question']}")
        for i in range(4):
            if i < len(q['options']):
                self.option_buttons[i].config(text=q['options'][i], value=q['options'][i])
                self.option_buttons[i].pack(anchor="w")
            else:
                self.option_buttons[i].pack_forget()

    def next_question(self):
        selected = self.var.get()
        if selected == self.questions[self.q_index]['answer']:
            self.score += 1
        self.q_index += 1
        if self.q_index < len(self.questions):
            self.display_question()
        else:
            self.show_result()

    def show_result(self):
        self.question_label.config(text=f"Quiz Completed!\nYou scored {self.score} out of {len(self.questions)}")
        for btn in self.option_buttons:
            btn.pack_forget()
        self.next_button.pack_forget()

root = Tk()
app = QuizApp(root)
root.mainloop()
