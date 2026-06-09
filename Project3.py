# ================================================================
#  AI QUIZ BOT — Adaptive Knowledge Testing System
#  DecodeLabs Batch 2026 | Artificial Intelligence | Project 3
#  Developer : Jay Pandya
#  GitHub    : github.com/PandyaJayTejas
#
#  Concept   : Rule-based AI that tracks performance, adapts
#              difficulty, and gives personalized feedback.
# ================================================================

import random
import time

# ── Question Bank ─────────────────────────────────────────────────
# Format: { "question": str, "options": list, "answer": int (0-3), "explanation": str, "difficulty": str }

QUESTION_BANK = {
    "ai_basics": [
        {
            "question"   : "What does AI stand for?",
            "options"    : ["Automated Interface", "Artificial Intelligence",
                            "Automated Intelligence", "Artificial Interface"],
            "answer"     : 1,
            "explanation": "AI = Artificial Intelligence — machines simulating human thinking.",
            "difficulty" : "easy",
        },
        {
            "question"   : "Which of these is an example of rule-based AI?",
            "options"    : ["ChatGPT", "A chess engine using minimax", "A calculator", "A chatbot using if-else logic"],
            "answer"     : 3,
            "difficulty" : "easy",
            "explanation": "Rule-based AI uses explicit if-else logic — exactly what you built in Project 1.",
        },
        {
            "question"   : "What is the main advantage of a rule-based system over an LLM?",
            "options"    : ["More creative responses", "Zero hallucination risk",
                            "Faster internet speed", "Works without electricity"],
            "answer"     : 1,
            "explanation": "Rule-based systems are deterministic — the output is always predictable and never hallucinated.",
            "difficulty" : "medium",
        },
        {
            "question"   : "What is the IPO model in computing?",
            "options"    : ["Internet Protocol Output", "Input-Process-Output",
                            "Internal Program Operation", "Integrated Processing Order"],
            "answer"     : 1,
            "explanation": "IPO = Input → Process → Output. It's the fundamental model for all computing systems.",
            "difficulty" : "easy",
        },
        {
            "question"   : "What Python method is used for O(1) dictionary lookup with a fallback?",
            "options"    : ["dict.find()", "dict.get()", "dict.search()", "dict.lookup()"],
            "answer"     : 1,
            "explanation": "dict.get(key, default) returns the value if key exists, else returns the default. Single atomic operation.",
            "difficulty" : "medium",
        },
    ],
    "python": [
        {
            "question"   : "Which loop runs indefinitely until a break condition is met?",
            "options"    : ["for loop", "do-while loop", "while True loop", "repeat loop"],
            "answer"     : 2,
            "explanation": "'while True' creates an infinite loop. Use 'break' to exit — the chatbot heartbeat!",
            "difficulty" : "easy",
        },
        {
            "question"   : "What does .lower().strip() do to a string?",
            "options"    : ["Uppercases and adds spaces", "Lowercases and removes whitespace",
                            "Removes all characters", "Reverses the string"],
            "answer"     : 1,
            "explanation": ".lower() converts to lowercase. .strip() removes leading/trailing whitespace. Essential for input sanitization.",
            "difficulty" : "easy",
        },
        {
            "question"   : "What is the time complexity of looking up a key in a Python dictionary?",
            "options"    : ["O(n)", "O(log n)", "O(1)", "O(n²)"],
            "answer"     : 2,
            "explanation": "Python dict uses hash maps — average O(1) lookup. Much faster than O(n) if-elif chains.",
            "difficulty" : "medium",
        },
        {
            "question"   : "Which statement exits a loop immediately?",
            "options"    : ["exit()", "stop", "return", "break"],
            "answer"     : 3,
            "explanation": "'break' immediately terminates the loop. Used as the kill command in chatbots.",
            "difficulty" : "easy",
        },
        {
            "question"   : "What does random.choice(list) do?",
            "options"    : ["Sorts the list randomly", "Returns a random element from the list",
                            "Removes a random element", "Shuffles the list in place"],
            "answer"     : 1,
            "explanation": "random.choice() picks and returns one random element. Used for varied chatbot responses.",
            "difficulty" : "easy",
        },
    ],
    "ml_concepts": [
        {
            "question"   : "What is Machine Learning?",
            "options"    : ["Programming machines with fixed rules",
                            "Systems that learn from data without explicit programming",
                            "Using machines to do mechanical work",
                            "A type of hardware component"],
            "answer"     : 1,
            "explanation": "ML systems improve their performance by learning from data — no hard-coded rules.",
            "difficulty" : "easy",
        },
        {
            "question"   : "What is the difference between rule-based AI and ML?",
            "options"    : ["There is no difference", "Rule-based uses explicit logic; ML learns from data",
                            "ML is older than rule-based AI", "Rule-based AI requires internet"],
            "answer"     : 1,
            "explanation": "Rule-based = human-defined logic. ML = patterns learned from data. Both are valid AI approaches.",
            "difficulty" : "medium",
        },
        {
            "question"   : "What is a 'hallucination' in AI?",
            "options"    : ["When AI dreams", "When AI generates false but confident information",
                            "When AI crashes", "When AI runs too fast"],
            "answer"     : 1,
            "explanation": "LLMs can generate plausible-sounding but completely wrong answers. Rule-based systems have zero hallucination risk.",
            "difficulty" : "medium",
        },
        {
            "question"   : "What is sentiment analysis?",
            "options"    : ["Detecting emotions or opinions in text",
                            "Analyzing network traffic",
                            "Measuring computer speed",
                            "Checking grammar errors"],
            "answer"     : 0,
            "explanation": "Sentiment analysis determines whether text expresses positive, negative, or neutral sentiment.",
            "difficulty" : "easy",
        },
        {
            "question"   : "In NLP, what does 'tokenization' mean?",
            "options"    : ["Encrypting text", "Splitting text into individual words or tokens",
                            "Translating text to another language", "Compressing text"],
            "answer"     : 1,
            "explanation": "Tokenization splits raw text into words/tokens — the first step in any text processing pipeline.",
            "difficulty" : "medium",
        },
    ],
}

