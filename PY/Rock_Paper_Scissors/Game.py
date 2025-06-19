import tkinter as tk
import random

class RockPaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎮 Rock-Paper-Scissors")
        self.root.geometry("400x500")
        self.root.configure(bg="#f8f9fa")

        self.choices = ["Rock", "Paper", "Scissors"]
        self.user_score = 0
        self.computer_score = 0

        self.setup_ui()

    def setup_ui(self):
        tk.Label(
            self.root,
            text="Rock, Paper, Scissors",
            font=("Segoe UI", 18, "bold"),
            bg="#f8f9fa",
            fg="#343a40"
        ).pack(pady=20)

        self.result_label = tk.Label(
            self.root,
            text="Make your choice!",
            font=("Segoe UI", 14),
            bg="#f8f9fa",
            fg="#495057"
        )
        self.result_label.pack(pady=10)

        button_frame = tk.Frame(self.root, bg="#f8f9fa")
        button_frame.pack(pady=10)

        for choice in self.choices:
            tk.Button(
                button_frame,
                text=choice,
                font=("Segoe UI", 12),
                width=10,
                height=2,
                bg="#007bff",
                fg="white",
                activebackground="#0056b3",
                relief="raised",
                bd=2,
                command=lambda c=choice: self.play_round(c)
            ).pack(side="left", padx=10)

        self.score_label = tk.Label(
            self.root,
            text="Your Score: 0  |  Computer Score: 0",
            font=("Segoe UI", 12),
            bg="#f8f9fa",
            fg="#212529"
        )
        self.score_label.pack(pady=20)

        self.user_choice_label = tk.Label(
            self.root,
            text="Your Choice: ",
            font=("Segoe UI", 11),
            bg="#f8f9fa"
        )
        self.user_choice_label.pack()

        self.computer_choice_label = tk.Label(
            self.root,
            text="Computer's Choice: ",
            font=("Segoe UI", 11),
            bg="#f8f9fa"
        )
        self.computer_choice_label.pack()

        tk.Button(
            self.root,
            text="Play Again",
            font=("Segoe UI", 11),
            bg="#28a745",
            fg="white",
            width=15,
            height=2,
            command=self.reset_game
        ).pack(pady=10)

        tk.Button(
            self.root,
            text="Exit",
            font=("Segoe UI", 11),
            bg="#dc3545",
            fg="white",
            width=15,
            height=2,
            command=self.root.quit
        ).pack(pady=5)

    def play_round(self, user_choice):
        computer_choice = random.choice(self.choices)
        result = self.get_winner(user_choice, computer_choice)

        self.user_choice_label.config(text=f"Your Choice: {user_choice}")
        self.computer_choice_label.config(text=f"Computer's Choice: {computer_choice}")

        if result == "win":
            self.result_label.config(text="🎉 You Win!", fg="#28a745")
            self.user_score += 1
        elif result == "lose":
            self.result_label.config(text="😞 You Lose!", fg="#dc3545")
            self.computer_score += 1
        else:
            self.result_label.config(text="😐 It's a Tie!", fg="#6c757d")

        self.score_label.config(
            text=f"Your Score: {self.user_score}  |  Computer Score: {self.computer_score}"
        )

    def get_winner(self, user, computer):
        if user == computer:
            return "tie"
        if (
            (user == "Rock" and computer == "Scissors") or
            (user == "Paper" and computer == "Rock") or
            (user == "Scissors" and computer == "Paper")
        ):
            return "win"
        return "lose"

    def reset_game(self):
        self.result_label.config(text="Make your choice!", fg="#495057")
        self.user_choice_label.config(text="Your Choice: ")
        self.computer_choice_label.config(text="Computer's Choice: ")

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsApp(root)
    root.mainloop()
