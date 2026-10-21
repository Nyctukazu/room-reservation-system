import os

def generate_ai_response(prompt: str) -> str:
    """
    Hackathon AI Service integration stub.
    
    You can easily drop in OpenAI, Google Gemini, Anthropic, or Hugging Face here:
    
    Example for Google Gemini:
    ```python
    import google.generativeai as genai
    genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text
    ```
    """
    api_key = os.environ.get('GEMINI_API_KEY') or os.environ.get('OPENAI_API_KEY')
    
    if not api_key:
        return f"[MOCK AI RESPONSE]: Received '{prompt}'. Add GEMINI_API_KEY or OPENAI_API_KEY in .env to activate live AI generation."
    
    return f"AI response generated for prompt: {prompt}"