# ── Feedback Rules ────────────────────────────────────────────────
FEEDBACK = {
    "correct"  : ["Correct! ✅", "Nailed it! ✅", "Exactly right! ✅", "Perfect! ✅"],
    "wrong"    : ["Not quite. ❌", "Incorrect. ❌", "That's wrong. ❌", "Nope. ❌"],
    "perfect"  : ["PERFECT SCORE! 🏆 You're an AI Engineer in the making.",
                  "100%! 🏆 Outstanding performance."],
    "excellent": ["Excellent! 🥇 You have a strong grasp of AI concepts.",
                  "Great work! 🥇 Very impressive score."],
    "good"     : ["Good job! 🥈 Solid performance. Review the explanations you missed.",
                  "Well done! 🥈 Keep studying and you'll be perfect next time."],
    "average"  : ["Not bad. 🥉 But there's room to improve. Go through the concepts again.",
                  "Average score. 🥉 Keep practicing — consistency beats talent."],
    "low"      : ["Keep going. 📚 This is just the beginning. Review the material and retry.",
                  "Don't give up. 📚 Every expert was once a beginner."],
}


# ── Quiz Engine ───────────────────────────────────────────────────

class QuizBot:

    def __init__(self):
        self.score         = 0
        self.total         = 0
        self.wrong_answers = []
        self.start_time    = None

    def display_question(self, q_data: dict, q_num: int):
        """Print a formatted question."""
        print(f"\n{'─'*55}")
        print(f"  Q{q_num}. {q_data['question']}")
        print(f"  [{q_data['difficulty'].upper()}]")
        print(f"{'─'*55}")
        for i, opt in enumerate(q_data["options"]):
            print(f"  {i + 1}. {opt}")

    def get_answer(self, max_options: int) -> int:
        """Get and validate user's answer (1-indexed input → 0-indexed)."""
        while True:
            try:
                raw = input(f"\n  Your answer (1-{max_options}): ").strip()
                if raw.lower() in {"exit", "quit", "q"}:
                    return -1
                choice = int(raw) - 1
                if 0 <= choice < max_options:
                    return choice
                print(f"  ⚠  Please enter a number between 1 and {max_options}.")
            except ValueError:
                print("  ⚠  Enter a number only.")

    def run_quiz(self, topic: str, questions: list):
        """Run a quiz on the selected topic."""
        random.shuffle(questions)

        print(f"\n{'═'*55}")
        print(f"   TOPIC: {topic.upper().replace('_', ' ')}")
        print(f"   Questions: {len(questions)}")
        print(f"{'═'*55}")
        print("  Type 'exit' at any answer prompt to quit early.\n")

        self.start_time = time.time()

        for i, q in enumerate(questions, 1):
            self.display_question(q, i)
            choice = self.get_answer(len(q["options"]))

            if choice == -1:
                print("\n  Quiz exited early.")
                break

            self.total += 1

            if choice == q["answer"]:
                self.score += 1
                print(f"\n  {random.choice(FEEDBACK['correct'])}")
            else:
                correct_text = q["options"][q["answer"]]
                print(f"\n  {random.choice(FEEDBACK['wrong'])}")
                print(f"  Correct answer: {q['answer'] + 1}. {correct_text}")
                self.wrong_answers.append(q)

            print(f"  💡 {q['explanation']}")
            time.sleep(0.5)

    def show_results(self):
        """Display final score and personalized feedback."""
        elapsed = round(time.time() - self.start_time, 1) if self.start_time else 0
        pct     = round(self.score / self.total * 100) if self.total else 0

        print(f"\n{'═'*55}")
        print(f"   QUIZ COMPLETE")
        print(f"{'═'*55}")
        print(f"   Score      : {self.score}/{self.total}  ({pct}%)")
        print(f"   Time taken : {elapsed}s")

        # Visual bar
        filled  = int(pct / 10)
        bar     = "█" * filled + "░" * (10 - filled)
        print(f"   Progress   : [{bar}] {pct}%")

        # Feedback
        if pct == 100:
            fb = random.choice(FEEDBACK["perfect"])
        elif pct >= 80:
            fb = random.choice(FEEDBACK["excellent"])
        elif pct >= 60:
            fb = random.choice(FEEDBACK["good"])
        elif pct >= 40:
            fb = random.choice(FEEDBACK["average"])
        else:
            fb = random.choice(FEEDBACK["low"])

        print(f"\n   {fb}")

        # Review wrong answers
        if self.wrong_answers:
            print(f"\n   Review ({len(self.wrong_answers)} missed):")
            for q in self.wrong_answers:
                print(f"   • {q['question']}")
                print(f"     → {q['options'][q['answer']]}")
        print(f"{'═'*55}\n")


