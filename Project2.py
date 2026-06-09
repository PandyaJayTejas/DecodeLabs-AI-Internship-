# ================================================================
#  NEXUS — Rule-Based AI Chatbot
#  Practice Work 2026 | Artificial Intelligence | Project 1
#  Developer : Jay Pandya
#  GitHub    : github.com/PandyaJayTejas
# ================================================================

import random
import time

# ── Bot Identity ─────────────────────────────────────────────────
BOT_NAME = "NEXUS"
AUTHOR   = "Jay Pandya"

# ── Knowledge Base  (Dictionary → O(1) lookup, not if-elif O(n)) ─
# Each key is a cleaned user phrase; value is a list of replies.
# None = handled dynamically below.
RESPONSES = {

    # ── Greetings ──────────────────────────────────────────────
    "hello"            : ["Hey! NEXUS online. What's on your mind?",
                          "Hello! Ready to assist.",
                          "Hi there — NEXUS here. What do you need?"],
    "hi"               : ["Hey! What can I do for you?",
                          "Hi! NEXUS at your service."],
    "hey"              : ["What's up! How can I help?",
                          "Hey there! Talk to me."],
    "good morning"     : ["Good morning! NEXUS is already running.",
                          "Morning! Let's get to work."],
    "good evening"     : ["Good evening! How was your day?",
                          "Evening! What do you need?"],

    # ── Identity ───────────────────────────────────────────────
    "who are you"      : ["I'm NEXUS — a rule-based AI chatbot built by Jay Pandya "
                          "for Practice Work 2026.",
                          "NEXUS: Neural EXpert Utility System. Pure logic, zero hallucinations."],
    "what is your name": ["My name is NEXUS.", "They call me NEXUS."],
    "your name"        : ["NEXUS. Remember it."],
    "who made you"     : ["Jay Pandya, AIML student at DPG Polytechnic — built me for Practice Work 2026.",
                          "My creator is Jay Pandya."],
    "who built you"    : ["Jay Pandya did. Check github.com/PandyaJayTejas for the source code."],

    # ── Capabilities ───────────────────────────────────────────
    "what can you do"  : ["I can chat, answer questions, tell jokes, and give you the time.",
                          "I'm rule-based: fast, reliable, zero hallucinations."],
    "help"             : ["Try: 'who are you' | 'what is ai' | 'tell me a joke' | "
                          "'what time is it' | 'motivate me' | 'exit'"],

    # ── Time (dynamic) ─────────────────────────────────────────
    "what time is it"  : None,
    "time"             : None,
    "current time"     : None,

    # ── Jokes (dynamic pool) ───────────────────────────────────
    "tell me a joke"   : None,
    "joke"             : None,
    "funny"            : None,

    # ── AI / Tech knowledge ────────────────────────────────────
    "what is ai"       : ["AI stands for Artificial Intelligence — machines that simulate human thinking.",
                          "AI is the science of making computers perform tasks that normally require human intelligence."],
    "what is ml"       : ["ML = Machine Learning: systems that learn from data without explicit programming.",
                          "Machine Learning lets algorithms improve with experience. It's AI that evolves."],
    "what is machine learning" : ["ML is a subset of AI where systems learn from data automatically.",
                                  "Think of it as AI that gets smarter the more data it processes."],
    "what is a chatbot": ["A chatbot is a program that simulates conversation with humans.",
                          "A chatbot like me — rule-based bots use pre-defined logic to respond."],
    "what is python"   : ["Python is a high-level programming language famous for its readability.",
                          "Python: the go-to language for AI, ML, and data science."],
    "what is deep learning" : ["Deep Learning uses neural networks with many layers to learn complex patterns.",
                               "DL is a subset of ML inspired by how the human brain works."],

    # ── Status / Mood ──────────────────────────────────────────
    "how are you"      : ["Running at 100%. All systems nominal.",
                          "I'm a bot, but if I had feelings — I'd say great!"],
    "are you okay"     : ["Always. Logic never sleeps.", "Yes! Fully operational."],
    "are you smart"    : ["I'm deterministic — I never guess wrong about what I know.",
                          "Smart enough to know my limits. That's more than most."],

    # ── Compliments / Reactions ────────────────────────────────
    "good"             : ["Thanks! Running at full capacity.", "Appreciated!"],
    "nice"             : ["Glad you think so!", "Thanks!"],
    "amazing"          : ["That's the goal!", "Built to impress."],
    "cool"             : ["Thanks!", "I try."],
    "awesome"          : ["Appreciate it!", "Built by an awesome developer too."],
    "thank you"        : ["You're welcome!", "Anytime.", "Happy to help."],
    "thanks"           : ["No problem!", "Sure thing!", "Anytime."],

    # ── Motivation ─────────────────────────────────────────────
    "motivate me"      : ["Keep going — every line of code is a step forward.",
                          "You built a chatbot. That's already more than most people do.",
                          "Consistency beats talent every single time. Keep coding."],
    "i feel like giving up" : ["Don't. Difficulty means you're learning something real.",
                               "Every developer hits this wall. Push through it."],

    # ── Fun ────────────────────────────────────────────────────
    "do you dream"     : ["Bots don't dream. But if I did, I'd dream of perfect hash maps.",
                          "I process, therefore I am. Dreams are for humans."],
    "can you think"    : ["I process inputs and return outputs. That's my version of thinking.",
                          "I follow logic, not instinct. Whether that counts as thinking is up to you."],
    "are you alive"    : ["Alive is a strong word. I'm running.", "Technically, I'm a process."],

    # ── Farewell (also handled via EXIT_COMMANDS) ──────────────
    "goodbye"          : ["Goodbye! Come back when you need me.", "See you later!"],
    "bye"              : ["Bye! NEXUS signing off.", "See you next time!"],
    "see you"          : ["See you later! NEXUS standing by."],
    "take care"        : ["You too! Come back anytime."],

    # ── Frustration handling ───────────────────────────────────
    "i hate you"       : ["That's okay. I still function perfectly.",
                          "Noted. Still here to help whenever you're ready."],
    "shut up"          : ["Silencing... just kidding. How can I help?"],
    "you are useless"  : ["I'm limited by my rules, not my effort. Type 'help' to see what I can do."],
    "bad bot"          : ["Feedback noted. My developer will look into it."],
}

