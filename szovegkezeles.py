
szoveg: str = "Szép nap van!"
"""ird ki a szoveg hosszat"""
print(szoveg[0])
"""ird ki az masodik karaktert"""
print(szoveg[1])
print("A szoveg hossza",len(szoveg))
"""ird ki a szoveg utolso karakteret"""
print("utolso",szoveg[len(szoveg)-1])
"""feladat:ird ki a szoveg karaktereit egymas ala, betunket"""

i:int = 0
while i < len(szoveg):
    print(szoveg[i])
    i += 1

def szovegkezeles():
    szoveg:str ="ez egy teszt szöveg"
    print(szoveg)
    print(szoveg.upper)
    """van e a szovegben 'teszt' szoveg?"""
    x:int =szoveg.find("teszt")
    if x>=0:
        print("nincs benne teszt szöveg")
    else:
        print("van benne teszt szöveg")
    """A SZOVEG valtozoban hol szerepel eloszor a s betu?"""
    print(szoveg.index("s"), ".helyen szerepel az s betu!")
    """alakitsd at minden szo kezdobetujet nagybetusse"""
    print (szoveg.title)
    """csereld ki a teszt szot 'próba!' szora"""
    print(szoveg.replace("teszt","próba"))

def aszoveg_visszafele(szoveg:str):
    """a parameterben kapott szoveg visszafele kiirva egymas melle a betuket"""
    """print(szoveg[::-1])csak píthonban"""
    i:int = len(szoveg)
    while i!=0:
        print(szoveg[i-1],end="")
        i-=1
def a_betuk_szama(szoveg:str):
    """hany 'a' betu van a szovegben?"""
    #print(szoveg.count("a"))
    i:int = 0
    a_szam:int = 0
    while i<len(szoveg):
        if szoveg[i] == 'a':
            a_szam += 1
        i+= 1
    print("A betűk száma: ", a_szam)










