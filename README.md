# in-numri

 *in-numri bil-Malti, Maltese numbers*

This is a terminal-based Python 3 script for learning Maltese numbers through guided practice and quizzes.

[![CodeQL](https://github.com/sambork/in-numri/actions/workflows/github-code-scanning/codeql/badge.svg?branch=main)](https://github.com/sambork/in-numri/actions/workflows/github-code-scanning/codeql)

## How it works

The script greets the learner, asks for their name, and then introduces Maltese number-word pairs in two stages: 1–10 and 11–20. For each stage, it first shows the numbers, then asks the learner to type the Maltese word, and finally runs a quiz to check recall.

If the learners scores too low in the quiz, the script offers a chance to try again. The retry is intentional: it supports learning through repetition and reinforcement.

## Design decisions

- Number-word pairs are stored in dictionaries because a dictionary naturally represents a fixed relationship between a key and a value. In this project, the number is the key and the Maltese word is the value, which makes the data easy to read and remember.
- The learning flow is structured as **learn → practice → recall** so the learner first sees the content, then uses it, and finally tries to retrieve it from memory.
- Timed pauses are used to make the script feel more conversational and to give the learner time to read each step.
- Quiz order is randomized so the learner can't rely on the same sequence every time.
- Retry after a low score is meant to reinforce learning after review.
- The script is intentionally simple and procedural so it remains easy to follow as a small educational tool.

## Security notes

- The script runs locally in the terminal.
- The learner’s name is used only for display purposes.
- Answers are compared immediately in memory.
- The script doesn't store data.
- The script doesn't transmit data over the network.
- The script isn't designed for production or multi-user environments.

## Development notes

This repository uses `pre-commit` to help keep files clean and the Python code consistent. The configured checks include:

- trailing whitespace removal
- end-of-file fixing
- YAML validation
- large file checks
- Ruff linting
- Ruff formatting
