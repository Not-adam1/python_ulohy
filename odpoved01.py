"""
ukol01, k ukolu mate take navod, nebojte se ho pouzit, je tam vse potrebne ke splneni ukolu
"""


# zadavani znamek: uzivatel zada znamku pomoci input a int, jako v navodu :) musite si ji ulozit do promenne
# TODO
znamka = int(input("zadejte znamku: "))
# na zaklade znamky vypise program:
# "vyborne" pokud je znamka 1
# "chvalitebne" pokud je znamka 2
# "dobre" pokud je znamka 3
# "dostatecne" pokud je znamka 4
# "nedostatecne" pokud je znamka 5
# "neznama znamka" pokud neni cislo ani jedno z predchozich

# napoveda, pouzijte if pak nekolikrat elif, pak else
# TODO
if znamka == 1:
    print("vyborne")
elif znamka == 2:
    print("chvalitebne")
elif znamka == 3:
    print("dobre")
elif znamka == 4:
    print("dostatecne")
elif znamka == 5:
    print("nedostatecne")
else:
    print("neznama znamka")

# znovu zadejte znamku (do jine promenne treba znamka2) stejne jako predchozi znamku
# vypiste jestli je znamka vetsi, mensi nebo stejna
# "znamky jsou stejne" pokud znamka je stejna jako ta prvni
# "prvni znamka je vetsi" pokud prvni znamka byla vetsi
# "druha znamka je vetsi" pokud druha znamka byla vetsi
# TODO
znamka2 = int(input("zadej 2 znamku: "))
if znamka == znamka2:
    print("znamky jsou stejne")
elif znamka > znamka2:
    print("prvni znamka je horsi")
else:
    print("druha znamka je horsi")

# zadej cislo z klavesnice a vypis "trefa" pokud je cislo stejne
# "to je malo" pokud je cislo mensi
# "to je moc" pokud je cislo vetsi
a = 7 # s timto cislem musite testovat cislo zadane z klavesnice
# TODO
odhad = int(input("uhodni cislo: "))
if odhad < a:
    print("to je malo")
elif odhad > a:
    print("to je moc")
else:
    print("trefa")