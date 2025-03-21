import re
class Morfologia:
    def OdczytWynikowMorfologicznych(self,indexMorf,indexNextMorf,line):
            daneMorfologia={}
            
            for k in range(indexMorf,indexNextMorf):
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
                    if(linijka[0]=='Wykonali' or'Synevo' in linijka):
                        break
                    elif( 'Zarejestrowana'not in linijka and not any("parametr" in line.lower() for line in linijka) and not any("materiał" in line.lower() for line in linijka) and'Procedura' not in linijka and 'Próbka' not in linijka and 'badanie' not in linijka and not any("metoda" in line.lower() for line in linijka) and len(linijka)>1 and'Wskaźniki' not in linijka and"automatyczny" not in linijka and"Mikroskopowa" not in linijka  and "wyliczane" not in linijka and "impedancja" not in linijka and not any("analizator" in line.lower() for line in linijka) and not any("PBW" in line for line in linijka)):
                        nazwa=""
                        for słowo in linijka:
                            try:
                                float(słowo)
                                break
                            except:
                                if(re.search(r"^\d+(\.\d+)?%$",słowo) or '↑' in słowo or '↓' in słowo ):
                                    break
                                else:
                                    
                                    nazwa=nazwa+' '+słowo
                                    z=z+1
                        
                        if(re.match(r'^ ◗(.*)',nazwa)):
                            nazwa=re.match(r'^ ◗(.*)',nazwa).group(1)
                        elif(re.match(r'^ •(.*)',nazwa)):
                            nazwa=re.match(r'^ •(.*)',nazwa).group(1)
                        if((len(nazwa.split(' '))-1)!=len(linijka)):
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

                            try:
                                float(linijka[z+1])
                            except:
                                if(jednostka!='%'):
                                    jednostka=linijka[z+1]
                                    
                                        
                                if(len(linijka)<=(z+2)):
                                    zakresMax='-'
                                    zakresMin='-'
                                elif(len(linijka)>(z+4)):
                                    if(jednostka=='x10'):
                                        jednostka=jednostka+linijka[z+2]
                                        zakresMin=linijka[z+3]
                                        zakresMax=linijka[z+5]
                                    elif (linijka[z+2]=='<'):
                                        zakresMin='0'
                                        zakresMax=re.match( r"^[^A-Za-z]*",  linijka[z+3]).group()
                                    elif(linijka[z+2]=='>'):
                                        zakresMax='inf'
                                        zakresMin=re.match( r"^[^A-Za-z]*",  linijka[z+3]).group()
                                    else:
                                        zakresMin=linijka[z+2]
                                        zakresMax=linijka[z+4]
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
                                   
                    if(nazwa!='' and zakresMax!=''): 
                        wartość=float(wartość)
                        if(zakresMin!='-'):
                            zakresMin=float(zakresMin)   
                        if(zakresMax!='-'):
                            zakresMax=float(zakresMax)    
                        daneMorfologia[nazwa.strip()] = (wartość,jednostka,zakresMin,zakresMax) 
                
            return daneMorfologia