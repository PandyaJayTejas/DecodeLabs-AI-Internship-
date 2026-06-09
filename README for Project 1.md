# Sentiment Analyzer 📊

A Python-based sentiment analysis tool that determines whether a piece of text expresses a positive, negative, or neutral opinion. Instead of using machine learning, it relies on weighted keyword scoring and smart negation handling to analyze sentiment quickly and accurately.

This project was developed as **Project 2** for the **Artificial Intelligence Track** at **DecodeLabs Batch 2026**.

---

## ⚡ Features

### Weighted Sentiment Scoring

Assigns different weights to sentiment words. Strong words such as *excellent* and *terrible* have a higher impact than standard words like *good* and *bad*.

### Negation Detection

Recognizes negating words such as *not*, *never*, and *didn't*, then reverses the sentiment of the following word.

**Example:**

* "good" → Positive
* "not good" → Negative

### Confidence Score

Calculates a confidence percentage based on how strongly positive or negative the detected sentiment is.

### Detailed Sentiment Categories

Classifies text into six categories:

* Strongly Positive
* Positive
* Mixed
* Neutral
* Negative
* Strongly Negative

### Batch Analysis Mode

Analyze multiple predefined text samples at once and generate a summary report.

### Visual Command-Line Output

Displays results in a clean, easy-to-read format with text-based bar charts using block characters (`█`).

---

## 🛠️ Tech Stack

* **Language:** Python 3
* **Libraries Used:**

  * `re` (Regular Expressions)
  * `time` (Standard Library)
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

2. Open the project directory:

```bash
cd your-repo-name
```

3. Run the program:

```bash
python Project1.py
```

---

## 💬 Example Output

```text
═══════════════════════════════════════════════════════
   SENTIMENT ANALYZER
   DecodeLabs Batch 2026 | Built by Jay Pandya
═══════════════════════════════════════════════════════

Enter text →
I hate slow internet but I love this new router,
it is fast and brilliant.

───────────────────────────────────────────────────────
Sentiment : POSITIVE 🟡
Net Score : +1
Confidence: 20.0%

Positive  : ████ (+4)
Negative  : ███ (-3)

+ Words   : love, fast, brilliant
- Words   : hate, slow
───────────────────────────────────────────────────────
```

---

## 🧠 How It Works

The analysis process follows four simple steps:

1. **Text Cleaning**

   * Converts text to lowercase
   * Removes punctuation using regular expressions
   * Splits text into individual words

2. **Keyword Matching**

   * Compares each word against predefined positive and negative dictionaries

3. **Negation Handling**

   * Checks whether a negation word appears before a sentiment word
   * Reverses the sentiment when necessary

4. **Score Calculation**

   * Calculates positive and negative scores
   * Determines the final sentiment category
   * Computes a confidence percentage
