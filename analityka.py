import re
class Analityka:
    def OdczytWynikowAnalitycznych(self,indexAnalityka,indexNextAnalityka,line):
        daneAnalityka={}
        for k in range(indexAnalityka,indexNextAnalityka):

            linijka=line[k].split(' ')
            zakresMax=''
            zakresMin=''
            wszystkie=len(''.join(line[k]))
            linijka= list(filter(lambda x: x != '' , linijka))
            linijka= list(filter(lambda x: x != '↑', linijka))
            linijka = [slowo.replace(',', '.') for slowo in linijka]
            for ind in range(len(linijka)):
                if(re.search(r'PB',linijka[ind])):
                    linijka[ind]=re.split(r'PB',linijka[ind])[0]
                    for index in range(ind+1,len(linijka)):
                        linijka[index]='-'
                    
                else:
                    linijka[ind]=linijka[ind]
            if(len(linijka)>0):
                if('Metoda:' in linijka or'Komentarz' in linijka  or 'Wykonali' in linijka or 'koniec' in ''.join(linijka)):
                    break
                elif('Osad'not in linijka and'ogólne'not in linijka and'Metoda' not in linijka and'badanie' not in linijka and'Analizator'not in linijka and'Środowisko' not in linijka and 'Mikroskopowy' not in linijka and 'Badanie' not in linijka and not re.match( r'\b\d{2}-\d{2}-\d{4}\b',linijka[0]) and 'Materiał:' not in linijka[0] and 'metod' not in linijka and len(linijka)>1):
                    nazwa=''
                    z=0
                    for słowo in linijka:

                        if( '(' in słowo or '↑' not in słowo and 'gęsto' not in słowo and'lekko' not in słowo and słowo !='pł' and 'mętny' not in słowo and 'ślad' not in słowo and 'prawidłowy'not in słowo and'nie' not in słowo and  'pojedyncze' not in słowo.lower() and 'nieliczne' not in słowo.lower() and 'dość' not in słowo.lower() and'żółta' not in słowo and 'żółty' not in słowo and'mało' not in słowo and 'nieliczne' not in słowo and 'ciemnożółty' not in słowo and 'nieobecn' not in słowo and'słomkowa' not in słowo and słowo!='przejrzysty' and'ujemn' not in słowo and słowo!='w' and not re.search(r'\d',słowo) and '>=' not in słowo and 'zupełna'not in słowo):
                            nazwa=nazwa+słowo+' '
                            z=z+1
                        else:
                            break
                    if(linijka[z]=='w'):
                        wartosc=linijka[z]+' '+linijka[z+1]
                        if(len(linijka)==z+2):
                            jednostka='-'
                            zakresMin='-'
                            zakresMax='-'
                            
                        elif('nieobecn' not in linijka[z+1] and'słomkowa' not in linijka[z+2] and linijka[z+2]!='przejrzysty' and 'ujemn' not in linijka[z+2] and linijka[z+2]!='w' and not re.search(r'\d',linijka[z+2])):
                            if(linijka[z+2]=='<'):
                                jednostka='-'
                                zakresMin='0'
                                zakresMax=linijka[z+3]
                            else:
                                jednostka=linijka[z+2]
                                zakresMin=linijka[z+3]
                                zakresMax='-'
                            
                        else:
                            jednostka='-'
                            zakresMin=linijka[z+2] +' '+linijka[z+3]
                            zakresMax='-'
                        
                    
                        
                    else:
                        
                        wartosc=linijka[z]
                        
                        
                        try:
                            if('żółty'not in linijka and 'prawidłowy' not in linijka and'żółta' not in linijka[z+1] and 'nieobecn' not in linijka[z+1] and'słomkowa' not in linijka[z+1] and linijka[z+1]!='przejrzysty' and 'ujemn' not in linijka[z+1]  and linijka[z+1]!='w' and not re.search(r'\d',linijka[z+1])):
                                try: 
                                    
                                    float(wartosc)
                                    jednostka=linijka[z+1]
                                    if(linijka[z+2]=='<'):
                                        zakresMin=0
                                        if "/" in linijka[z+3]:
                                            zakresMax=re.search(r'\d+\.?\d*', linijka[z+3]).group()
                                        else:
                                            zakresMax=float(linijka[z+3])
                                        
                                    elif(linijka[z+2].startswith('<')):
                                        zakresMin=0
                                        if "/" in linijka[z+2]:
                                            zakresMax=re.search(r'\d+\.\d+', linijka[z+2]).group()
                                        else:
                                            zakresMax=linijka[z+2].replace('<', '')
                                    elif(linijka[z+1]=='-'):
                                        wartosc=linijka[z]+linijka[z+1]+linijka[z+2]
                                        jednostka=linijka[z+3]
                                        zakresMin=linijka[z+4]+'-'+linijka[z+6]
                                        zakresMax='-'
                                        

                                        
                                    else:
                                        zakresMax= re.split('[a-zA-Z]', linijka[z+4])[0]
                                        zakresMin=linijka[z+2]
                                    
                                except:
                                    if(wartosc.lower()=='dość' or wartosc.lower()=='nie'):
                                        wartosc=linijka[z]+' '+linijka[z+1]
                                        if(wartosc=='nie wykryto'):
                                            jednostka='-'
                                            
                                            try:
                                                zakresMin=linijka[z+2]+' '+linijka[z+3]
                                                zakresMax='-' 
                                            except:
                                                zakresMin=linijka[z+2]
                                                zakresMax='-'
                                        else:
                                            jednostka=linijka[z+2]
                                            try:
                                                zakresMin=linijka[z+3]+' '+linijka[z+4]
                                                zakresMax='-' 
                                            except:
                                                zakresMin=linijka[z+3]
                                                zakresMax='-'
                                        
                                    else:
                                        if(re.match(r'\b\d{2}:\d{2}\b',linijka[z+2])):
                                            wartosc=  re.sub(r'\d.*', '', wartosc)
                                            jednostka='-'
                                            zakresMin='-'
                                            zakresMax='-'
                                        else:
                                            jednostka=linijka[z+1]
                                            if(jednostka=='wpw' and  re.search(r'\d+', wartosc)):
                                                
                                                zakresMin=linijka[z+2]+linijka[z+3]+linijka[z+4]
                                                zakresMax='-'
                                            elif(jednostka=='wpw' and not re.search(r'\d+', wartosc)):
                                                zakresMin=linijka[z+2]
                                                zakresMax='-'
                                            elif(wartosc.startswith('!')):
                                                wartosc=wartosc.split('!')[1]
                                                zakresMin=linijka[z+2]
                                                zakresMax='-'
                                            elif(wartosc=='gęsto'):
                                                wartosc=wartosc+' '+linijka[z+1]
                                                jednostka=linijka[z+2]
                                                zakresMin=linijka[z+3]
                                            else:

                                                zakresMin=linijka[z+2]
                                                zakresMax='-'
                            else:
                                

                                jednostka='-'
                                try: 
                                   
                                    if(wartosc=='>='):
                                        wartosc=linijka[z+1]
                                        float(wartosc)
                                        zakresMin=float(linijka[z+2])
                                        zakresMax=float(linijka[z+4])
                                        
                                    elif(re.split('b', linijka[z+1])[0]=='wpw'):
                                        jednostka=re.split('b', linijka[z+1])[0]
                                        zakresMax='-'
                                        zakresMin='-'  
                                        
                                    
                                    elif(linijka[z+2]=='<'):
                                        zakresMin=0
                                        zakresMax=float(linijka[z+3])
                                    
                                    else:
                                        zakresMax=linijka[z+3]
                                        zakresMin=linijka[z+1]
                                    float(wartosc)
                                except:
                                    if(jednostka=='wpw' ):
                                        zakresMax='-'
                                        zakresMin='-'
                                    
                                    else:
                                        zakresMin=linijka[z+1]
                                        zakresMax='-'
                                    
                        except:
                            if(wartosc=='lekko'):
                                wartosc=wartosc+' '+linijka[z+1]
                            
                            else:
                                jednostka='-'
                                zakresMax='-'
                                zakresMin='-'
                    if(re.search(r'^\d+:\d+$',linijka[len(linijka)-1])):
                            if(linijka[z]=='pł'):
                                wartosc=linijka[z]+' '+linijka[z+1]
                                jed=linijka[z+2]
                                jednostka=jed[:(len(jed)-2)]
                                zakresMax='-'
                                zakresMin='-'
                            else:
                                try:
                                    float(wartosc)
                                except:
                                    wart=linijka[z]
                                    wartosc=wart[:(len(wart)-2)]
                        
                    
                    if(nazwa.strip() in daneAnalityka):
                        nazwa= nazwa+'2'
                    try:
                        wartosc=float(wartosc)
                        if(zakresMax!='-'):
                            zakresMax=float(zakresMax)
                        if(zakresMin!='-'):
                            zakresMin=float(zakresMin)    
                    except:
                        wartosc=wartosc
                    

                    daneAnalityka[nazwa.strip()] = (wartosc,jednostka,zakresMin,zakresMax)
        return daneAnalityka
                
        