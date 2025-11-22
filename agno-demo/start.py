# Simple launcher for the Agno agent
# Run: python start.py

import sys
import os

# Add current dir to path (for agent.py)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import and run the agent
from agent import assistant  # Assumes agent.py defines 'assistant'

if __name__ == "__main__":
    prompt = "Explain Newton's second law in one short paragraph."  # Or input("Enter prompt: ")
    try:
        assistant.print_response(prompt, stream=False)
    except:
        response = assistant.run(prompt)
        print(response.content)
    print("\n--- Agent ready! Edit start.py for new prompts. ---")