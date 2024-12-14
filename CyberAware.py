import tkinter as tk
from tkinter import messagebox

# Quiz questions and answers, with a 'type' key for question format (text input or multiple choice)
quizData = [
    {"question": "What does 'phishing' mean?", "options": ["Fishing online", "Scamming users via fake emails", "Hacking passwords", "Blocking viruses"], "answer": 1, "type": "multiple_choice"},
    {"question": "Which of the following is a strong password?", "options": ["password123", "12345678", "Qwerty!", "P@ssw0rd!123"], "answer": 3, "type": "multiple_choice"},
    {"question": "What is a VPN?", "options": ["Virus Protection Network", "Virtual Private Network", "Visual Proxy Node", "Verified Privacy Net"], "answer": 1, "type": "multiple_choice"},
    {"question": "What should you check before clicking a link?", "options": ["The color of the link", "The domain name", "Number of characters", "The size of the page"], "answer": 1, "type": "multiple_choice"},
    {"question": "What does 2FA stand for?", "options": ["Two-Factor Authentication", "Two-Faced Access", "Twice Firewall Access", "Second-Factor Authentication"], "answer": 0, "type": "multiple_choice"},
    {"question": "Which file extension is likely malicious?", "options": [".exe", ".txt", ".jpg", ".pdf"], "answer": 0, "type": "multiple_choice"},
    {"question": "What is the main purpose of antivirus software?", "options": ["To speed up your computer", "To detect and remove malware", "To update your drivers", "To block pop-ups"], "answer": 1, "type": "multiple_choice"},
    {"question": "What should you avoid doing on public Wi-Fi?", "options": ["Streaming videos", "Logging into bank accounts", "Reading the news", "Listening to music"], "answer": 1, "type": "multiple_choice"},
    {"question": "What does SSL stand for?", "options": ["Secure Socket Layer", "Safe Surfing Link", "Secure Service Login", "System Security Lock"], "answer": 0, "type": "multiple_choice"},
    {"question": "How often should you update your passwords?", "options": ["Once a year", "Frequently", "Every few months", "Never"], "answer": 2, "type": "text_input"},
]

# Main QuizApp class that manages the overall application
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CyberAware Quiz")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        # Call the main menu method to initialize the main menu
        self.mainMenu()

    # Main Menu: Displays the start button and password checker button
    def mainMenu(self):
        # Clear any existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        # Title label
        label = tk.Label(self.root, text="CyberAware Main Menu", font=("Arial", 16))
        label.pack(pady=20)

        # Button to start quiz
        startBtn = tk.Button(self.root, text="Start Quiz", font=("Arial", 12), command=self.startQuiz)
        startBtn.pack(pady=10)

        # Button to show password checker
        passwordBtn = tk.Button(self.root, text="Password Checker", font=("Arial", 12), command=self.passwordChecker)
        passwordBtn.pack(pady=10)

        # Button to end the program
        endBtn = tk.Button(self.root, text="End Program", font=("Arial", 12), command=self.endProgram)
        endBtn.pack(pady=10)

    # Start the quiz section
    def startQuiz(self):
        # Clear the main menu and start the quiz
        for widget in self.root.winfo_children():
            widget.destroy()
        self.quizApp = Quiz(self.root)

    # Open the password checker section
    def passwordChecker(self):
        # Clear the main menu and open password checker
        for widget in self.root.winfo_children():  # Clear any existing widgets
            widget.destroy()
        self.passwordCheckerScreen()  # Open password checker screen

    # Display the password checker screen with input and a check button
    def passwordCheckerScreen(self):
        label = tk.Label(self.root, text="Enter a password to check its strength", font=("Arial", 14))
        label.pack(pady=20)

        # Entry widget to input password
        self.passwordEntry = tk.Entry(self.root, font=("Arial", 12), width=30)
        self.passwordEntry.pack(pady=10)

        checkBtn = tk.Button(self.root, text="Check Password", font=("Arial", 12), command=self.checkPasswordStrength)
        checkBtn.pack(pady=10)

        # Back button to return to the main menu
        backBtn = tk.Button(self.root, text="Back to Main Menu", font=("Arial", 12), command=self.mainMenu)
        backBtn.pack(pady=10)

    # Method to check the password strength
    def checkPasswordStrength(self):
        password = self.passwordEntry.get()  # Get the password entered
        specialCharacters = "!@#$%^&*()-_=+[]{}|;:',.<>?/`~"  # Set of special characters

        # List of common weak passwords to check against
        weakPasswords = ["password", "123456", "qwerty", "12345678", "abc123", "password123", "welcome", "letmein"]

        # Check if the password is in the list of weak passwords
        if password.lower() in weakPasswords:
            messagebox.showinfo("Password Strength", "Weak password. It's a common weak password.")
        elif len(password) < 8:
            messagebox.showinfo("Password Strength", "Weak password. It should be at least 8 characters long.")
        elif (any(char.isdigit() for char in password) and
            any(char.isalpha() for char in password) and
            any(char.isupper() for char in password) and
            any(char in specialCharacters for char in password)):
            messagebox.showinfo("Password Strength", "Strong password.")
        else:
            messagebox.showinfo("Password Strength", "Medium password. It should include a capital letter, numbers, and at least one special character.")


    # End the program and close the window
    def endProgram(self):
        # Close the tkinter window and end the program
        self.root.quit()


