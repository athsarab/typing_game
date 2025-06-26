import tkinter as tk
import time
import random

# Sentences to choose from
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Typing games help improve your speed.",
    "Python is a great programming language.",
    "Always practice to become better.",
    "Never give up on your goals."
]

# Initialize global variables
start_time = 0
current_sentence = ""

# Save results to a file
def save_results(wpm, accuracy):
    with open("typing_results.txt", "a") as file:
        file.write(f"WPM: {wpm:.2f}, Accuracy: {accuracy:.2f}%\n")

# Start the countdown before showing sentence
def start_countdown(count=3):
    input_box.delete(0, tk.END)
    feedback_label.config(text="")
    input_box.config(state="disabled")
    countdown_label.config(text=f"⏳ Starting in {count}...")
    if count > 0:
        root.after(1000, start_countdown, count - 1)
    else:
        show_sentence()

# Show random sentence
def show_sentence():
    global start_time, current_sentence
    current_sentence = random.choice(sentences)
    sentence_label.config(text=current_sentence)
    countdown_label.config(text="Go!")
    input_box.config(state="normal")
    input_box.focus()
    start_time = time.time()

# Check result
def check_result():
    global current_sentence
    typed = input_box.get()
    end_time = time.time()
    time_taken = end_time - start_time

    words = len(typed.split())
    wpm = (words / time_taken) * 60 if time_taken > 0 else 0

    correct_chars = sum(1 for i in range(min(len(current_sentence), len(typed))) if current_sentence[i] == typed[i])
    accuracy = (correct_chars / len(current_sentence)) * 100

    result_label.config(
        text=f"⏱ Time: {time_taken:.2f}s  🖋 WPM: {wpm:.2f}  ✅ Accuracy: {accuracy:.2f}%"
    )

    # Feedback
    if accuracy > 90:
        feedback = "🎉 Great job!"
    elif accuracy > 70:
        feedback = "👍 Good effort!"
    else:
        feedback = "🤔 Try again!"

    feedback_label.config(text=feedback)
    save_results(wpm, accuracy)
    input_box.config(state="disabled")

# Restart the game
def try_again():
    input_box.delete(0, tk.END)
    result_label.config(text="")
    feedback_label.config(text="")
    start_countdown()

# Set up main window
root = tk.Tk()
root.title("Typing Speed Test Game")
root.geometry("600x400")
root.config(bg="#f5f5f5")

# Sentence display
sentence_label = tk.Label(root, text="", font=("Helvetica", 16), wraplength=580, bg="#f5f5f5")
sentence_label.pack(pady=20)

# Countdown
countdown_label = tk.Label(root, text="", font=("Helvetica", 14), fg="blue", bg="#f5f5f5")
countdown_label.pack()

# Input box
input_box = tk.Entry(root, font=("Helvetica", 14), width=50)
input_box.pack(pady=10)

# Submit button
submit_button = tk.Button(root, text="✅ Submit", font=("Helvetica", 12), command=check_result, bg="green", fg="white")
submit_button.pack(pady=5)

# Result display
result_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#f5f5f5")
result_label.pack(pady=10)

# Feedback label
feedback_label = tk.Label(root, text="", font=("Helvetica", 14, "italic"), fg="purple", bg="#f5f5f5")
feedback_label.pack(pady=5)

# Try again button
retry_button = tk.Button(root, text="🔁 Try Again", font=("Helvetica", 12), command=try_again, bg="orange")
retry_button.pack(pady=10)

# Start the game for the first time
start_countdown()

# Run app
root.mainloop()
