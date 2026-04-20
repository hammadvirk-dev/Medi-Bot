```python
import os
import time
import google.generativeai as genai

# --- CONFIGURATION ---
# The environment provides the API key at runtime.
API_KEY = "" 
genai.configure(api_key=API_KEY)

def get_gemini_response(prompt):
    """
    Fetches response from Gemini 2.5 Flash with exponential backoff.
    """
    model = genai.GenerativeModel('gemini-2.5-flash-preview-09-2025')
    
    # Exponential backoff parameters: 1s, 2s, 4s, 8s, 16s
    for n in range(5):
        try:
            response = model.generate_content(
                prompt,
                generation_config={"temperature": 0.3}
            )
            return response.text
        except Exception:
            if n == 4:
                return "Error: Unable to connect to the AI engine after multiple attempts. Please check your internet connection."
            time.sleep(2**n)

def check_interactions(drug_a, drug_b):
    """
    Constructs the medical analysis prompt for the AI.
    """
    system_prompt = (
        "You are a professional Medical AI Assistant. Analyze the interaction between two drugs. "
        "Provide a structured report including: \n"
        "1. Interaction Severity (Minor, Moderate, Major)\n"
        "2. Potential Side Effects\n"
        "3. Safety Warnings\n"
        "4. Recommendations for the user (always advise consulting a doctor).\n"
        "Maintain a professional, clinical tone."
    )
    
    user_query = f"Analyze the interaction between {drug_a} and {drug_b}."
    
    full_prompt = f"System Instruction: {system_prompt}\n\nUser Query: {user_query}"
    return get_gemini_response(full_prompt)

def main():
    print("="*50)
    print("🏥 MEDI-BOT: AI-Powered Drug Interaction Checker")
    print("Developed by Hammad Virk")
    print("="*50)
    print("\n[DISCLAIMER]: This tool is for EDUCATIONAL PURPOSES ONLY.")
    print("It is NOT a substitute for professional medical advice, diagnosis, or treatment.")
    print("Always seek the advice of your physician or qualified health provider.\n")

    while True:
        drug_a = input("Enter the first medication name (or 'q' to quit): ").strip()
        if drug_a.lower() == 'q': break
        
        drug_b = input("Enter the second medication name: ").strip()
        if not drug_b:
            print("Please enter two medications.")
            continue

        print(f"\n🔍 Analyzing interaction between {drug_a} and {drug_b}...")
        
        result = check_interactions(drug_a, drug_b)
        
        print("\n--- ANALYSIS REPORT ---")
        print(result)
        print("-" * 30)
        print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    main()

```
  
