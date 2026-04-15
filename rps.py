import os
import random
import re

# Inputs from GitHub
player_move = os.environ["ISSUE_TITLE"].replace("RPS:", "").strip().lower()
player = os.environ.get("ACTOR", "someone")

choices = ["rock", "paper", "scissors"]
computer_move = random.choice(choices)

if player_move == computer_move:
    outcome = "Tie"
elif (
    (player_move == "rock" and computer_move == "scissors") or
    (player_move == "paper" and computer_move == "rock") or
    (player_move == "scissors" and computer_move == "paper")
):
    outcome = "Win"
else:
    outcome = "Loss"

outcome_display = {
    "Win": "🏆 Win",
    "Loss": "❌ Loss",
    "Tie": "🫱🏾‍🫲🏻 Tie"
}[outcome]

with open("README.md", "r") as f:
    readme = f.read()

def extract(pattern, default=0):
    m = re.search(pattern, readme)
    return int(m.group(1)) if m else default

rounds = extract(r"\*\*rounds played:\*\* (\d+)") + 1

wins = extract(r"(\d+)W")
losses = extract(r"(\d+)L")
ties = extract(r"(\d+)T")

if outcome == "Win":
    wins += 1
elif outcome == "Loss":
    losses += 1
else:
    ties += 1

rock_count = extract(r"Rock: (\d+)")
paper_count = extract(r"Paper: (\d+)")
scissors_count = extract(r"Scissors: (\d+)")

if player_move == "rock":
    rock_count += 1
elif player_move == "paper":
    paper_count += 1
elif player_move == "scissors":
    scissors_count += 1

move_emoji = {
    "rock": "🪨",
    "paper": "📄",
    "scissors": "✂️"
}

new_status = (
    f"**rounds played:** {rounds}  \n"
    f"**record:** {wins}W · {losses}L · {ties}T  \n\n"
    f"**move counts:**  \n"
    f"🪨 Rock: {rock_count} · 📄 Paper: {paper_count} · ✂️ Scissors: {scissors_count}  \n\n"
    f"**last player:** @{player}  \n"
    f"**last round:** 😄 you played **{player_move.title()}** · "
    f"💻 computer played **{computer_move.title()}** → **{outcome_display}**"
    f"**play shown:** 😄 {move_emoji[player_move]} vs 💻 {move_emoji[computer_move]}  \n"
)

updated = re.sub(
    r"<!-- BEGIN RPS STATUS -->.*?<!-- END RPS STATUS -->",
    f"<!-- BEGIN RPS STATUS -->\n{new_status}\n<!-- END RPS STATUS -->",
    readme,
    flags=re.S
)

with open("README.md", "w") as f:
    f.write(updated)
