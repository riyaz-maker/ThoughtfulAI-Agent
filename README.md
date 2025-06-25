# Overview
Thoughtful AI support agent built with Python and Gradio. It is designed to handle user questions about the Thoughtful AI's products by retrieving answers from a hardcoded dataset. For any questions outside the dataset, it provides a fallback response.

## Features
Knowledge based responses: Answers are sourced from a structured, internal hardcoded dataset.
Intelligent fuzzy string matching: Uses thefuzz library to match user questions against predefined questions.
Robust Fallback Mechanism: Handles invalid or unexpected inputs with a predefined response.

## Tech Stack
Backend - Python
UI Interface - Gradio
Core logic - thefuzz. 
Install the dependencies by copying this code in terminal.
```bash
pip install thefuzz gradio
```
## Screenshot of UI in localhost and replit
<img width="1440" alt="Screenshot 2025-06-25 at 03 45 42" src="https://github.com/user-attachments/assets/69524a4e-5ed4-4d24-b27c-bd4d1026fe95" />
<img width="1440" alt="Screenshot 2025-06-25 at 04 16 04" src="https://github.com/user-attachments/assets/2be5c1ac-98a7-452b-9ac2-76f5a7269014" />

## Working
KNOWLEDGE_BASE dictionary holds the dataset given from the exercise. thefuzz.process.extractOne present in the find_best_match function is used to calculate the similarity between the user's question and all the questions in the KNOWLEDGE_BASE. Match is only considered valid if its similarity score is above 0.8. If no question in the dataset meets the threshold, the find_best_match function returns None.
