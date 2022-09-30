from disgay.scraper import scrape
from colorama import Fore

x = [
    "f",
    "F",
    "n",
    "N"
]

def main():

    token = input("Enter your token (skip to choose from config): ")
    guild_id = input("Enter guild id: ")
    channel_id = input("Enter channel id: ")

    run_badge_scraper = input("Run badge scraper (True/False)? ")

    if run_badge_scraper != "False" or run_badge_scraper != "True":
        for y in x:
            if y in run_badge_scraper:
                run_badge_scraper = "False"
                break
            else:
                run_badge_scraper = "True"
    run_badge_scraper = bool(run_badge_scraper)

    ids = scrape(token, guild_id, channel_id, run_badge_scraper)

    print(f"{Fore.GREEN}[SUCCESS] Successfuly scraped {len(ids)} IDs from {guild_id} saving them to scraped/{guild_id}.txt")

    with open(f"scraped/{guild_id}.txt", "w", encoding="utf-8") as f:
        for id in ids:
            print(id)
            f.write(f"{id}\n")

    input("Press enter to Exit...\n\n")

main()