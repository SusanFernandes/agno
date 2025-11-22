from dotenv import load_dotenv
load_dotenv()  # Loads GROQ_API_KEY from .env

from agno.agent import Agent
from agno.team.team import Team  # For multi-agent collaboration
from agno.models.groq import Groq

# Define two collaborating agents (using Groq for speed)
researcher = Agent(
    name="Researcher",
    role="Conduct research and gather key facts on the topic.",
    model=Groq(id="llama-3.1-8b-instant"),  # Fast model for research
    instructions="""
    You are a thorough researcher. For the given topic:
    - List 3-5 key facts or concepts.
    - Cite sources if possible (simulate or use tools).
    - Keep it factual and concise.
    Pass your findings to the Writer for summarization.
    """,
    markdown=True
)

writer = Agent(
    name="Writer",
    role="Write a polished, engaging summary based on research.",
    model=Groq(id="llama-3.1-8b-instant"),  # Same model for consistency
    instructions="""
    You are a skilled writer. Using the researcher's facts:
    - Write a short blog-style paragraph (100-150 words).
    - Make it engaging and structured: intro, body, conclusion.
    - End with implications or next steps.
    """,
    markdown=True
)

# Create a Team: Agents collaborate via shared context
team = Team(
    name="Research-Write Team",
    members=[researcher, writer],  # Fixed: Use 'members', not 'agents'
    model=Groq(id="llama-3.1-8b-instant"),  # NEW: Override OpenAI fallback with Groq
    delegate_to_all_members=True,  # All members discuss/collaborate on the task
    instructions="""Collaborate to create a short explanation on the topic.
    Researcher starts with facts, Writer polishes the output. Share context freely.
    Stop when consensus is reached.""",  # Team-wide instructions (string or list)
    markdown=True,
    show_members_responses=True  # Show individual agent outputs for demo
)

if __name__ == "__main__":
    topic = "Explain AI ethics in one short paragraph."  # Change this for different outputs
    print(f"Team collaborating on: {topic}\n")
    # Run the team synchronously
    try:
        team.print_response(topic, stream=False)
    except:
        # Fallback for output issues
        response = team.run(topic)
        print(response.content)
    print("\n--- Multi-agent demo complete! Edit 'topic' for new tasks. ---")