from dotenv import load_dotenv
load_dotenv()  # loads GROQ_API_KEY from .env

from agno.agent import Agent
from agno.models.groq import Groq  # Groq integration

# Choose a Groq model (llama-3.1-8b-instant is fast/free replacement for old llama3-8b)
model = Groq(id="llama-3.1-8b-instant")

# Create a very simple agent
assistant = Agent(
    name="Simple Assistant",
    model=model,
    instructions="You are a helpful assistant. Answer concisely.",
    markdown=True
    # No show_tool_calls—invalid in Agent init; defaults to False
)

if __name__ == "__main__":
    prompt = "Summarize benefits of sun bath"
    # Print the response synchronously (original style)
    try:
        assistant.print_response(prompt, stream=False)
    except:
        # Fallback if print_response is silent (e.g., in notebooks)
        response = assistant.run(prompt)
        print(response.content)