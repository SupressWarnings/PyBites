from collections import defaultdict

# fake data from https://www.mockaroo.com
data = """last_name,first_name,country_code
Watsham,Husain,ID
Harrold,Alphonso,BR
Apdell,Margo,CN
Tomblings,Deerdre,RU
Wasielewski,Sula,ID
Jeffry,Rudolph,TD
Brenston,Luke,SE
Parrett,Ines,CN
Braunle,Kermit,PL
Halbard,Davie,CN"""


def group_names_by_country(data: str = data) -> defaultdict:
    countries = defaultdict(list)
    # your code
    entries = data.split("\n")
    country_names = [string.split(",")[-1] for string in entries]
    country_names.remove("country_code")
    country_set = set(country_names)
    for entry in entries[1:]:
        words = entry.split(",")
        countries[words[-1]].append(f"{words[1]} {words[0]}")
    return countries
