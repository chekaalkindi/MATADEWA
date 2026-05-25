import ollama

def analyze_results(query, findings):

    prompt = f"""
Analyze public OSINT findings.

Target:
{query}

Findings:
{findings}

Generate:
- Profile summary
- Exposure assessment
- Public interests
- Risk indicators

Avoid unsupported claims.
"""

    response = ollama.chat(
        model='mistral',
        messages=[
            {
                'role': 'user',
                'content': prompt
            }
        ]
    )

    return response['message']['content']
