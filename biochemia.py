import re
class Biochemia:
    def OdczytWynikowBiochemicznych(self,indexBiochem,indexNextBiochem,line):
        daneBiochemia={}
        for k in range(indexBiochem,indexNextBiochem):
                linijka=line[k].split(' ')
                linijka= list(filter(lambda x: x != '' , linijka))
                linijka= list(filter(lambda x: x != '↑', linijka))
                linijka= list(filter(lambda x: x != '↓', linijka))
              
                linijka = [slowo.replace(',', '.') for slowo in linijka]
                wartość=""
                jednostka=""
                zakresMin=""
                zakresMax=""
                nazwa=""
                z=0
                for ind in range(0,len(linijka)):
                    if(re.search(r'\b\d{1,2}:\d{2}\b',linijka[ind])):
                        linijka= linijka[:(len(linijka)-2)]
                        break
                if(len(linijka)>0):
                    if(linijka[0]=='Wykonali' or'Synevo' in linijka):
                        break
                    elif(linijka[0]!='umiarkowane' and linijka[0]!='małe' and  linijka[0]!='duże' and linijka[0]!='bardzo' and 'ekstremalne' not in linijka and 'Zmiana' not in linijka and 'sercowo-naczyniowego' not in linijka and 'wytycznych' not in linijka and 'próbkę' not in linijka and 'zakresie' not in linijka and'Analizator' not in linijka and 'Patrz' not in linijka and linijka[0]!='na' and 'nieprawidłowa' not in linijka and 'cukrzyca' not in linijka and 'Wartość' not in linijka and'skali' not in linijka and not any("badania" in line.lower() for line in linijka) and 'równania' not in linijka and not any(re.search( r"\b(\d{2})-(\d{2})-(\d{4})\b",line)  for line in linijka) and not any("metoda" in line.lower() for line in linijka) and not any("materiał" in line.lower() for line in linijka) ):
                        nazwa=""
                        for słowo in linijka:
                            try:
                                float(słowo)
                                break
                            except:
                                if('>' in słowo or re.search(r"^\d+(\.\d+)?%$",słowo) or '↑' in słowo or '↓' in słowo ):
                                    break
                                else:
                                    
                                    nazwa=nazwa+' '+słowo
                                    z=z+1
                        
                        if(nazwa.startswith(' ◗')):
                            nazwa=nazwa.split('◗')[1]
                        elif(nazwa.startswith(' •')):
                            nazwa=nazwa.split('•')[1]
                        
                        if((len(nazwa.split(' '))-1)!=len(linijka) and not linijka[0].startswith('<')):
                            wartość=linijka[z]
                            if('%' in wartość):
                                wartość=wartość.split('%')[0]
                                jednostka='%'
                                
                                if('↑' in wartość ):
                                    wartość=wartość.split('↑')[1]
                                elif('↓' in wartość):
                                    wartość=wartość.split('↓')[1]
                                if(len(linijka)>(z+3)):
                                    zakresMin=linijka[z+1]
                                    zakresMax=linijka[z+3]
                                else:
                                    if(linijka[z+1]=='<'):
                                        zakresMin='0'
                                        zakresMax=linijka[z+2]
                                    elif(linijka[z+1]=='>'):
                                        zakresMax='inf'
                                        zakresMin=linijka[z+2]
                            elif('<' in nazwa):
                                nazwa= nazwa.split('<')[0]
                                wartość='<'+wartość
                            elif('>' in nazwa):
                                nazwa= nazwa.split('>')[0]
                                wartość='>'+wartość
                            try:
                                float(linijka[z+1])
                            except:
                                if(jednostka!='%'):
                                    if(len(linijka)>z+1 and (linijka[z+1]=='<' or linijka[z+1]=='<')):
                                        jednostka='-'
                                        if(linijka[z+1]=='<'):
                                            zakresMax=linijka[z+2]
                                            zakresMin='0'
                                            
                                        elif(linijka[z+1]=='>'):
                                            zakresMax='inf'
                                            zakresMin=linijka[z+2]
                                            
                                    else:
                                         jednostka=linijka[z+1]
                                    
                                        
                                if(len(linijka)<=(z+2)):
                                    zakresMax='-'
                                    zakresMin='-'
                                elif('Dla' in linijka):
                                    jednostka=linijka[z+1]
                                    zakresMin='dokładny zakres pliku zakresy.xml'
                                    zakresMax='-'
                                elif (re.search(r'\b\d+-\d+\b',linijka[z+2])):
                                    zakresMin=linijka[z+2].split('-')[0]
                                    zakresMax=linijka[z+2].split('-')[1]
                                elif(len(linijka)>=(z+4)):
                                    if(jednostka=='x10'):
                                        jednostka=jednostka+linijka[z+2]
                                        zakresMin=linijka[z+3]
                                        zakresMax=linijka[z+5]
                             
                                    elif (linijka[z+2]=='<'):

                                        zakresMin='0'
                                        zakresMax=re.match( r"^[^A-Za-z]*",  linijka[z+3]).group()
                                    elif(linijka[z+2]=='>'):
                                        if( len(linijka)>z+4 and linijka[z+4]=='-'):
                                            zakresMin='-'
                                            zakresMax='-'
                                        else:
                                            zakresMax='inf'
                                            zakresMin=re.match( r"^[^A-Za-z]*",  linijka[z+3]).group()
                                    else:
                                        try:
                                            float(linijka[z+2])
                                            zakresMin=linijka[z+2]
                                            zakresMax=linijka[z+4]
                                        except:
                                            if(wartość.startswith('>') or wartość.startswith('<')):
                                                zakresMin=linijka[z+2]
                                                zakresMax='-'
                                            else:
                                                if(len(linijka)>8 and linijka[z+3]=='pożądane'):
                                                    if(linijka[z+5]=='powyżej'):
                                                        zakresMax='inf'
                                                        zakresMin=linijka[z+6]
                                                    elif(linijka[z+5]=='poniżej'):
                                                        zakresMax='0'
                                                        zakresMin=linijka[z+6]    
                                                else:
                                                    
                                                    zakresMin='-'
                                                    zakresMax='-'
                                

                                elif(linijka[z+1]=='mężczyźni' or linijka[z+1]=='kobiety'):
                                    jednostka='-'
                                    zakresMin='dokładny zakres pliku zakresy.xml'
                                    zakresMax='-'
                                elif(re.match(r"^<\d+(\.\d+)?$", linijka[z+2])):
                                    zakresMin='0'
                                    zakresMax= re.match(r"^<([\d.]+)$", linijka[z+2]).group(1)
                                elif(re.match(r"^<$", linijka[z+2])):
                                    zakresMin='0'
                                    zakresMax=linijka[z+3]
                                elif(re.match(r"^>$", linijka[z+2])):
                                    zakresMax='inf'
                                    zakresMin=linijka[z+3]

                        if(re.match(r"^\d+(\.\d+)?[A-Za-z]",zakresMax)):
                            zakresMax=re.match(r"([^A-Za-z]*)", zakresMax).group(1)
                
                if(('GFR' in nazwa and zakresMin=='-')or('Cholesterol'in nazwa and zakresMax=='-')or('LDL' in nazwa and (zakresMin=='' or zakresMin=='-')) or ('Nie-HDL'in nazwa and zakresMax=='-')or ('Glukoza'in nazwa and zakresMax=='-') or (('Witamina' in nazwa and 'D' in nazwa) and zakresMax=='-')):
                    zakresMin='dokładny zakres pliku zakresy.xml'
                    zakresMax='-'
                if('Cholesterol' in nazwa and'Triglicerydy' in nazwa):
                    nazwa=nazwa.split('Triglicerydy')[0]
                    wartość='Triglicerydy'+' '+wartość
                if(nazwa!='' and zakresMax!=''):
                    try:        
                        wartość=float(wartość)
                        if(zakresMin!='-' and 'zakres' not in zakresMin):
                            zakresMin=float(zakresMin)   
                        if(zakresMax!='-'):
                            zakresMax=float(zakresMax)
                    except:
                        wartość=wartość
                    daneBiochemia[nazwa.strip()] = (wartość,jednostka,zakresMin,zakresMax) 
                
        return daneBiochemia
            
     