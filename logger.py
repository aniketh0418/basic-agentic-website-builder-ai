import time

def log_step(step_name, message):
    print(f"\n[{step_name}] {message}")

def log_state(step_name, state):
    print(f"[{step_name}] STATE → {state}")

def log_time(step_name, start_time):
    elapsed = time.time() - start_time
    print(f"[{step_name}] completed in {elapsed:.2f}s")