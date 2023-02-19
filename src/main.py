from requests_html import HTMLSession
#from classes import Pokemon

from bs4 import BeautifulSoup
import requests

# Try and have damage projections/calculations
# show each mon and possible movesets
# show mons with hazardz
# show mons with recovery

#def pokemon():
#    website = requests.get("https://play.pokemonshowdown.com/battle-gen9ou-1793765055").text
#    soup = BeautifulSoup(website, "lxml")
#    # pokemon = soup.find_all("span", class_="picon has-tooltip")
#    print("printing soup...")
#    print(soup)
#    #test = soup.find_all("div")
#    #print(test)


def get_team():
    # 'data-tooltip' is key that be associated with a pokemon
    # it tells them the user and then which slot

    # Unfortunately can't tell if first 0 or 1 is deterministic based
    # on whether it is me or other user

    # I was S against Xakisu and I was 0
    # I was S against n and I was 1
    # I was S against RaytedR and I was 1
    # maybe make name bunch of A
    # Initially unable to reverse engineer how they determine 0 or 1
    # What I could do is give my first and pokemon a unique nickname
    # So script will see my lead, and then go until it sees end
    # Then the others will be put on a different team
    # Implement this and try to get it outputting in a list
    # a < A < 0 ???

    # So far link must be in this format
    # https://play.pokemonshowdown.com/battle-gen9ou-1793970481
    # Not this format
    # https://play.pokemonshowdown.com/battle-gen9ou-1793969083-zjw3c7n9w8pmlz4gd3tv1auu8rny9zqpw

    # Currently is able to make a list and keep both teams pokemon
    # It does display nicknames, status, and damage.
    # Status and damage are surrounded by () so will be easy to parse

    # Next steps are storing status and health
    # Then storing it on a website with cool visual and common movesets
    # Get movesets from smogon, maybe they have API
    # If not, can probably web scrape easily with soup
    # Will likely need to create a front end and my own APIS as backend
    # Ideally even make calcs run automatically

    # Probably upload to github repo over the weekend

    # Might need to update for when teams dont have 6 mons

    # Show ratings, recovery

    # Thing to tell you if they are band, specs, or not

    # Can also track moves as they have and
    all_mons = []
    session = HTMLSession()
    url = input("Enter Showdown URL: ")
    poke = session.get(url)
    poke.html.render(sleep=2, keep_page=True, scrolldown=1)
    # uses CSS Selector
    teams = poke.html.find(".picon.has-tooltip")
    print(teams)

    for x in teams:
        # print(x)
        # print(x.attrs["aria-label"])
        all_mons.append(x.attrs["aria-label"])
    for index, pokemon, in enumerate(all_mons):
        if pokemon[0] == "#" and 5 >= index >= 0:
            user_team = [all_mons[x] for x in range(6)]
            enemy_team = [all_mons[x] for x in range(6, 12)]
            break
        elif pokemon[0] == "#" and 11 >= index >= 0:
            user_team = [all_mons[x] for x in range(6, 12)]
            enemy_team = [all_mons[x] for x in range(6)]
            break
    else:
        # If loop never breaks, we couldn't distinguish teams
        # Throw error, probably not keyerror tho
        raise KeyError("Cannot distinguish user and enemy team, # not found")


    # Now work on having list of just names
    user_team_names_only = []
    enemy_team_names_only = []
    for pokemon in enemy_team:
        print(pokemon)
        tmp = ""
        # If last char isn't #, then no conditions and can just take name backwards
        if (pokemon[-1] != ")"):
            for char in reversed(pokemon):
                if (char != " "):
                    tmp += char
                else:
                    break
        # They do have some status, need to go through those
        else:
            # Example: Dondozo (56%) (brn)
            # Must go through all sets of () to get to name
            arr = pokemon.split()
            print(arr)

        enemy_team_names_only.append(tmp[::-1])

    print("User team is", user_team)
    print("Enemy team is", enemy_team)
    print(f'Enemy team names only is {enemy_team_names_only}')

def parseEnemyPokemon(arr):
    """
    OU mons with double spaces in their name
    Iron Treads, Iron Valiant, Roaring Moon, Iron Moth, Great Tusk

    If using this function, it is not simple
    Pokemon name will be surrounded in parenthesis like (Dondozo) or (Great Tusk)

    """
    pass


def test():
    session = HTMLSession()
    poke = session.get("https://www.smogon.com/dex/sv/pokemon/dondozo/")
    poke.html.render(sleep=2, keep_page=True, scrolldown=1)
    # Need to find way to get only movesets
    moves = poke.html.find(".MoveLink")
    print(moves)


if __name__ == "__main__":
    get_team()
