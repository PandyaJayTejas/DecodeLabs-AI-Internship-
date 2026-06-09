# NEXUS — Rule-Based AI Chatbot 🤖

> **Practice Work 2026 | Artificial Intelligence | Project 1**  
> Developer: **Jay Pandya** | [GitHub](https://github.com/PandyaJayTejas)

---

## What is this?

NEXUS is a rule-based AI chatbot built in Python as part of the **Practice Work 2026**.  
It responds to predefined user inputs using **dictionary-based O(1) lookup** — no machine learning, no APIs, pure programmatic logic.

---

## Features

| Feature | Detail |
|---|---|
| Input Sanitization | `.lower().strip()` normalizes all input |
| Knowledge Base | 30+ intents stored in a Python dictionary |
| O(1) Lookup | `dict.get()` method — faster than if-elif chains |
| Partial Matching | Keyword scan as fallback for unrecognized input |
| Dynamic Responses | Real-time clock, randomized joke pool |
| Fallback Handler | Default reply for completely unknown input |
| Exit Strategy | Clean `break` on exit/quit/bye commands |

---

## How to Run

**Requirements:** Python 3.x (no external libraries needed)

```bash
# Clone the repo
git clone https://github.com/PandyaJayTejas/Practice-Work.git
cd Practice-Work

# Run the chatbot
python nexus_chatbot.py
```

---

## Sample Conversation

```
══════════════════════════════════════════════════════════
   NEXUS — Rule-Based AI Chatbot
   Practice Work 2026  |  Built by Jay Pandya
══════════════════════════════════════════════════════════

You    → hello
NEXUS  → Hey! NEXUS online. What's on your mind?

You    → what is ai
NEXUS  → AI stands for Artificial Intelligence — machines that simulate human thinking.

You    → tell me a joke
NEXUS  → Why do programmers prefer dark mode? Because light attracts bugs!

You    → what time is it
NEXUS  → Current system time: 09:45:12 AM

You    → motivate me
NEXUS  → Consistency beats talent every single time. Keep coding.

You    → exit
NEXUS  → Goodbye! NEXUS shutting down. See you next time.
```

---

## Architecture

```
User Input
    │
    ▼
Sanitize (lowercase + strip)
    │
    ▼
Exit Check ──── YES ──▶ Break loop
    │ NO
    ▼
Dictionary Lookup O(1)
    │
    ├── Match found ──▶ Return random reply from list
    │
    ├── No match ──▶ Keyword scan
    │                    ├── Partial match found ──▶ Return reply
    │                    └── No match ──▶ Return fallback
    ▼
Print Response → Loop
```

---

## Key Concepts Demonstrated

- **Control Flow** — `while True` loop with `break`
- **Input Sanitization** — case and whitespace normalization
- **Hash Maps** — Python `dict` for O(1) intent lookup over O(n) if-elif
- **Fallback Logic** — graceful handling of unknown inputs
- **Randomization** — varied responses to avoid repetitive output

---

## About

Built as **Project 1** of the Practice Work 2026.  
This project covers foundational AI concepts — specifically **deterministic rule-based systems** — before advancing to machine learning in later projects.

---

*"An LLM without rules is a hallucination engine. Today, we build the skeleton that holds the intelligence."*
