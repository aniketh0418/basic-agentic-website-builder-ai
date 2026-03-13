from gemini import ask_gemini
import time
from logger import log_step, log_state, log_time

def coder(state):

    start = time.time()

    log_step("CODER", "Starting code generation")
    log_state("CODER INPUT", state)

    plan = state["plan"]

    prompt = f"""
    Generate a responsive frontend website.

    Use HTML + Tailwind.

    Plan:
    {plan}

    Return files like this:

    FILE: index.html
    CODE:
    ...

    FILE: styles.css
    CODE:
    ...
    """

    code = ask_gemini(prompt)

    state["code"] = code

    log_step("CODER", "code geerated")

    log_state("CODER OUTPUT", {"code_length": len(code)})

    log_time("CODER", start)

    return state