# Quiz class that manages the quiz functionality
class Quiz:
    def __init__(self, root):
        self.root = root
        self.currentQuestion = 0
        self.score = 0

        # Title label 
        self.titleLabel = tk.Label(root, text="CyberAware Quiz", font=("Arial", 16))
        self.titleLabel.pack(pady=10)

        # Question label 
        self.questionLabel = tk.Label(root, text="", wraplength=480, font=("Arial", 14), anchor="w", justify="left")
        self.questionLabel.pack(pady=20)

        # Frame for dynamic widgets (e.g., options or text input)
        self.dynamicFrame = tk.Frame(root)
        self.dynamicFrame.pack(pady=10)

        # Start quiz by showing the first question
        self.showQuestion()

    def showQuestion(self):
        # Get the current question data
        questionData = quizData[self.currentQuestion]
        self.questionLabel.config(text=f"Q{self.currentQuestion + 1}: {questionData['question']}")

        # Clear previous question's widgets
        for widget in self.dynamicFrame.winfo_children():
            widget.destroy()

        # Display appropriate input method for the question type
        if questionData["type"] == "multiple_choice":
            self.displayMultipleChoiceOptions(questionData)
        elif questionData["type"] == "text_input":
            self.displayTextInput()

    def displayMultipleChoiceOptions(self, questionData):
        # Create buttons for multiple-choice options
        for idx, option in enumerate(questionData["options"]):
            button = tk.Button(self.dynamicFrame, text=option, font=("Arial", 12), command=lambda idx=idx: self.checkAnswer(idx))
            button.pack(pady=5)

    def displayTextInput(self):
        # Create an entry box for text input
        self.answerEntry = tk.Entry(self.dynamicFrame, font=("Arial", 12), width=40)
        self.answerEntry.pack(pady=10)

        # Submit button for text input answer
        self.submitBtn = tk.Button(self.dynamicFrame, text="Submit Answer", font=("Arial", 12), command=self.checkTextInputAnswer)
        self.submitBtn.pack(pady=10)

    # Check if the selected answer is correct for multiple-choice questions
    def checkAnswer(self, selectedIdx):
        correct_idx = quizData[self.currentQuestion]["answer"]
        if selectedIdx == correct_idx:
            self.score += 1
        self.currentQuestion += 1
        self.nextQuestion()

    # Check the answer for text input questions
    def checkTextInputAnswer(self):
        userAnswer = self.answerEntry.get().strip().lower()
        correctAnswer = quizData[self.currentQuestion]["options"][quizData[self.currentQuestion]["answer"]].lower()

        if userAnswer == correctAnswer:
            self.score += 1  # Increase score for correct answer

        self.currentQuestion += 1
        self.nextQuestion()  # Display next question

    def nextQuestion(self):
        # Proceed to the next question or end the quiz
        if self.currentQuestion < len(quizData):
            self.showQuestion()
        else:
            self.endQuiz()

    def endQuiz(self):
        # Display the final score and return to the main menu
        for widget in self.dynamicFrame.winfo_children():
            widget.destroy()

        messagebox.showinfo("Quiz Completed", f"Your score: {self.score}/{len(quizData)}")
        backBtn = tk.Button(self.dynamicFrame, text="Back to Main Menu", font=("Arial", 12), command=self.backToMainMenu)
        backBtn.pack(pady=10)

    def backToMainMenu(self):
    # Clear all quiz-specific widgets
        for widget in self.root.winfo_children():
            widget.destroy()
    
    # Reinitialize the main menu
        QuizApp(self.root).mainMenu()


# Run the Application
root = tk.Tk()
app = QuizApp(root)
root.mainloop()
