import os
import json
import urllib.request
import urllib.error

from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

API_URL = "https://openrouter.ai/api/v1/chat/completions"


def get_ticket_suggestions(description):

    if not API_KEY:
        raise ValueError("OpenRouter API key is missing.")

    prompt = f"""
    You are an IT support assistant.

    A student has reported the following technical problem:

    {description}

    Please provide:
    1. Possible causes of the problem.
    2. Steps to investigate the problem.
    3. Practical solutions.
    4. When the issue should be escalated to technical support.

    Use simple and clear language.
    """

    payload = {
        "model": "openrouter/free",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    data = json.dumps(payload).encode("utf-8")

    request = urllib.request.Request(
        API_URL,
        data=data,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        method="POST"
    )

    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            result = json.loads(response.read().decode("utf-8"))

        return result["choices"][0]["message"]["content"]

    except urllib.error.HTTPError as error:
        details = error.read().decode("utf-8")
        raise RuntimeError(f"OpenRouter API error: {details}")

    except urllib.error.URLError as error:
        raise RuntimeError(f"Connection error: {error.reason}")

    except (KeyError, IndexError, json.JSONDecodeError):
        raise RuntimeError("Could not understand the response from OpenRouter.")