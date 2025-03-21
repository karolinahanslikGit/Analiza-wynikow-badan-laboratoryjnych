from PyPDF2 import PdfReader
from immunochemia import Immunochemia
from analityka import Analityka
from biochemia import Biochemia
from morfologia import Morfologia
from zapisDoJson import ZapisDoJson
from analiza import Analiza
from tkinter import messagebox
import re
class ProgramGlowny:
    

    def __init__(self) :
        self.immunochemia=Immunochemia()
        self.analityka=Analityka()
        self.json=ZapisDoJson()
        self.biochemia=Biochemia()
        self.morfologia=Morfologia()
        self.analiza= Analiza()

    def SprawdzeniePliku(self,sciezkaDoPliku):
        reader=PdfReader(sciezkaDoPliku)
        page=reader.pages[0]
        line=page.extract_text().split('\n')
        
        if(any('sprawozdanie' in linijka.lower() and 'bada' in linijka.lower() for linijka in line)):
            return True
        else:
            return False
    def AnalizaPliku(self,sciezkaDoPliku,imie,nazwisko,pesel,dataUr):
        daneImmunochemia={}
        daneAnalityka={}
        daneBiochemia={}
        danePacjenta={}
        daneMorfologia={}
        reader=PdfReader(sciezkaDoPliku)
        pages=reader.pages
        for page in pages:
            indexBiochem=0
            indexNextBiochem=0    
            indexMorf=0
            indexNextMorf=0
            indexAnalityka=0
            indexNextAnalityka=0
            indexImmuno=0
            indexNextImmuno=0
            czesci={}
            m=0
            a=0
            b=0
            im=0
            oc=0
            ko=0
            
            line=page.extract_text().split('\n') 
            
            for i in range(1,len(line)):
                if(re.search('Morfologia',line[i])):
                    m=i
                    if(m!=0):
                        czesci['Morfologia']=m
                if(re.search('Analityka',line[i])):
                    a=i 
                    if(a!=0):
                        czesci['Analityka']=a   
                if(re.search('Biochemia',line[i])or re.search('BIOCHEMIA',line[i])): 
                    b=i
                    if(b!=0):
                        czesci['Biochemia']=b
                if(re.search('Immunochemia',line[i]) or re.search('Hormony',line[i]) ):
                    im=i
                    if(im!=0):
                        czesci['Immunochemia']=im
                if(re.search('Ocena właściwości próbki',line[i])):
                    oc=i
                    if(oc!=0):
                        czesci['Ocena właściwości próbki']=oc
                if(re.search('Koagulologia',line[i])):
                    ko=i
                    if(ko!=0):
                        czesci['Koagulologia']=ko
                if(re.search('Diagnostyka infekcji',line[i])):
                    di=i
                    if(di!=0):
                        czesci['Diagnostyka infekcji']=di
            foundImmunochem=False
            for key,value in czesci.items():
                if foundImmunochem==True:
                    indexNextImmuno=value
                    break
                if(key=='Immunochemia'):
                    indexImmuno=value+1
                    foundImmunochem=True
                    ostatni=list(czesci.keys())[-1]
                    if ostatni=='Immunochemia':
                        indexNextImmuno=len(line)
                        break
            foundDiagnostyka=False
            for key,value in czesci.items():
                if foundDiagnostyka==True:
                    indexNextDiagnostyka=value
                    break
                if(key=='Dianostyka infekcji'):
                    indexDiagnostyka=value+1
                    foundDiagnostyka=True
                    ostatni=list(czesci.keys())[-1]
                    if ostatni=='Diagnostyka infekcji':
                        indexNextDiagnostyka=len(line)
                        break
            foundAnalityka=False
            for key,value in czesci.items():
                if foundAnalityka==True:
                    indexNextAnalityka=value
                    break
                if(key=='Analityka'):
                    indexAnalityka=value+2
                    foundAnalityka=True
                    ostatni=list(czesci.keys())[-1]
                    if ostatni=='Analityka':
                        indexNextAnalityka=len(line)
                        break
            foundBiochem=False
            for key,value in czesci.items():
                if foundBiochem==True:
                    indexNextBiochem=value
                    break
                if(key=='Biochemia'):
                    indexBiochem=value+2
                    foundBiochem=True
                    ostatni=list(czesci.keys())[-1]
                    if ostatni=='Biochemia':
                        indexNextBiochem=len(line)
                        break
        
            foundMorf=False
            for key,value in czesci.items(): 
                if foundMorf==True:
                    indexNextMorf=value
                    break
                if(key=='Morfologia'):
                    indexMorf=value+1
                    foundMorf=True
                    if len(czesci)==1:
                        indexNextMorf=len(line)
                        break
            wynikiImmuno = self.immunochemia.OdczytWynikowImmunochemicznych(indexImmuno,indexNextImmuno,line)
            daneImmunochemia.update(wynikiImmuno)
            wynikiAnalityka=self.analityka.OdczytWynikowAnalitycznych(indexAnalityka,indexNextAnalityka,line)
            daneAnalityka.update(wynikiAnalityka)
            wynikiBiochemia=self.biochemia.OdczytWynikowBiochemicznych(indexBiochem,indexNextBiochem,line)
            daneBiochemia.update(wynikiBiochemia)
            wynikiMorfoliga=self.morfologia.OdczytWynikowMorfologicznych(indexMorf,indexNextMorf,line)
            daneMorfologia.update(wynikiMorfoliga)
            self.json.ZapisJson(daneMorfologia,daneBiochemia,daneImmunochemia,daneAnalityka,nazwisko)
            danePacjenta['Imie']=imie
            danePacjenta['Nazwisko']=nazwisko
            danePacjenta['PESEL']=pesel
            danePacjenta['DataUrodzenia']=dataUr
        print(daneImmunochemia)
        print('--------------------------------------------')
        print(daneAnalityka)
        print('----------------------------------------------')
        print(daneBiochemia)
        print('---------------------------------')
        print(daneMorfologia)
        print('----------------------------------------------')
        self.analiza.AnalizaWynikow(daneMorfologia,danePacjenta,daneAnalityka,daneImmunochemia,daneBiochemia)
            
if __name__ == "__main__":
    mainProgram = ProgramGlowny()  
    mainProgram.AnalizaPliku("wyniki\wyniki_anonimowe\wyniki_redacted.pdf","","","","")  
    