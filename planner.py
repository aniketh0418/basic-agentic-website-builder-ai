from gemini import ask_gemini
from logger import log_step, log_state, log_time
import time

def planner(state):

    start = time.time()

    log_step("PLANNER", "Starting planner node")
    log_state("PLANNER INPUT", state)

    user_prompt = state.get("prompt", "")

    prompt = f"""
    You are a frontend architect.

    Create a website plan for this request:

    {user_prompt}

    Include:
    - sections
    - components
    - style
    """

    log_step("PLANNER", "Calling Gemini...")

    plan = ask_gemini(prompt)

    log_step("PLANNER", "Gemini returned plan")

    state["plan"] = plan

    log_state("PLANNER OUTPUT", state)

    log_time("PLANNER", start)

    return state