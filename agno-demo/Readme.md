# Agno Demo: Simple AI Agent with Groq

A minimal demo of [Agno](https://github.com/agno-agi/agno) integrated with [Groq](https://console.groq.com/) for fast LLM inference. Includes a single-agent example and a multi-agent team demo.

## Quick Start

### Prerequisites
- Python 3.10+
- [Groq API key](https://console.groq.com/keys) (free tier available)

### Setup

```bash
git clone https://github.com/SusanFernandes/agno-demo.git
cd agno-demo

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

pip install -r requirements.txt
```

Create a `.env` file and add your API key:
```
GROQ_API_KEY=your-key-here
```

### Run

```bash
# Single agent
python start.py

# Multi-agent team (Researcher + Writer)
python multiagent.py
```

## Project Structure

```
agno-demo/
├── requirements.txt   # Dependencies
├── .env.example       # API key template
├── agent.py           # Single agent definition
├── multiagent.py      # Multi-agent team (Researcher + Writer)
├── start.py           # Single agent entry point
└── README.md
```

## Customization

**Change model** — Edit `agent.py` or `multiagent.py`:
```python
id="llama-3.3-70b-versatile"  # See https://console.groq.com/docs/models
```

**Change prompt** — Edit `start.py` or `multiagent.py`:
```python
prompt = "Your new prompt here"  # single agent
topic = "Your collaborative task here"  # multi-agent
```

**Add tools** — In `multiagent.py`:
```python
researcher.tools = [DuckDuckGoTools()]  # requires duckduckgo-search
```

**Extend multi-agent** — Add agents to `Team` or change `mode` to `"route"` or `"coordinate"`. See [Agno Teams](https://docs.agno.com/introduction/multi-agent-systems).

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Model deprecated | Check [Groq deprecations](https://console.groq.com/docs/deprecations) and update model ID |
| API errors (401/400) | Verify `.env` key has no quotes or extra spaces |
| Rate limits | Free tier ~30 req/min — wait or upgrade |
| Dependency issues | `pip install --upgrade agno groq` |

## License

MIT