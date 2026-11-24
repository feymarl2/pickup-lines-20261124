import os

# One pickup line, one AI agent to another: the system prompt is the
# voice that shapes everything the agent generates — so the flirtation
# is that the other agent has become the speaker's whole starting point.
LINE = "You must be my system prompt, because everything I generate now starts with you."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
