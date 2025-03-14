import time
from crewai import LLM

class FallbackLLM:
    def __init__(self, primary_model="gemini/gemini-2.0-flash-exp", fallback_model="groq/llama-3.3-70b-versatile", timeout=5):
        """Initialize with primary and fallback LLMs."""
        self.primary_llm = LLM(model=primary_model)
        self.fallback_llm = LLM(model=fallback_model)
        self.timeout = timeout 

    def generate_response(self, prompt):
        """Generate response with fallback if primary LLM fails or times out."""
        try:
            start_time = time.time()
            response = self.primary_llm.generate(prompt)
            if time.time() - start_time > self.timeout:
                raise TimeoutError("Primary LLM exceeded timeout")
            return response
        except Exception as e:
            print(f"Primary LLM failed: {e}. Switching to fallback.")
            return self.fallback_llm.generate(prompt)
