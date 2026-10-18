# AI Text Summarizer

A Python application built with the Google Gemini API to automatically summarize text using error handling and multi-model fallbacks.

## Features
- Connects to Google's 
google-genai SDK.
- Handles server busy errors (503 Service Unavailable) automatically with retries.
- Multi-model fallback strategy (gemini-3.5-flash-lite, gemini-2.5-flash, gemini-1.5-flash).

## Setup & Usage
1. Set your Gemini API Key in your terminal:
   ```cmd
   set GEMINI_API_KEY=your_api_key_here
   ```
   ```bash
   2. **Install dependencies:**
   - Windows/Mac/Linux:
   `pip install google-genai`
   ```
   ```bash
   3. **Run the tool:**
   - Execute the script in your terminal:
   `python main.py`
   ```

**Author:** Aryan Rathi
**CU ID:** CU26220292
**Branch:** AI/ML
