import os
import time
from logger import log_step, log_state, log_time
import re

def clean_filename(name):

    invalid_chars = ['<','>',':','"','/','\\','|','?','*']

    for ch in invalid_chars:
        name = name.replace(ch,"")

    return name.strip()


def parse_files(text):

    files = {}

    matches = re.findall(r"FILE:\s*(.*?)\n(.*?)(?=FILE:|\Z)", text, re.DOTALL)

    for name, content in matches:

        content = content.replace("CODE:", "")

        content = re.sub(r"```[a-zA-Z]*", "", content)
        content = content.replace("```", "")

        safe_name = clean_filename(name)

        files[safe_name] = content.strip()

    return files


def write_files(state):

    start = time.time()

    log_step("WRITER", "Writing files")

    code = state["code"]

    files = parse_files(code)

    for path, content in files.items():

        full_path = "generated_site/" + path

        os.makedirs(os.path.dirname(full_path), exist_ok=True)

        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)

    state["files_written"] = True

    state["files_written"] = True

    log_time("WRITER", start)

    return state