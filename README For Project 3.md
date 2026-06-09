# AI Quiz Bot 🤖🧠

An interactive terminal-based quiz application built with Python. The AI Quiz Bot helps users test their knowledge across multiple topics while providing instant explanations, performance tracking, and personalized feedback to support learning.

This project was developed as **Project 3** for the **Artificial Intelligence Track** at **Practice Work 2026**.

---

## ⚡ Features

### Multiple Quiz Categories

Choose from different topics:

* AI Fundamentals & Rule-Based Systems
* Python Programming
* Machine Learning Concepts
* All Topics (Mixed Quiz)

### Instant Answer Explanations

Receive detailed explanations immediately after each question to strengthen understanding and reinforce key concepts.

### Performance Tracking

Tracks:

* Quiz score
* Time taken
* Incorrect answers

### Personalized Feedback

Provides customized feedback based on your final score, ranging from beginner-level encouragement to perfect-score recognition.

### Review Missed Questions

At the end of the quiz, the bot generates a review section containing all incorrectly answered questions and their explanations.

### Visual Command-Line Interface

Features a clean terminal layout with progress indicators and visual progress bars using block characters (`████░░░░░░`).

---

## 🛠️ Tech Stack

* **Language:** Python 3
* **Libraries Used:**

  * `random`
  * `time`
* **External Dependencies:** None

---

## 🚀 Getting Started

### Prerequisites

Make sure Python is installed:

```bash
python --version
```

### Installation

1. Clone the repository:

```bash
git clone https://github.com/PandyaJayTejas/your-repo-name.git
```

2. Navigate to the project folder:

```bash
cd your-repo-name
```

3. Run the application:

```bash
python Project3.py
```

---

## 💬 Example Output

```text
═══════════════════════════════════════════════════════
   AI QUIZ BOT 🤖
   Practice Work 2026 | Built by Jay Pandya
═══════════════════════════════════════════════════════

SELECT TOPIC:

1. AI Fundamentals & Rule-Based Systems
2. Python Programming
3. Machine Learning Concepts
4. All Topics

Your choice: 2

Q1. What does random.choice(list) do?

1. Sorts the list randomly
2. Returns a random element from the list
3. Removes a random element
4. Shuffles the list in place

Your answer: 2

Correct! ✅

💡 random.choice() selects and returns a random element from a list.
```

---

## 🧠 How It Works

The application is built using an object-oriented `QuizBot` class and a structured `QUESTION_BANK`.

### 1. Topic Selection

Users select a quiz category, and the corresponding questions are loaded from the question bank.

### 2. Quiz Execution

The quiz engine:

* Randomizes question order
* Displays questions and options
* Validates user input
* Supports early exit commands

### 3. Answer Evaluation

Each response is compared with the correct answer.

The system:

* Updates the score
* Displays explanations
* Records incorrect answers for review

### 4. Result Generation

After the quiz is completed, the bot:

* Calculates the final percentage
* Generates personalized feedback
* Displays performance statistics
* Shows a review sheet of missed questions

---

## 🎯 Learning Objectives

This project demonstrates:

* Object-Oriented Programming (OOP)
* Dictionary and List Data Structures
* User Input Validation
* Randomization Techniques
* Performance Tracking
* Command-Line Interface Design
