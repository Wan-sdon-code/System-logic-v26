# System Design of Life — My Notes

## What is this project?

This project is about one simple question:

**When life doesn't go according to plan, what do you fall back on?**

It encourages people to think about life, purpose, faith and what they believe.

---

## What does my Python do?

The program is very simple:

1. Shows the project title.
2. Asks the user what they fall back on when life gets difficult.
3. Saves their answer.
4. Shows their answer back to them.
5. Gives them four questions to think about.
6. Ends with a simple message.

The program does **not** tell the user what they must believe.

It simply asks them to think about it.

---

## Simple Example

The program asks:

> **When life gets difficult, what do you fall back on?**

Someone might type:

`Family and faith`

Python saves that answer and shows:

`Your answer: Family and faith`

Then it asks the user to think about:

* Why am I here?
* What gives my life meaning?
* Do I believe in a Creator?
* What do I actually believe — and why?

---

## What does `input()` do?

`input()` lets the person using the program type an answer.

In my program:

`anchor = input(...)`

means:

**Ask the question → take the person's answer → save it as `anchor`.**

---

## What does the `f` do?

This line:

`print(f"\nYour answer: {anchor}")`

takes whatever the person typed and puts it into the sentence.

For example:

If `anchor` is:

`Family`

Python shows:

`Your answer: Family`

---

## Why did I use Python?

I wanted to turn the README idea into a small program someone can interact with.

Instead of only reading the question, the user can answer it themselves.

---

## What did I learn?

Python doesn't only have to be used for numbers and data.

It can also take information from a user and respond to what they entered.

---

## If Someone Asks Me What This Project Is

> **"It's a small reflection program that asks what you depend on when life gets difficult and gives you some questions about life, purpose and belief to think about."**
