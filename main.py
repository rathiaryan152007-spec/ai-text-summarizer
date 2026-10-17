import os
import sys
import time
from google import genai
from google.genai.errors import ServerError

def summarize_text(input_text):
    client = genai.Client()
    prompt = f"Summarize the following text clearly in 3 short bullet points:\n\n{input_text}"
    
    # List of models to try in order if one is at peak capacity
    models_to_try = ["gemini-3.5-flash-lite", "gemini-2.5-flash", "gemini-1.5-flash"]
    
    for model_name in models_to_try:
        for attempt in range(2):
            try:
                response = client.models.generate_content(
                    model=model_name,
                    contents=prompt,
                )
                return response.text
            except ServerError as e:
                print(f"[{model_name} busy, retrying... (Attempt {attempt + 1}/2)]")
                time.sleep(2)
    
    return "Error: All Gemini model endpoints are currently experiencing high demand. Please wait a few moments and try again."

if __name__ == "__main__":
    print("=== AI TEXT SUMMARIZER ===")
    user_input = input("Enter text to summarize: ")
    print("\n--- Generating Summary ---")
    print(summarize_text(user_input))