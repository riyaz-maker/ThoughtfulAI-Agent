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