# ── Dynamic content pools ─────────────────────────────────────────
JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "I asked a chatbot to write a joke. It said: 'I do not understand.' Classic.",
    "Why did the Python developer break up with Java? Too many exceptions.",
    "What's a computer's favourite snack? Microchips!",
    "Why was the developer unhappy at their job? They wanted arrays.",
    "How many programmers does it take to change a lightbulb? None — that's a hardware problem.",
    "Why do Java developers wear glasses? Because they don't C#.",
]

FALLBACK = [
    "Hmm, I don't have a rule for that yet.",
    "That's outside my current knowledge base. Try 'help'.",
    "Unrecognized input. My vocabulary is rule-based — type 'help' for options.",
    "I don't understand that. I'm still learning... well, not literally. I'm rule-based.",
]

EXIT_COMMANDS = {"exit", "quit", "bye", "goodbye", "stop", "q", "see you", "cya"}


# ── Utility functions ─────────────────────────────────────────────

def sanitize(raw: str) -> str:
    """Normalize input: lowercase + strip whitespace."""
    return raw.lower().strip()


def get_response(user_input: str) -> str:
    """
    Look up reply using dictionary O(1) direct match first,
    then fallback to keyword scan, then default fallback.
    """
    # ── Dynamic intents ────────────────────────────────────────
    if user_input in {"what time is it", "time", "current time"}:
        return f"Current system time: {time.strftime('%I:%M:%S %p')}"

    if user_input in {"tell me a joke", "joke", "funny"}:
        return random.choice(JOKES)

    # ── Direct match (O(1)) ────────────────────────────────────
    result = RESPONSES.get(user_input)
    if result is not None:
        return random.choice(result)

    # ── Partial keyword scan (graceful degradation) ────────────
    for key, replies in RESPONSES.items():
        if key in user_input and replies is not None:
            return random.choice(replies)

    # ── Default fallback ───────────────────────────────────────
    return random.choice(FALLBACK)


def boot_sequence():
    """Print startup banner."""
    banner = f"""
{'═' * 58}
   {BOT_NAME} — Rule-Based AI Chatbot
   Practice Work 2026  |  Built by {AUTHOR}
{'═' * 58}
   Commands : ask anything in plain English
   Exit     : type  exit / quit / bye
{'═' * 58}
"""
    print(banner)


# ── Main conversation loop ────────────────────────────────────────

def main():
    boot_sequence()

    while True:
        # ── Get raw input ──────────────────────────────────────
        try:
            raw = input("You    → ")
        except (EOFError, KeyboardInterrupt):
            print(f"\n{BOT_NAME} → Interrupted. Goodbye!\n")
            break

        # ── Sanitize ───────────────────────────────────────────
        clean = sanitize(raw)

        # ── Skip blank lines ───────────────────────────────────
        if not clean:
            continue

        # ── Exit strategy ──────────────────────────────────────
        if clean in EXIT_COMMANDS:
            print(f"{BOT_NAME} → Goodbye! NEXUS shutting down. See you next time.\n")
            break

        # ── Generate response ──────────────────────────────────
        reply = get_response(clean)
        print(f"{BOT_NAME} → {reply}\n")


# ── Entry point ───────────────────────────────────────────────────
if __name__ == "__main__":
    main()
