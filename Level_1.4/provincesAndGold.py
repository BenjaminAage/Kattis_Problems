PROVINCE_COST = 8
DUCHY_COST = 5
ESTATE_COST = 2

GOLD_COST = 6
SILVER_COST = 3
COPPER_COST = 0

case = input()
G, S, C = case.split(" ")
amount = int(G)*3 + int(S)*2 + int(C)*1

if amount >= GOLD_COST:
    if amount >= PROVINCE_COST:
        print("Province or Gold")
    else:
        print("Duchy or Gold")
elif amount >= SILVER_COST:
    if amount >= DUCHY_COST:
        print("Duchy or Silver")
    else:
        print("Estate or Silver")
elif amount >= ESTATE_COST:
    print("Estate or Copper")
else:
    print("Copper")
