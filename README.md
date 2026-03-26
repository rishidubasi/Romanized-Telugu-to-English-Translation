# Romanized Telugu to English Translation

## Overview
This project is an NLP-based translation system that converts romanized Telugu text (often mixed with English, such as social media posts or chats) into meaningful English sentences.

It uses a transformer-based model (T5) fine-tuned on custom data to handle informal and mixed-language inputs.

## Features
- Translates romanized Telugu + English mixed text into English
- Handles informal language (tweets, chats, comments)
- Custom dataset preprocessing and cleaning
- Transformer-based sequence-to-sequence learning
- Web interface using Flask for real-time translation

## Tech Stack
- Python
- HuggingFace Transformers (T5)
- PyTorch
- Pandas, NumPy
- Flask (for deployment)
- HTML/CSS (frontend)

## Dataset
- Custom dataset created and preprocessed for romanized Telugu to English translation
- Includes mixed-language text (Telugu + English)
- Data cleaning applied using encoding fixes and preprocessing steps

## Model
- T5-small fine-tuned for translation
- Input format:
  translate romanized telugu to english: <text>

## Example
Input:
naku ee movie chala nachindi

Output:
I liked this movie very much
