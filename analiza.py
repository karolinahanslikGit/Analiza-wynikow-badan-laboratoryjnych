from generowaniePDF import GenerowaniePDF
from odczytZakresow import OdczytZakresow
import re
class Analiza():
    
    def __init__(self):
        self.tabelaMorf=[]
        self.tabelaAnalityka=[]
        self.tabWartMorf=[]
        self.tabWartBiochem=[]
        self.tabWartImmuno=[]
        self.tabWartAnalityka=[]
        self.tabelaBiochemia=[]
        self.tabelaImmunochemia=[]
        self.generowanie=GenerowaniePDF()
        self.odczytZakresow=OdczytZakresow()
    def AnalizaWynikow(self,daneMorf,danePacjenta,daneAnalityka, daneImmunochemia,daneBiochemia):
        self.tabelaMorf=[]
        self.tabelaAnalityka=[]
        self.tabWartMorf=[]
        self.tabWartBiochem=[]
        self.tabWartImmuno=[]
        self.tabWartAnalityka=[]
        self.tabelaBiochemia=[]
        self.tabelaImmunochemia=[]
        tabZaWysokoMorf=[]
        tabZaNiskoMorf=[]
        tabZaNiskoBiochem=[]
        tabZaWysokoBiochem=[]
        tabZaWysokoImmuno=[]
        tabZaNiskoImmuno=[]
        tabZaNiskoAnalityka=[]
        tabZaWysokoAnalityka=[]
        tabNiepAnalityka=[]
        parametryImmunochemiczne=['tsh','ft3','ft4','ferrytyna','witamina','psa','prolaktyna','testosteron','kortyzol']
        parametryBiochemiczne=['alt','ast','bilirubina','kreatynina','egfr','ggtp','witamina','glukoza','cholesterol','peroksyd','triglicerydy','sód','potas','mocznik','aterogenności','magnez','crp','alkohol','wapń','żelazo','alp','albumina','moczowy']
        hemat="Podstawy hematologii dla studentów i lekarzy, Aleksander B. Skotnicki, Wiesław S. Nowak, Medycyna Praktyczna, Kraków 1998. "
        kreat="Should we pay more attention to low creatinine levels?, Carlos A. Amado Diagoa, José A. Amado Senaris,Endocrinología, Diabetes y Nutrición 2020, tom: 67,str: 486-492."
        badaniaLab="Badania Laboratoryjne - zakres norm i interpretacja, F.Kokot, S.Kokot, Wydawnictwo Lekarskie PZWL, Warszawa, 2002."
        diagSUM="DIAGNOSTYKA LABORATORYJNA DLA STUDENTÓW MEDYCYNY. Zofia Ostrowska, Bogdan Mazur. Śląski Uniwersytet Medyczny, Katowice, 2011"
        diagGUMED="Diagnostyka Laboratoryjna TOM II, A.Szutowicz, A.Raszeja-Specht, Gdański Uniwersytet Medyczny, 2011"
        diagLab="Diagnostyka Laboratoryjna z elementami biochemii klinicznej, A.Dembińska-Kieć, J.W.Naskalski, Volumed, Wrocław, 1998"
        atero="Association of atherogenic index of plasma with cardiovascular disease mortality and allcause mortality in the general US adult population: results from NHANES 2005–2018, Minghui Qin, Bo Chen, Cardiovascular Diabetology 2024,tom: 23, DOI: 10.1186/s12933-024-02359-z."
        neutroArt="How we evaluate and treat neutropenia in adults, A. Gibson, N. Berliner, Blood, 2014, 124 (8) str: 1251-1258, DOI:https://doi.org/10.1182/blood-2014-02-482612"
        monoStr="https://www.msdmanuals.com/professional/hematology-and-oncology/leukopenias/neutropenia#Treatment_v970715"
        platet="Średnia objętość płytek krwi i wskaźnik dużych komórek jako czynniki prognostyczne choroby wieńcowej i zawału serca, M. Gawlita, J. Wasilewski, T. Osadnik, R. Reguła, K. Bujak, M. Gonera, Folia Cardiologica 2015, tom: 10, str: 418-422, DOI: 10.5603/FC.2015.0079"
        nadplyt="Nadpłytkowość a powikłania zakrzepowo-zatorowe, J. Treliński, Hematologia 2013, tom: 4, str: 43-50"
        witD="Rola oznaczania witaminy D w praktyce klinicznej, L. Napiórkowska, E. Franek, Choroby Serca i Naczyń 2009, tom: 6, str: 203-210"
        egrf="Wpływ wzorów (MDRD i CKD–EPI) do wyliczania eGFR, w klasyfikacji pacjentów do poszczególnych stadiów przewlekłej choroby nerek, U.Błazucka, M. Iwanowska, D. Bobilewicz, Diagnostyka Laboratoryjna 2019, tom: 55, str: 29-34, DOI: 10.5604/01.3001.0013.7328"      
        b12="Obraz kliniczny niedoboru witaminy B12 Opis przypadku i przegląd piśmiennictwa, Jan Żurek, Marta Zawadzka, Agnieszka Sawicka, Maria Mazurkiewicz-Bełdzińska, Polski Przegląd Neurologiczny 2021, tom: 17, str: 176-179, DOI: 10.5603/PPN.2021.0030."
        dodZakresy=[]
        #________________MORFOLOGIA________________
        for klucz,(wartosc, jednostka,zakresMin,zakresMax) in daneMorf.items():
            klucz1=klucz.lower() 
              
            if(zakresMin!='-' and zakresMax!='-'):
                wartosc=float(wartosc)
                zakresMax=float(zakresMax)
                zakresMin=float(zakresMin)
                if(wartosc<zakresMin):
                 
                    tabZaNiskoMorf.append(f'{klucz} {wartosc} {zakresMin} {zakresMax}')
                    self.tabWartMorf.append(f'Parametr: {klucz} wartość: {wartosc} zakresy: {zakresMin} - {zakresMax}')
    
                elif(wartosc>zakresMax):
            
                    tabZaWysokoMorf.append(f'{klucz} {wartosc} {zakresMin} {zakresMax}')
                    self.tabWartMorf.append(f'Parametr: {klucz} wartość: {wartosc} zakresy: {zakresMin} - {zakresMax}')
   
        for indMorf in range(0,len(tabZaNiskoMorf)):
            tekst=[]
            zrodla=[]
            if(('hematokryt' in tabZaNiskoMorf[indMorf].lower() or 'hct' in tabZaNiskoMorf[indMorf].lower() or'erytrocyty' in tabZaNiskoMorf[indMorf].lower() or 'rbc' in tabZaNiskoMorf[indMorf].lower() or 'hemoglobina' in tabZaNiskoMorf[indMorf].lower()) and not any('świdczyć o niedokrwistości' in string[0].lower() for string in self.tabelaMorf)):
                self.tabelaMorf.append(['Wartość hematorytu i\lub erytrocytów i\lub hemoglobiny jest za niska, co może świdczyć o niedokrwistości. ',diagSUM])
                
                hemoglobina= {k: v for k, v in daneMorf.items() if 'hemoglobina' in k.lower()}
                MCV={k: v for k, v in daneMorf.items() if 'mcv' in k.lower() }
                MCHC={k: v for k, v in daneMorf.items() if 'mchc' in k.lower() }
                if( any('hemoglobina' in s.lower() for s in tabZaNiskoMorf)):
                    if(float(next(iter(hemoglobina.values()))[0])>10 and float(next(iter(hemoglobina.values()))[0])<13.5):
                        tekst.append('Wartość hemoglobiny świadczy o łagodnej niedokrwistości. ')
                        if( not any(diagGUMED in t for t in zrodla)):
                            zrodla.append(diagGUMED)
                    elif(float(next(iter(hemoglobina.values()))[0])>8 and float(next(iter(hemoglobina.values()))[0])<9.9):
                        if( not any(diagGUMED in t for t in zrodla)):
                            zrodla.append(diagGUMED)
                        tekst.append('Wartość hemoglobiny świadczy o umiarkowanej niedokrwistości. ')
                    elif(float(next(iter(hemoglobina.values()))[0])>=6.5 and float(next(iter(hemoglobina.values()))[0])<7.9):
                        tekst.append('Wartość hemoglobiny świadczy o ciężkiej niedokrwistości. ')
                        if( not any(diagGUMED in t for t in zrodla)):
                            zrodla.append(diagGUMED)
                    elif(float(next(iter(hemoglobina.values()))[0])<6.5):
                        tekst.append('Wartość hemoglobiny świadczy o zagrażającej życiu niedokrwistości. ')
                        if(not any(diagGUMED in t for t in zrodla)):
                            zrodla.append(diagGUMED)
                    
                if(any('mcv' in s.lower() for s in tabZaNiskoMorf)):
                    tekst.append('Niska wartość MCV może świadzcyć o niedokrwistości mikrocytarnej. ')
                    if( not any(diagGUMED in t for t in zrodla)):
                        zrodla.append(diagGUMED)
                    if((float(next(iter(MCV.values()))[0])>72 and float(next(iter(MCV.values()))[0])<80) and (float(next(iter(MCHC.values()))[0])>=30 and float(next(iter(MCHC.values()))[0])<=34)):
                        tekst.append('Dana wartość MCV i MCHC może świadczyć o niedokrwistości mikrocytarnej normochromicznej, która może wskazywać na: chorobach nieinfekcyjnych, przewlekłych stanach zapalnych, chorobach endokrynologicznych, przewlekłych chorób wątroby i nerek. ')
                    elif((float(next(iter(MCV.values()))[0])>50 and float(next(iter(MCV.values()))[0])<=72) and  float(next(iter(MCHC.values()))[0])<=30):
                        tekst.append('Dana wartość MCV i MCHC może świadczyć o niedokrwistości mikrocytarnej hipochromicznej, która może wskazywać na niedobory żelaza, niedobór witaminy B6, zatrucie ołowiem lub talasemie. ')
                    if(not any('rdw' in s.lower() for s in tabZaNiskoMorf) and not any('rdw' in s.lower() for s in tabZaWysokoMorf)):
                        tekst.append('Prawidłowa wartość RDW i za niska wartość MCV świadczą o niedokrwistości jednorodnej mikrocytarnej, która może być spowodowana przez choroby zakaźne. ') 
                        if( not any(diagLab in t for t in zrodla)):
                            zrodla.append(diagLab)
                    elif(any('rdw' in s.lower() for s in tabZaWysokoMorf)):
                        tekst.append('Za niska wartość MCV i za wysoka wartość RDW mogą świadczyć o niedokriwstości niejednorodnej mikrocytowej, która może być powodowana przez niedobór żelaza. ')
                        if(not any(diagLab in t for t in zrodla)):
                            zrodla.append(diagLab)
                if((not any('mcv' in s.lower() for s in tabZaNiskoMorf) and not any('mcv' in s.lower() for s in tabZaWysokoMorf)) and(not any('rdw' in s.lower() for s in tabZaNiskoMorf) and not any('rdw' in s.lower() for s in tabZaWysokoMorf))):
                    tekst.append('Wartości MCV i RDW są w normie może świadczyć o niedokrwistości jednorodnej normocytowej, która może być powodowana prze choroby zakaźne. ')
                    if(  not any(diagLab in t for t in zrodla)):
                        zrodla.append(diagLab)
                if((not any('mcv' in s.lower() for s in tabZaNiskoMorf) and not any('mcv' in s.lower() for s in tabZaWysokoMorf)) and any('rdw' in s.lower() for s in tabZaWysokoMorf)):
                    tekst.append('Wartość MCV w normie i za wysoka wartość RDW może świadczyć o niedokrwistości niejednorodnej normocytowej, którą może powodować niedobór żelaza i kwasu foliowego. ')
                    if( not any(diagLab in t for t in zrodla)):
                        zrodla.append(diagLab)
                if((not any('rdw' in s.lower() for s in tabZaNiskoMorf) and not any('rdw' in s.lower() for s in tabZaWysokoMorf)) and any('mcv' in s.lower() for s in tabZaWysokoMorf)):
                    tekst.append('Prawidłowa wartość RDW i za wysoka wartość MCV może świadczyć o niedokrwistości jednorodnej makrocytowej. ')
                    if(not any(diagLab in t for t in zrodla)):
                        zrodla.append(diagLab)    
                if(any('mcv' in s.lower() for s in tabZaWysokoMorf) and any('rdw' in s.lower()for s in tabZaWysokoMorf)):
                    tekst.append('Za wysoka wartosć RDW i MCV mogą świadczyć o niedokrwistości niejednorodnej makrocytowej, co może być spowodowane niedoborem witaminy B12 lub kwasu foliowego. ')
                    if(not any(diagLab in t for t in zrodla)):
                        zrodla.append(diagLab)
                ''.join(tekst)        
                self.tabelaMorf.append([tekst,zrodla])
            if('mch' in tabZaNiskoMorf[indMorf].lower() and 'mchc' not in tabZaNiskoMorf[indMorf].lower()):
                self.tabelaMorf.append(['Za niska wartość MCH Może świadczyć o niedokriwostści, marskości wątroby.', hemat])
                
            if('mpv' in tabZaNiskoMorf[indMorf].lower()):
                self.tabelaMorf.append(['Zmniejszona wartość MPV może być spowodowana nadciśnieniem tętniczym, cukrzycą, niewydolnością nerek, wiekiem, wagą pacjenta lub paleniem papierosów. ', 'Mean platelet volume and platelet-large cell ratio as prognostic factors for coronary artery disease and myocardial infarction, Marcin Gawlita, Jarosław Wasilewski, Tadeusz Osadnik, Rafał Reguła, Kamil Bujak, Małgorzata Gonera, Folia Cardiologica 2015 10, str: 418-422, doi:10.5603/FC.2015.0079. '])
            if('leukocyty' in tabZaNiskoMorf[indMorf].lower()):
                self.tabelaMorf.append(['Zmniejszona wartość leukocytów może świadczyć o leukopenii, która mogą powodować: zakażenia, uszkodzenie szpiku kostnego, wstrząs anafilaktyczny. ',diagLab])
                   
            if( (any(limf in wiersz.lower() for wiersz in tabZaNiskoMorf for limf in ['limfocyty', 'lymph'])) and not any('Zmniejszona liczba limfocytów' in string[0] for string in self.tabelaMorf) ):
                self.tabelaMorf.append(['Zmniejszona liczba limfocytów może świadczyć o limfopeni, która może być powodowana niedoborami immunologicznymi, upośledzoną odpornością. ',[badaniaLab,diagSUM]])
            if (any(baso in wiersz.lower() for wiersz in tabZaNiskoMorf for baso in ['baso','bazo']) and not any('Zmniejszoną liczbę bazocytów' in string[0] for string in self.tabelaMorf) ):
                self.tabelaMorf.append(['Zmniejszoną liczbę bazocytów moga powodować przyjmowane leki, hormony. ', badaniaLab])
            if (any(eos in wiersz.lower() for wiersz in tabZaNiskoMorf for eos in ['eos','eoz']) and not any('Zmniejszoną liczbę eozynocytów' in string[0] for string in self.tabelaMorf)):
                self.tabelaMorf.append(['Zmniejszoną liczbę eozynocytów mogą powodować wstrząsy, ciężkie posocznice. ',badaniaLab])
            
            neu = ['neu', 'neu%', 'neutrocyty', 'neutrocytów', 'neut%', 'neut']
            if (any(n in tabZaNiskoMorf[indMorf].lower() for n in neu) and not any('Zmniejszona wartość neutrocytów' in string[0]for string in self.tabelaMorf) ):
                self.tabelaMorf.append(['Zmniejszona wartość neutrocytów może być spowodowana przez infekcje, zażywanie narkotyków, niedobóry witaminy B12, głodzenie. ',neutroArt])
                            
            if (any('mon' in wiersz.lower()for wiersz in tabZaNiskoMorf) and not any('Zmniejszona liczba monocytów' in string[0] for string in self.tabelaMorf) ): 
                self.tabelaMorf.append(['Zmniejszona liczba monocytów może świadczyć o zakażeniach, resekcji żołądka lub jelit. ',monoStr])
            
            if('płytki krwi' in tabZaNiskoMorf[indMorf].lower()):
                self.tabelaMorf.append(['Zmniejszona liczba płytek krwi może być spowodowana przyjmowaniem leków, upośledzonym wytwrzaniem płytek w szpiku kostnym.',badaniaLab])
        
        for indMorf in range(0,len(tabZaWysokoMorf)):
            
            if(('hematokryt' in tabZaWysokoMorf[indMorf].lower() or 'hct' in tabZaWysokoMorf[indMorf].lower() or'erytrocyty' in tabZaWysokoMorf[indMorf].lower() or 'rbc' in tabZaWysokoMorf[indMorf].lower() or 'hemoglobina' in tabZaWysokoMorf[indMorf].lower()) and not any('świdczyć o nadkrwistości' in string.lower() for string in self.tabelaMorf)):
                self.tabelaMorf.append(['Wartość hematorytu i\lub erytrocytów i\lub hemoglobiny jest za niska, co może świdczyć o nadkrwistości, odwodnieinu.',diagLab])
        
            if('mchc' in tabZaWysokoMorf[indMorf].lower()):
                self.tabelaMorf.append(['Za wysoka wartość MHCH może świadczyć o niedokrwistości lub odwodnieniu.',diagLab])
            if('mch' in tabZaWysokoMorf[indMorf] and 'mchc' not in tabZaWysokoMorf[indMorf]):
                self.tabelaMorf.append(['Za wysoka wartość mch może świdczyć o nieodborze żelaza, niedokrwistości, talasemie',hemat])
            if('mpv' in tabZaWysokoMorf[indMorf].lower()):
                self.tabelaMorf.append(['Zwiększona wartość MPV może być spowodowana nadciśnieniem tętniczym, cukrzycą, niewydolnością nerek, migotaniem przedsnionków.',platet])
            if('pct' in tabZaWysokoMorf[indMorf].lower()):
                self.tabelaMorf.append(['Wysokie stężenie PCT może być spowodowane chorobami zakaźnymi, stanami zapalnymi, przyjmowaniem niektórych leków. ','https://badaniakrwi.pl/co-oznacza-pct-norma-i-przyczyny-podwyzszonego-pct/'])
            if('leukocyty'in tabZaWysokoMorf[indMorf].lower()):
                self.tabelaMorf.append(['Zwiększona wartość leukocytów może świadczyć o leukocytozie, którą mogą powodować: uszkodzenia tkanek, zakażenia bakteryjne, grzybicze, wirusowe, stanay zapalne. uszkodzenia tkanek.',diagLab])
            if('płytki krwi' in tabZaWysokoMorf[indMorf].lower()):
                self.tabelaMorf.append(['Zbyt wysoka ilosć płytek krwi może być spowodowana przewlekłymi stanami zapalnymi, infekcjami, uszkodzeniami tkanek.',nadplyt])
            
            if( (any(limf in wiersz.lower() for wiersz in tabZaWysokoMorf for limf in ['limfo', 'lymph'])) and not any('Zwiększona liczba limfocytów ' in string[0] for string in self.tabelaMorf) ):

                self.tabelaMorf.append(['Zwiększona liczba limfocytów może świaczyć o monoukleozie, odrze, różyczce, zapaleniu wątroby, HIV, paleniu papierosów.',diagSUM]) 
            neu = ['neu', 'neu%', 'neutrocyty', 'neutrocytów', 'NEUT%', 'NEUT']
            if (any(n in tabZaWysokoMorf[indMorf].lower() for n in neu) and not any('Zwiększona wartość neutrocytów' in string[0] for string in self.tabelaMorf) ):
                self.tabelaMorf.append(['Zwiększona wartość neutrocytów może być spowodowana przez infekcje bakteryjne, zakażenie pasożytami, niektórymi \
                                        infekcjami wirusowymi, zakażenie grzybami.',diagSUM])
            if (any('mon' in wiersz.lower()for wiersz in tabZaWysokoMorf) and not any('Zwiększona liczba monocytów' in string[0] for string in self.tabelaMorf) ):
                self.tabelaMorf.append(['Zwiększona liczba monocytów może świadczyć o zapaleniu stawów, mononukleozie, zapaleniu mięśni, gruźlicy.',diagSUM])
            if (any(eos in wiersz.lower() for wiersz in tabZaWysokoMorf for eos in ['eos','eoz','kwaso']) and not any('Zwiększoną liczbę eozynocytów' in string[0] for string in self.tabelaMorf)):
                self.tabelaMorf.append(['Zwiększoną liczbę eozynocytów mogą powodować choroby alergiczne, choroby pasożytnicze, choroby skóry.',diagSUM])
            if (any(baso in wiersz.lower() for wiersz in tabZaWysokoMorf for baso in ['baso','bazo']) and not any('Zwiększoną liczbę bazocytów' in string[0] for string in self.tabelaMorf) ):
                self.tabelaMorf.append(['Zwiększoną liczbę bazocytów mogą powodować niewydolność nerek, leczenie estrogenami.',diagSUM]) 
         
      
            #__________________ANALITYKA__________________
        for klucz,(wartosc,jednostka,zakresMin,zakresMax)in daneAnalityka.items():
            if('materia' not in klucz.lower()):
                try:
                    wartosc=float(wartosc)
                    
                    if(wartosc<float(zakresMin)):
                        self.tabelaAnalityka.append(f'{klucz} wartość {wartosc} zakresMin {zakresMin} zakresMax {zakresMax}')
                        tabZaNiskoAnalityka.append(f'{klucz} {wartosc} {zakresMin} {zakresMax}')  
                        self.tabWartAnalityka.append(f'Parametr: {klucz} wartość: {wartosc} zakresy: {zakresMin} - {zakresMax}')              
                    elif(float(wartosc)>float(zakresMax)):
                        tabZaWysokoAnalityka.append(f'{klucz} {wartosc} {zakresMin} {zakresMax}')       
                        self.tabWartAnalityka.append(f'Parametr: {klucz} wartość: {wartosc} zakresy: {zakresMin} - {zakresMax}')               

                    
                except:

                    if('-' in wartosc):
                            wartosci=wartosc.split('-')
                            zakresy=zakresMin.split('-')
                            if(float(wartosci[1])>float(zakresy[1])):
                                tabNiepAnalityka.append(f'{klucz} {wartosc} {zakresMin} {zakresMax}')
                                self.tabWartAnalityka.append(f'Parametr: {klucz} wartość: {wartosc} zakresy: {zakresMin} - {zakresMax}')      
                    elif(wartosc.lower()!=zakresMin.lower() and zakresMin!='-'and wartosc!='w normie'):                    
                        tabNiepAnalityka.append(f"{klucz} {wartosc} {zakresMin}")
                        self.tabWartAnalityka.append(f'Parametr: {klucz} wartość: {wartosc} zakres: {zakresMin}')      
                    else:

                        if(klucz.lower()=='barwa' and(wartosc.lower()!='słomkowa' and 'żółt' not in wartosc.lower())):
                            tabNiepAnalityka.append(f'{klucz} {wartosc} {zakresMin}')
                            self.tabWartAnalityka.append(f'Parametr: {klucz} wartość: {wartosc} zakres: {zakresMin}')   
                        if(klucz.lower()=='przejrzystość' and (wartosc.lower()!='przejrzysty' and wartosc.lower()!='zupełna')):
                            tabNiepAnalityka.append(f'{klucz} {wartosc} {zakresMin}')
                            self.tabWartAnalityka.append(f'Parametr: {klucz} wartość: {wartosc} zakres: {zakresMin}')   
                        if('-' in wartosc):
                            wartosci=wartosc.split('-')
                            zakresy=zakresMin.split('-')
                           
                            
        for indAnalityka in range(0,len(tabNiepAnalityka)):
            if('przejrzystość' in tabNiepAnalityka[indAnalityka].lower()):
                self.tabelaAnalityka.append(['Przyczyną nieprawidłowej przejrzystości moczu mogą być elementy morfotyczne w moczu, przyjęcie kontrastu, nadmierny rozrost drobnoustrojów.',diagGUMED])
            if('leukocyty' in tabNiepAnalityka[indAnalityka].lower()):
                self.tabelaAnalityka.append(['Zwiększona liczba leukocytów w moczu może być spowodowana stanem zapalnym dróg moczowych, przyjmowaniem niektórych leków, odwodnieniem, niewydolnościa nerek.',badaniaLab])
            if('azotyny' in tabNiepAnalityka[indAnalityka].lower()):
                self.tabelaAnalityka.append(['Dodatni wynik azotynów w moczu może być spowodowany bakteryjnym zakażeniem układu moczowego.',diagGUMED])
            if('białko' in tabNiepAnalityka[indAnalityka].lower()):
                self.tabelaAnalityka.append(['Obecność białka w moczu może być spowodowana problemami z nerkami, niewydolnością krążenia.',badaniaLab])
            if('glukoza' in tabNiepAnalityka[indAnalityka].lower()):
                self.tabelaAnalityka.append(['Podwyżsozna wartość glukozy w moczu może być spowodowana cukrzycą, chorobami wątroby, zaburzeniami hormonalnymi.',diagGUMED])
            if('ciała ketonowe' in tabNiepAnalityka[indAnalityka].lower()):
                self.tabelaAnalityka.append(['Podwyższona wartość ciał ketonowych w moczu może być spowodowana odwodnieniem, gorączką, zatruciami, wysiłkiem fizycznym, głodzeniem, cukrzycą, dietą bogatotłuszczową.',diagSUM])
            if('urobilinogen'in tabNiepAnalityka[indAnalityka].lower()):
                self.tabelaAnalityka.append(['Zwiększona zawartość urobilinogenu w moczu może być spowodowana upośledzoną czynnością wątroby, niedokrwistością.',diagSUM])
            if('bilirubina' in tabNiepAnalityka[indAnalityka].lower()):
                self.tabelaAnalityka.append(['Dodatnia wartość bilirubiny w moczu może być spowodowana chorobami wątroby, chorobami dróg żółciowych.',diagLab])
            if('śluz' in tabNiepAnalityka[indAnalityka].lower()):
                self.tabelaAnalityka.append(['Większa zawartość śluzu w moczu może być spowodowana chorobami zapalnymi nerek.',diagLab])
            if('bakterie' in tabNiepAnalityka[indAnalityka].lower()):
                self.tabelaAnalityka.append(['Zbyt duża ilość bakterii w moczu może być spowodowana zakażeniem dróg moczowych.',badaniaLab])
            
           
            if(('erytrocyty' in tabNiepAnalityka[indAnalityka].lower()or 'krew' in tabNiepAnalityka[indAnalityka].lower()) and not any('Większa ilość erytrocytów' in string[0] for string in self.tabelaAnalityka)):
                self.tabelaAnalityka.append(['Większa ilość erytrocytów w moczu może być spowodowana zapaleniami i gruźlicą układu moczowego i kamicy nerkowej.',diagLab])
            if('barwa' in tabNiepAnalityka[indAnalityka].lower()):
                self.tabelaAnalityka.append([ 'Nieprawidłowa barwa moczu może być spowodowana obecnością krwi, spożyciem niektórych potraw, przyjmowaniem niektórych leków, ilością bilirubiny w moczu.',diagLab])  
        for indAnalityka in range(0,len(tabZaNiskoAnalityka)-1):
            if('ciężar właściwy' in tabZaNiskoAnalityka[indAnalityka].lower()):
                self.tabelaAnalityka.append(['Za niska wartość ciężaru właściwego może być spowodowana upośledzeniem funkcji zagęszczaina moczu, niewydolnością nerek, nadmierną podażą płynów.',diagSUM])
            if('ph' in tabZaNiskoAnalityka[indAnalityka].lower()):
                self.tabelaAnalityka.append(['Zbyt kwaśny odczyn moczu może być spowodowany dietą wysokobiałkową, głodzeniem, przyjmowaniem niektórych leków, chorobami nerek, odwodnieniem.',diagSUM])
        for indAnalityka in range(0,len(tabZaWysokoAnalityka)):
            if('ciężar właściwy' in tabZaWysokoAnalityka[indAnalityka].lower()):
                self.tabelaAnalityka.append(['Za wysoka wartość ciężaru właściwego może być spowodowana odwodnieniem, białkomoczem, po podaniu środków kontrastowych.',diagSUM])     
            if('ph' in tabZaWysokoAnalityka[indAnalityka].lower()):
                self.tabelaAnalityka.append(['Zbyt zasadowy odczyn moczu może być spowodowany dietą wegetariańską, przyjmowaniem niektórych leków.',diagSUM])   
            if('bakterie' in tabZaWysokoAnalityka[indAnalityka].lower()):
                self.tabelaAnalityka.append(['Zbyt duża ilość bakterii w moczu może być spowodowana zakażeniem dróg moczowych.',badaniaLab])
            if('leukocyty' in tabZaWysokoAnalityka[indAnalityka].lower()):

                self.tabelaAnalityka.append(['Zwiększona liczba leukocytów w moczu może być spowodowana stanem zapalnym dróg moczowych, przyjmowaniem niektórych leków.',badaniaLab])
            if('erytrocyty' in tabZaWysokoAnalityka[indAnalityka].lower()or'krew' in tabZaWysokoAnalityka[indAnalityka].lower() ):
                self.tabelaAnalityka.append(['Większa ilość erytrocytów w moczu może być spowodowana zapaleniami i gruźlicą układu moczowego i kamicy nerkowej.',diagLab])
            if('śluz' in tabZaWysokoAnalityka[indAnalityka].lower()):
                self.tabelaAnalityka.append(['Większa zawartość śluzu w moczu może być spowodowana chorobami zapalnymi nerek.',diagLab])
        #_______________IMMUNOCHEMIA_______________
        for klucz,(wartosc,jednostka,zakresMin,zakresMax) in daneImmunochemia.items():
            if(any(parametr.lower() in klucz.lower() for parametr in parametryImmunochemiczne)):

                try:
                    wartosc= float(wartosc)
                    zakresMin= float(zakresMin)
                    zakresMax=float(zakresMax)
                    if(wartosc<zakresMin):
                        
                        self.tabWartImmuno.append(f'Parametr: {klucz} wartość: {wartosc} zakresy: {zakresMin} - {zakresMax}')
                        tabZaNiskoImmuno.append(f'{klucz} {wartosc} {zakresMin} {zakresMax}')
                    elif(wartosc>zakresMax):
                    
                        self.tabWartImmuno.append(f'Parametr: {klucz} wartość: {wartosc} zakresy: {zakresMin} - {zakresMax}')
                        tabZaWysokoImmuno.append(f'{klucz} {wartosc} {zakresMin} {zakresMax}')
                    
                except:
                    if(zakresMin!='-'):
                        if('zakresy.xml' in zakresMin):
                            dod_zakres=  self.odczytZakresow.AnalizaDodatkowychZakresow(klucz,wartosc,jednostka,zakresMin)
                        if('witamina d' in dod_zakres.lower() and ('niedobór' in dod_zakres or 'stężenie niewystarczające' in dod_zakres)):
                                self.tabelaImmunochemia.append(['Zmniejszona zawartość  witaminy D  może być spowodowany niewystarczającą podażą w diecie, zmniejszonym wchłanianiem, niewydolnością nerek , wątroby.',witD])
                        if('witamina d' in dod_zakres.lower() and('stężenie wysokie' in dod_zakres or 'stężenie potencjalnie toksyczne' in dod_zakres)):
                            self.tabelaImmunochemia.append(['Stężenie Witaminy D jest za wysokie, przyczyną tego może być za dużą podażą tej witaminy.',witD])
                            self.tabWartImmuno.append(f'Parametr: {klucz} wartość: {wartosc}')
                        
        for indImmuno in range(0,len(tabZaNiskoImmuno)):
            if('ferrytyna' in tabZaNiskoImmuno[indImmuno].lower()):
                self.tabelaImmunochemia.append(['Obniżona zawartość ferrytyny może być spowodowane obniżoną zawartością żelaza, krwotokami, zaburzeniami wchłaniania żelaza.',diagSUM])
            if('glukoza' in tabZaNiskoImmuno[indImmuno].lower() and not any('hipoglikemia' in string[0].lower() for string in self.tabelaImmunochemia)):
                self.tabelaImmunochemia(['Za niska wawrtość glukozy - hipoglikemia może byc spowodowana niedostateczna podażą węglowodanów, nadmierna utratą glukozy z moczem, nadmiernym zużyciem glukozy, upośledzonym wchałanianiem glukozy.',badaniaLab])
            if('kortyzol' in tabZaNiskoImmuno[indImmuno].lower()):
                self.tabelaImmunochemia.append(['Za niska wartość kortyzolu może być spowodowana niewydolnością kory nadnerczy oraz zaburzeniami biosyntezt kortyzolu.',badaniaLab])
            if('prolaktyna' in tabZaNiskoImmuno[indImmuno].lower()):
                self.tabelaImmunochemia.append(['Za niski poziom prolaktyny może świadczyć o zniszczeniu przysadki gruczołowej, defektem biosyntezy prolaktyny, przyjmowaniem niektórych leków.',badaniaLab])   
            if('tsh' in tabZaNiskoBiochem[indImmuno].lower()): 
                if(any('ft3' in string.lower() for string in tabZaWysokoImmuno) and any('ft4' in string.lower() for string in tabZaWysokoImmuno) ):
                    self.tabelaImmunochemia.append(['Zmniejszona wartość TSH, podwyższona wartość FT4 oraz FT3 mogą być spowodowane nadczynnością pierowtną tarczycy.',diagSUM])
                elif(any('ft3' in string.lower() for string in tabZaWysokoImmuno) and not any('ft4' in string.lower() for string in tabZaWysokoImmuno) ):
                    self.tabelaImmunochemia.append(['Zmniejszona wartosć TSH i podwyżsozna wartosć FT3 może być spowodowane nadczynnością pierwotną tarczycy.',diagSUM])
                elif(any('ft4' in string.lower() for string in tabZaWysokoImmuno) and not any('ft3' in string.lower() for string in tabZaWysokoImmuno) ):
                    self.tabelaImmunochemia.append(['Zmniejszona wartosć TSH i podwyżsozna wartosć FT4 może być spowodowane nadczynnością pierwotną tarczycy.',diagSUM])
                else:
                    self.tabelaImmunochemia.append(['Zmniejszona wartość TSH może być spowodowana niedoczynnością tarczycy lub nadczynnością.',diagSUM])
                
                
                if(any('ft3' in string.lower() for string in tabZaNiskoImmuno) and any('ft4' in string.lower() for string in tabZaNiskoImmuno) ):
                    self.tabelaImmunochemia.append(['Zmniejszona wartość TSH, zmniejszona wartość FT4 oraz FT3 mogą być spowodowane niedoczynnością wtórną tarczycy.',diagSUM])
                elif(any('ft3' in string.lower() for string in tabZaNiskoImmuno) and not any('ft4' in string.lower() for string in tabZaNiskoImmuno) ):
                    self.tabelaImmunochemia.append(['Zmniejszona wartosć TSH i zmniejszona wartosć FT3 może być spowodowane niedoczynnością wtórną tarczycy.',diagSUM])
                elif(any('ft4' in string.lower() for string in tabZaNiskoImmuno) and not any('ft3' in string.lower() for string in tabZaNiskoImmuno) ):
                    self.tabelaImmunochemia.append(['Zmniejszona wartosć TSH i zmniejszona wartosć FT4 może być spowodowane niedoczynnością wtórną tarczycy.',diagSUM])
                    
        for indImmuno in range(0,len(tabZaWysokoImmuno)):
            if('ferrytyna' in tabZaWysokoImmuno[indImmuno].lower()):
                self.tabelaImmunochemia.append(['Podwyższona wartość ferrytyny świadczy o za wysokiej wartości żelaza, co może być spowodowane problemami dystrybucji żelazem, stanami zapalnymi.',diagSUM])
                if any('niska wartośc witaminy b12' in string.lower() for string in self.tabelaImmunochemia):
                    self.tabelaImmunochemia.append(['Obniżona wartość witaminy B12 może świdczyć o tym, że jest to przyczyną podwyższonej ferrytyny.',diagSUM])
            if('peroksydazie tarczycowej' in tabZaWysokoImmuno[indImmuno].lower()):
                self.tabelaImmunochemia.append(['Podwyższony parametr anty-TPO może świadczyć o chorobie Hashimoto.',diagSUM])
            if('psa' in tabZaWysokoImmuno[indImmuno].lower()):
                self.tabelaImmunochemia.append(['Za wysokie stężenie PSA może być spowodowane stanem zapalnym gruczołu krokowego lub przerostem łagodnym tego gruczołu, niewydolnoscią nerek, żółtaczką lub cukrzycą.',badaniaLab]) 
            if('prolaktyna' in tabZaWysokoImmuno[indImmuno].lower()):
                self.tabelaImmunochemia.append(['Za wysoki poziom prolaktyny może być spowodowany uszkodzeniem funkcji podwzgórza, nadmierną sekrecją prolaktyny.',badaniaLab])
            if('atg' in tabZaWysokoImmuno[indImmuno].lower()):
                self.tabelaImmunochemia.append(['Podwyżsozna wartość ATG może być spowodowana chorobą Hashimoto.',diagSUM])
            if('glukoza' in tabZaWysokoImmuno[indImmuno].lower() and not any('hiperglikemia' in string[0].lower() for string in self.tabelaImmunochemia)):
                self.tabelaImmunochemia.append(['Podwyższona wartość glukozy - hiperglikemia może świadzyć o niedoborze insuliny, przyjmowanymi lekami, stanami zapalnymi, zawałem mięśnia sercowego.',badaniaLab])
            if('kortyzol' in tabZaWysokoImmuno[indImmuno].lower()):
                self.tabelaImmunochemia.append(['Za wysoka wartość kortyzolu może być spowodowana depresją, problemami korą nadnerczy.',badaniaLab])
          
            if('tsh' in tabZaWysokoImmuno[indImmuno].lower()):
                if(any('ft3' in string.lower() for string in tabZaWysokoImmuno) and any('ft4' in string.lower() for string in tabZaWysokoImmuno) ):
                    self.tabelaImmunochemia.append(['Za wysoka wartość TSH, podwyższona wartość FT4 oraz FT3 mogą być spowodowane nadczynnością wtórną tarczycy.',diagSUM])
                elif(any('ft3' in string.lower() for string in tabZaWysokoImmuno) and not any('ft4' in string.lower() for string in tabZaWysokoImmuno) ):
                    self.tabelaImmunochemia.append(['Za wysoka wartosć TSH i podwyżsozna wartosć FT3 może być spowodowane nadczynnością wtórną tarczycy.',diagSUM])
                elif(any('ft4' in string.lower() for string in tabZaWysokoImmuno) and not any('ft3' in string.lower() for string in tabZaWysokoImmuno) ):
                    self.tabelaImmunochemia.append(['Za wysoka wartosć TSH i podwyżsozna wartosć FT4 może być spowodowane nadczynnością wtórną tarczycy.',diagSUM])
                else:
                    self.tabelaImmunochemia.append(['Za wysoka wartość TSH może być spowodowana niedoczynnością tarczycy lub nadczynnością.',diagSUM])
                
                
                if(any('ft3' in string.lower() for string in tabZaNiskoImmuno) and any('ft4' in string.lower() for string in tabZaNiskoImmuno) ):
                    self.tabelaImmunochemia.append(['Za wysoka wartość TSH, zmniejszona wartość FT4 oraz FT3 mogą być spowodowane niedoczynnością pierwotną tarczycy.',diagSUM])
                elif(any('ft3' in string.lower() for string in tabZaNiskoImmuno) and not any('ft4' in string.lower() for string in tabZaNiskoImmuno) ):
                    self.tabelaImmunochemia.append(['Za wysoka wartosć TSH i zmniejszona wartosć FT3 może być spowodowane niedoczynnością pierwotną tarczycy.',diagSUM])
                elif(any('ft4' in string.lower() for string in tabZaNiskoImmuno) and not any('ft3' in string.lower() for string in tabZaNiskoImmuno) ):
                    self.tabelaImmunochemia.append(['Za wysoka wartosć TSH i zmniejszona wartosć FT4 może być spowodowane niedoczynnością pierwotną tarczycy.',diagSUM])
                    
        #_______________BIOCHEMIA_______________
        for klucz,(wartosc,jednostka,zakresMin,zakresMax) in daneBiochemia.items():
            if(any(parametr.lower() in klucz.lower() for parametr in parametryBiochemiczne )):
                try:
                    wartosc=float(wartosc)
                    zakresMin=float(zakresMin)
                    zakresMax=float(zakresMax)
                    if(wartosc<zakresMin):
                    
                        tabZaNiskoBiochem.append(f'{klucz} {wartosc} {zakresMin} {zakresMax}')
                        self.tabWartBiochem.append(f'Parametr: {klucz} wartość: {wartosc} zakresy: {zakresMin} - {zakresMax}')
                        
                    elif(wartosc>zakresMax):
                        print(f'Za wysoka wartość {klucz} wartosc {wartosc} zakresMin {zakresMin} zakresMax {zakresMax}')
                        tabZaWysokoBiochem.append(f'{klucz} {wartosc} {zakresMin} {zakresMax}')
                        self.tabWartBiochem.append(f'Parametr: {klucz} wartość: {wartosc} zakresy: {zakresMin} - {zakresMax}')
                    
                except:
                    if('zakresy.xml' in zakresMin):
                        dodZakresy.append(f'{self.odczytZakresow.AnalizaDodatkowychZakresow(klucz,wartosc,jednostka,zakresMin)}')
                        dod_zakres=self.odczytZakresow.AnalizaDodatkowychZakresow(klucz,wartosc,jednostka,zakresMin)
                        dod_zakres_low=dod_zakres.lower()
                        zMin=dod_zakres.split('-')
                        if('Witamina D' in dod_zakres_low and ('niedobór' in dod_zakres_low or 'stężenie niewystarczające' in dod_zakres_low)):
                            self.tabelaBiochemia.append(['Zmniejszona wartość  witaminy D  może być spowodowana niewystarczającą podażą w diecie, \
                                                zmniejszonym wchałanianiem z przewodu pokarmowego, stanami zapalnymi w wątrobie lub nerkach.',witD])
                            self.tabWartBiochem.append(f'Parametr: {klucz} wartość: {wartosc}')
                        if('Witamina D' in dod_zakres and('stężenie wysokie' in dod_zakres_low or 'stężenie potencjalnie toksyczne' in dod_zakres_low)):
                            self.tabelaBiochemia.append(['Stężenie witaminy D jest za wysokie, przyczyną tego może być za duża podaż tej witaminy.',witD])                
                            self.tabWartBiochem.append(f'Parametr: {klucz} wartość: {wartosc}')
                        if('ldl' in dod_zakres_low):
                            opis=dod_zakres_low.split('-')
                            if('dla' in dod_zakres_low):
                                self.tabelaBiochemia.append([f'Wartość stężenia cholesterolu LDL jest spełniona {opis[len(opis)-1]} sercowo - naczyniowego.','Skala SCORE'])
                                self.tabWartBiochem.append(f'Parametr: {klucz} wartość: {wartosc}')
                            elif('nie spełnia' in opis[len(opis)-1]):
                                self.tabelaBiochemia.append(['Wartość stężenia cholesterolu LDL jest za wysoka dla wszystkich.','Skala SCORE'])
                                self.tabWartBiochem.append(f'Parametr: {klucz} wartość: {wartosc}')
                            elif('triglicer' in dod_zakres_low):
                                o=dod_zakres.split('-')
                                self.tabelaBiochemia.append([f'{o[len(o)-1]}',"sprawozdanie z badań"])
                                self.tabWartBiochem.append(f'Parametr: {klucz} wartość: {wartosc}')
                        if('nie-hdl' in dod_zakres_low):
                            if('dla' in dod_zakres_low):
                                self.tabelaBiochemia.append([f'Wartość stężenia cholesterolu nie - HDL jest spełniona {opis[len(opis)-1]} sercowo-naczyniowego','Skala SCORE'])
                                self.tabWartBiochem.append(f'Parametr: {klucz} wartość: {wartosc}')
                            else:
                                self.tabelaBiochemia.append(['Wartość stężenia cholesterolu nie - HDL jest za wysoka dla wszystkich.','Skala SCORE']) 
                                self.tabWartBiochem.append(f'Parametr: {klucz} wartość: {wartosc}')                      
                        if('egfr' in dod_zakres_low):
                            self.tabelaBiochemia.append(['Za niska wartość EGFR może świadczyć o nieprawidłowej pracy nerek.',egrf])
                            self.tabWartBiochem.append(f'Parametr: {klucz} wartość: {wartosc}')
                        if('cholesterol całkowity' in dod_zakres):
                            self.tabelaBiochemia.append(['Zwiększona wartość cholesterolu całkowitego może być spowodowana nadmierną podażą w pokarmach, upośledzonym wydalaniem cholesterolu, upośledzeniem przemian metabolicznych cholesterolu.',badaniaLab])
                            self.tabWartBiochem.append(f'Parametr: {klucz} wartość: {wartosc} zakresy: {zakresMin}-{zakresMax}')
                        if('glukoza' in dod_zakres_low):
                            opis=dod_zakres_low.split('-')
                            if('glikemii' in opis[len(opis)-1]):
                                self.tabelaBiochemia.append([f'Wartość glukozy świadczy o {opis[len(opis)-1]}',"Sprawozdanie z badań laboratoryjnych."])
                                self.tabWartBiochem.append(f'Parametr: {klucz} wartość: {wartosc}')
                            elif('za nisko'in opis[len(opis)-1]):
                                self.tabelaBiochemia.append(['Wartość glukozy jest za niska, powodem może być niedostateczna podaż węglowodanów w pokarmach, nadmiernym zużyciem glukozy, upośledzonym wchłanainiem glukozy z przewodu pokarmowego, niedoborem danych hormonów.',badaniaLab])            
                                self.tabWartBiochem.append(f'Parametr: {klucz} wartość: {wartosc}')
                            elif('za wysoka'in opis[len(opis)-1]):
                                self.tabelaBiochemia.append(['Za wysoka wartość glukozy może być spowodowana przez cukrzycę, przyjmowaniem niektórych leków, zstanami zapalnymi.',badaniaLab])                
                                self.tabWartBiochem.append(f'Parametr: {klucz} wartość: {wartosc}')
                        if('wskaźnik aterogenny' in dod_zakres_low):
                            opis=dod_zakres_low.split('-')
                            opis=opis[len(opis)-1]
                            if('spełniona' in opis):
                                self.tabelaBiochemia.append([f'Wartość wskaźnika aterogennego {opis}',""])
                                self.tabWartBiochem.append(f'Parametr: {klucz} wartość: {wartosc}')
                            else:
                                self.tabelaBiochemia.append(['Wskaźnik aterogenności ma za wysoka wartość, powodem może być zbyt duża podaż tłuszczy w diecie, palenie papierosów, nadużywanie alkoholu.',atero]) 
                                self.tabWartBiochem.append(f'Parametr: {klucz} wartość: {wartosc}')
            
                    elif( wartosc.startswith('<') or wartosc.startswith('>')):
                        if(wartosc!=zakresMin):
                            if('alkohol etylowy'in klucz.lower() and wartosc!='<0.20'):
                                tabZaWysokoBiochem.append(f'{klucz} {wartosc} {zakresMin} {zakresMax}')
                                self.tabWartBiochem.append(f'Parametr: {klucz} wartość: {wartosc} zakresy: {zakresMin} - {zakresMax}') 
                          
        for indBiochem in range(0,len(tabZaNiskoBiochem)):
            if('witamina' in tabZaNiskoBiochem[indBiochem].lower() and 'b12' in tabZaNiskoBiochem[indBiochem].lower()):
            
                self.tabelaBiochemia.append(["Za niska wartość witaminy B12, może być spowodowana dietą ubogą w tą witaminę, zaburzeniami jej wchłaniania, lub jej nieprawidłowym transportem.",b12])
            
            if('ferrytyna' in tabZaNiskoBiochem[indBiochem].lower()):
                self.tabelaBiochemia.append(['Obniżona zawartość ferrytyny może być spowodowane obniżoną zawartością żelaza, krwotokami, zaburzeniami wchłaniania żelaza.',diagSUM])
            if('glukoza' in tabZaNiskoBiochem[indBiochem].lower() and not any('hipoglikemia' in string[0].lower() for string in self.tabelaBiochemia)):
                self.tabelaBiochemia(['Za niska wawrtość glukozy - hipoglikemia może byc spowodowana niedostateczną podażą węglowodanów, nadmierną utratą glukozy z moczem, nadmiernym zużyciem glukozy, upośledzonym wchałanianiem glukozy.',badaniaLab])
            if('sód' in tabZaNiskoBiochem[indBiochem].lower()):
                self.tabelaBiochemia.append(['Mniejsza wartość sodu może świadczyć o utracie sodu wraz z odwodnieniem (wymiotami, biegunką, przetokami przewodu pokarmowego, utratą sodu przez skórę (nadmierne pocenie się)), nadmiernym działaniem wazopresyny.',badaniaLab])       
            if('potas' in tabZaNiskoBiochem[indBiochem].lower()):
                self.tabelaBiochemia.append(['Wartość potasu poniżej normy może świadczyć o niedostatecznej podaży potasu, utratą potasu przez przewód pokarmowy lub nerki, transmineralizacji.',badaniaLab])
            if('magnez' in tabZaNiskoBiochem[indBiochem].lower()):
                self.tabelaBiochemia.append(['Za niska wartość magnezu może być spowodowana niedostateczną podażą magnezu z pokarmami, zaburzeniami wchłaniania, nadmierną utratą wraz z moczem, nadczynnością tarczycy, chorobami kości, nadmiernym odkładaniem się w mięśniach.',badaniaLab])
            if('wapń' in tabZaNiskoBiochem[indBiochem].lower()):
                self.tabelaBiochemia.append(['Za niska wartość wapnia może świadczyć o upośledzeniu biosyntezy lub sekrecji PTH, nadmierną utratą wapnia wraz z moczem, nadmiernym odkładaniem w tkankach, upośledzonym wchłanianiem wapnia z przewodu pokarmowego, niedoborem witaminy D3.',badaniaLab])
                if( any ('magnez' in string.lower() for string in tabZaNiskoBiochem)):
                    self.tabelaBiochemia.append(['Przyczyną za niskiej wartości wapnia może być niedobór magnezu.',badaniaLab])
                if(any(all(s in string.lower() for s in ['witamina','d','niedobór'])  for string in dodZakresy)):
                    self.tabelaBiochemia.append(['Niedobór wapnia może być spowodowany niedoborem witaminy D.',badaniaLab])
            if('żelazo' in tabZaNiskoBiochem[indBiochem].lower()):
                self.tabelaBiochemia.append(['Niska wartość żelaza może być spowodowana niedostateczną podażą żelaza w pokarmach, upośledzonym wchłaniaiem w przewodzie pokarmowym, utratą żelaza przez krwotoki, nadmiarnym odkładaniem się zelaza w tkankach.',badaniaLab])
            if('alp' in tabZaNiskoBiochem[indBiochem].lower()):
                self.tabelaBiochemia.append(['Niższa zawartość ALP może być spowodowana niedoborem witaminy C, niedoczynnością tarczycy, wrodzonym defektem metabolicznym.',badaniaLab])
            if('albumina' in tabZaNiskoBiochem[indBiochem].lower()):
                self.tabelaBiochemia.append(['Za niskie stężenie albuminy może być spowodowane wrodzonym defektem biosyntezy, niedostateczną podażą białka, upośledzieniem wchłaniania białka z przewodu pokarmowego, niedoczynnością tarczycy, nadmierną utratą białka.',badaniaLab])      
            if('mocznik' in tabZaNiskoBiochem[indBiochem].lower()):
                self.tabelaBiochemia.append(['Za niskie stężenie mocznika może świadczyć o przewodnieniu, stosowaniu androgenów, diecie niskobiałkowej.',diagLab])
            if('kreatynina' in tabZaNiskoBiochem[indBiochem].lower()):
                self.tabelaBiochemia.append(['Za niska wartość kreatyniny może być spowodowana dietą wegetariańską, niewydolnością wątroby, niska masa mięśniowa.',kreat])
        for indBiochem in range(0,len(tabZaWysokoBiochem))  :
            if('witamina' in tabZaWysokoBiochem[indBiochem].lower() and 'b12' in tabZaWysokoBiochem[indBiochem].lower()):
                self.tabelaBiochemia.append(['Za wysokie stężenie witaminy B12 może być spowodowane chorobami wątroby.',badaniaLab]) 
            if('ferrytyna' in tabZaWysokoBiochem[indBiochem].lower()):
                self.tabelaBiochemia.append(['Podwyższona wartość ferrytyny świadczy o za wysokiej wartości żelaza, problemach dystrybucji żelazem, zaburzeniach syntezy hemoglobiny.',diagSUM])

                if any('niska wartośc witaminy b12' in string.lower() for string in self.tabelaBiochemia):
                    self.tabelaBiochemia.append(['Obniżona wartość witaminy B12 może świdczyć o tym, że jest to przyczyną podwyższonej ferrytyny.',diagSUM])
            if(('alt' in tabZaWysokoBiochem[indBiochem].lower() or 'AST' in tabZaWysokoBiochem[indBiochem])and not any('aminotransferaz' in string[0].lower() for string in self.tabelaBiochemia)):
                self.tabelaBiochemia.append(['Wyższa wartość aminotransferaz(AST lub ALT) świadczy o uszkodzeniu lub martwiy tkanek. Może to być spowodowane uszkodzeniem wątroby, marwicą mięśnia sercowego, uszkodzeniem płuc lub mózgu, chorobami mięśni szkieletowych.',badaniaLab])   
            if('triglicerydy' in tabZaWysokoBiochem[indBiochem].lower()):
                self.tabelaBiochemia.append(['Zwiększona liczba triglicerydów może świadczyć o nadmiernym spożywaniu triglicerydów, niedoczynnością tarczycy, alkoholiźmie, niewydolności nerek.',badaniaLab])     
            if('kreatynina' in tabZaWysokoBiochem[indBiochem].lower()):
                self.tabelaBiochemia.append(['Podwyżsozna wartość kreatyniny świadczy o niewydolności wydalniczej nerek.',badaniaLab]) 
            if('glukoza' in tabZaWysokoBiochem[indBiochem].lower()):
                self.tabelaBiochemia.append(['Podwyższona wartość glukozy - hiperglikemia może świadzyć o niedoborze insuliny, przyjmowanymi lekami, stanami zapalnymi, zawałem mięśnia sercowego.',badaniaLab])
            if('sód' in tabZaWysokoBiochem[indBiochem].lower()):
                self.tabelaBiochemia.append(['Podwyższona wartość sodu może swiadczyć o nadmiernej podaży sody, utratcie hipolitycznych płynów (przez skórę, przewód pokarmowy, nerki), stanach gorączkowych, nadczynności tarczycy.',badaniaLab])
            if('potas' in tabZaWysokoBiochem[indBiochem].lower()):
                self.tabelaBiochemia.append(['Za wysoka wartosć potasu może śwadczyć o nadmiernej podaży potasu, upośledzonym wydalaniu potasu przez nerki, nadmiernym uwalnianiem potasu z komórek.',badaniaLab])  
                self.tabelaBiochemia.append(['Za wysokie stężenie bilirubiny może być związane z uszkodzneiem hepatocytów, cholestazą wewnątrzwątrobową, wzmożoną hemolizą, uszkodzniem procesów estryfikacji.',badaniaLab])
            if('ggtp' in tabZaWysokoBiochem[indBiochem].lower()):
                self.tabelaBiochemia.append(['Przyczyną zwiększonej wartości GGTP może być cholestaza, uszkodzenie wątroby, nadużywanie alkoholu, naciekanie miąszu wątroby.',diagSUM])
            if('magnez'in tabZaWysokoBiochem[indBiochem].lower()):
                self.tabelaBiochemia.append(['Zbyt wysoka wartość magnezu może być spowodowana nadmierną podażą soli magnezowych, upośledzonym wydalaniu magnezu przez nerki, niedoczynnością tarczycy.',badaniaLab])
            if('crp' in tabZaWysokoBiochem[indBiochem].lower()):
                self.tabelaBiochemia.append(['Powodem zbyt wysokiej wartości CRP mogą być stany zapalne, martwica tkanki. Wyższa wartość CRP (do 25 mg/l) może występować u osób palących papierosy.',diagSUM])
            if('wapń' in tabZaWysokoBiochem[indBiochem].lower()):
                self.tabelaBiochemia.append(['Nadmierna wartość wapnia może świadczyć o nadmiernym wchłanianiu wapnia z przewodu pokarmowego, spadku wydalania wapnia z moczem, wzmożonej mobilizacji wapnia z kości.',badaniaLab])
                if(any(all(s in string.lower() for s in ['witamina','d','stęzenie wysokie'])  for string in dodZakresy) or any(all(s in string.lower() for s in ['witamina','d','stężenie potencjalnie toksyczne'])  for string in dodZakresy)):
                    self.tabelaBiochemia.append(['Wysokie stężenie wapnia może byc spodowane wysoką wartością witaminy D.',badaniaLab])
            if('żelazo' in tabZaWysokoBiochem[indBiochem].lower()):
                self.tabelaBiochemia.append(['Za wysoka wartośc żelaza może być spowodowana nadmierną podażą żelaza w pokarmach, nadmiernym wchłanianiem żelaza w przewodzie pokarmowym, nadmiernym uwalnianiem żelaza z komórek.',badaniaLab])
            if('alp' in tabZaWysokoBiochem[indBiochem].lower()):
                self.tabelaBiochemia.append(['Podwyższona zawartość ALP może być spowodowana nadmierną aktywnością osteoblastów, upośledzonym wydzialniem ALP przez drogi żółciowe.',badaniaLab])
            if('albumina' in tabZaWysokoBiochem[indBiochem].lower()):
                self.tabelaBiochemia.append(['Za wysoka wartość albuminy jest najczęściej powodowana odwonieniem.',badaniaLab])
            if('mocznik' in tabZaWysokoBiochem[indBiochem].lower()):
                self.tabelaBiochemia.append(['Podwyższone stężenie mocznika może świadczyć o odwodnieniu, wzmożeniu ketabolizmu białkowym, gorączce, nadczynności tarczycy.',diagLab])
            if('cholesterol całkowity' in tabZaWysokoBiochem[indBiochem].lower()):
                self.tabelaBiochemia.append(['Zwiększona wartość cholesterolu całkowitego może być spowodowana nadmierną podażą w pokarmach, upośledzonym wydalaniem cholesterolu, upośledzeniem przemian metabolicznych cholesterolu.',badaniaLab])
        self.generowanie.GenerowaniePlikuPDF(self.tabelaMorf,self.tabelaAnalityka,self.tabelaBiochemia,self.tabelaImmunochemia,danePacjenta, self.tabWartMorf,self.tabWartBiochem,self.tabWartImmuno,self.tabWartAnalityka)      

        