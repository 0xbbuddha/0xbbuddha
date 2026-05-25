import requests
import asciichartpy as ac
from datetime import date

USERNAME = "PtitWaguri"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
GAME_COUNT = 100


def fetch_ratings():
    url = f"https://api.chess.com/pub/player/{USERNAME}/games/archives"
    archives = requests.get(url, headers=HEADERS).json()["archives"][::-1]

    ratings = []
    for archive_url in archives:
        if len(ratings) >= GAME_COUNT:
            break
        games = requests.get(archive_url, headers=HEADERS).json().get("games", [])
        for game in reversed(games):
            if len(ratings) >= GAME_COUNT:
                break
            if game.get("time_class") != "rapid" or game.get("rules") != "chess":
                continue
            color = "white" if game["white"]["username"].lower() == USERNAME.lower() else "black"
            ratings.append(game[color]["rating"])

    return list(reversed(ratings))


def main():
    ratings = fetch_ratings()
    if not ratings:
        print("No rapid games found.")
        return

    chart = ac.plot(ratings, {"height": 17, "min": min(ratings), "max": max(ratings)})
    chart_block = f"{chart}\n\n  Chart last updated - {date.today()}"

    with open("README.tpl") as f:
        readme = f.read()

    readme = readme.replace("{{ RATINGS_PLACEHOLDER }}", chart_block)

    with open("README.md", "w") as f:
        f.write(readme)


if __name__ == "__main__":
    main()
