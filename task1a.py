from itertools import combinations

k = int(input("squad size: "))

pd = {
    "Pikachu": ("Electric",),
    "Charizard": ("Fire", "Flying"),
    "Lapras": ("Water", "Ice"),
    "Machamp": ("Fighting",),
    "Mewtwo": ("Psychic", "Fighting"),
    "Hoopa": ("Psychic", "Ghost", "Dark"),
    "Lugia": ("Psychic", "Flying", "Water"),
    "Squirtle": ("Water",),
    "Gengar": ("Ghost", "Poison"),
    "Onix": ("Rock", "Ground")
}

mx = 0
best = None
bt = None

for sq in combinations(pd.keys(), k):
    t = set()
    for p in sq:
        t.update(pd[p])
    if len(t) > mx:
        mx = len(t)
        best = sq
        bt = t

print("Strongest Squad:", best)
print("Covers Types:", bt)
print("Number of Types:", mx)
