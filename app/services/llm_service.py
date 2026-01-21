import subprocess

def ask_llm(prompt: str) -> str:
    result = subprocess.run(
        ["ollama", "run", "mistral"],
        input=prompt,
        capture_output=True,
        text=True,
        encoding="utf-8"
    )
    return result.stdout.strip()
