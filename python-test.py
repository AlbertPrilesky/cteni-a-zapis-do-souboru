import os
from datetime import datetime
from decimal import Decimal

DELIMITER = "#"

def zpracuj_postavy(radek):
    postavy = radek.split(DELIMITER)
    jmeno = postavy[0]
    vek = int (postavy[1].strip())
    pohlavi = postavy[2].strip()
    zvire = bool(postavy[3].strip())
    datum_promitani = datetime.strptime(postavy[4].strip(), "%Y-%m-%d")
    oblibenost = Decimal(postavy[5].strip())

    if oblibenost > Decimal("2.5"):
        print(f"Jméno: {jmeno}\n- Věk: {vek}\n- Pohlaví: {pohlavi}\n- Zvíře: {zvire}\n- Datum promítání: {datum_promitani}\n- Oblíbenost: {oblibenost}")

        return "\t".join([
            jmeno,
            str(vek),
            pohlavi,
            "ano" if zvire else "ne",
            datum_promitani.strftime("%Y-%m-%d"),
            str(oblibenost)
        ]) + "\n"
    
    return None

vystup = []

with open(os.sep.join(["postavy.txt"]), "r", encoding="utf-8") as soubor:
    radky = soubor.readlines()
    for radek in radky:
        vysledek = zpracuj_postavy(radek)
        if vysledek is not None:
            vystup.append(vysledek)

with open("oblibene-postavy.txt", "w", encoding="utf-8") as vystup_soubor:
    vystup_soubor.writelines(vystup)