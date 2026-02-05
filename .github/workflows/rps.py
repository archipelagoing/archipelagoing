import os
import random
import re

player_move = os.environ["ISSUE_TITLE"].replace("RPS:", "").strip()
choices = ["Rock", "Paper", "Scissors"]
computer_move = random.choice(choices)

if player_move == computer_move:
    outcome = "Tie."
elif (
    (player_move == "Rock" and computer_move == "Scissors") or
    (player_move == "Paper" and computer_move == "Rock") or
    (player_move == "Scissors" and computer_move == "Paper")
):
    outcome = "You win."
else:
    outcome = "You lose."

with open("README.md", "r") as f:
    readme = f.read()

match = re.search(r"\*\*Rounds played:\*\* (\d+)", readme)
rounds = int(match.group(1)) + 1 if match else 1

new_status = (
    f"**Rounds played:** {rounds}  \n"
    f"**Last result:** You chose {player_move}. "
    f"Computer chose {computer_move}. {outcome}"
)

updated = re.sub(
    r"<!-- BEGIN RPS STATUS -->.*?<!-- END RPS STATUS -->",
    f"<!-- BEGIN RPS STATUS -->\n{new_status}\n<!-- END RPS STATUS -->",
    readme,
    flags=re.S
)

with open("README.md", "w") as f:
    f.write(updated)
