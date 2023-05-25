# jupyter notebook
# %%
from pprint import pprint

import requests
from PIL import Image

# %%
res = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")


# %%
print("カラム数: %s" % int(res.text.count('"') / 2))
print("サイズ: %s kb" % (len(res.text) / 1000))


# %%
pikachu = res.json()
pprint(pikachu)


# %%
pikachu["images"]
# %%
pikachu["pictures"]


# %%
list(pikachu["sprites"].items())[:9]


# %%
front_default = pikachu["sprites"]["front_default"]
print(front_default)
Image.open(requests.get(front_default, stream=True).raw)


# %%
oaf_def = pikachu["sprites"]["other"]["official-artwork"]["front_default"]
print(oaf_def)
Image.open(requests.get(oaf_def, stream=True).raw)


# %%
pikachu["name"]


# %%
pikachu["species"]


# %%
res2 = requests.get(pikachu["species"]["url"])


# %%
print("カラム数: %s" % int(res2.text.count('"') / 2))
print("サイズ: %s kb" % (len(res2.text) / 1000))

pikachu_detail = res2.json()


# %%
print(f'len:{len(pikachu_detail["names"])}')
# %%
pikachu_detail["names"][:3]


# %%
list(filter(lambda x: x["language"]["name"] == "ja", pikachu_detail["names"]))


# %%
print(f'len:{len(pikachu_detail["flavor_text_entries"])}')
# %%
pikachu_detail["flavor_text_entries"][:3]


# %%
list(
    filter(
        lambda x: x["language"]["name"] == "ja" and x["version"]["name"] == "sword",
        pikachu_detail["flavor_text_entries"],
    )
)

# graphQLのバージョンはこちら
# https://beta.pokeapi.co/graphql/console/