import subprocess
import time
from logger import log_step, log_state, log_time

def deploy(state):

    start = time.time()

    print("Deploying to Vercel...")

    subprocess.run("vercel --prod", shell=True, cwd="generated_site")

    log_step("DEPLOY", "Deployment finished")

    state["deployed"] = True

    log_time("DEPLOY", start)

    return state