import json
import os
class ZapisDoJson:
    def ZapisJson(self,daneMorfologia,daneBiochemia,daneImmunochemia,daneAnalityka,nazwisko):
        wszystkieDane={}
        wszystkieDane.update(daneMorfologia)
        wszystkieDane.update(daneBiochemia)
        wszystkieDane.update(daneImmunochemia)
        for klucz,(wartość,jednostka,zakresMin,zakresMax) in daneAnalityka.items():
            if(klucz in wszystkieDane):
                klucz=klucz+'M'
            wszystkieDane[klucz]=(wartość,jednostka,zakresMin,zakresMax)
        daneJson=[]
        for key, (wartość,jednostka, zakresMin,zakresMax) in wszystkieDane.items():
            daneJson.append(
                {
                "parametr":key,
                "wartość":wartość,
                "jednostka":jednostka,
                "zakresMin": zakresMin,
                "zakresMax": zakresMax
                }
            )
        sciezkaDoPulpitu = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') 
        if(nazwisko!=""):
            sciezkaDoJson=f'{sciezkaDoPulpitu}\wyniki_json_{nazwisko}.json'
        else:
            sciezkaDoJson=f'{sciezkaDoPulpitu}\wyniki_json.json'
        with open(sciezkaDoJson, 'w', encoding='utf-8') as file:
            file.write(json.dumps(daneJson, indent = True,ensure_ascii=False))   
        