# ── Main Menu ─────────────────────────────────────────────────────

def select_topic() -> tuple:
    """Show topic menu and return (topic_key, questions)."""
    topics = list(QUESTION_BANK.keys())
    labels = {
        "ai_basics"  : "AI Fundamentals & Rule-Based Systems",
        "python"     : "Python Programming",
        "ml_concepts": "Machine Learning Concepts",
    }

    print("\n  SELECT TOPIC:")
    print("  ─────────────────────────────────────")
    for i, key in enumerate(topics, 1):
        count = len(QUESTION_BANK[key])
        print(f"  {i}. {labels[key]}  [{count} questions]")
    print("  4. ALL TOPICS  (mixed)")
    print("  ─────────────────────────────────────")

    while True:
        try:
            choice = input("  Your choice (1-4): ").strip()
            c = int(choice)
            if c == 4:
                all_q = [q for qs in QUESTION_BANK.values() for q in qs]
                return "All Topics", all_q
            if 1 <= c <= len(topics):
                key = topics[c - 1]
                return labels[key], QUESTION_BANK[key]
            print("  ⚠  Choose between 1 and 4.")
        except ValueError:
            print("  ⚠  Enter a number.")


def main():
    print("\n" + "═" * 55)
    print("   AI QUIZ BOT 🤖")
    print("   DecodeLabs Batch 2026  |  Built by Jay Pandya")
    print("═" * 55)

    while True:
        topic, questions = select_topic()
        bot = QuizBot()
        bot.run_quiz(topic, list(questions))
        bot.show_results()

        again = input("  Play again? (yes / no): ").strip().lower()
        if again not in {"yes", "y"}:
            print("  Thanks for using AI Quiz Bot. Keep learning! 🚀\n")
            break


if __name__ == "__main__":
    main()
