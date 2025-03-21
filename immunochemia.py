
import re
from PyPDF2 import PdfReader
class Immunochemia():
    
    def OdczytWynikowImmunochemicznych(self,indexImmunochem,indexNextImmuno,line):
        daneImmunochemia={}
        for k in range(indexImmunochem,indexNextImmuno):
            
            linijka=line[k].split(' ')
            wszystkie=len(''.join(line[k]))
            linijka= list(filter(lambda x: x != '', linijka))
            linijka = [slowo.replace(',', '.') for slowo in linijka]
            
            if( len(linijka)>1):
                if('akredytowane'  in linijka or 'koniec' in ''.join(linijka) or linijka[0]=='Środowisko'  or linijka[0]=='Toksyczność'or linijka[0]=='Synevo' or linijka[0]=='NIP:' or linijka[0]=="Towarzystwa"):
                    break
                elif('wprowadzone'not in linijka and 'Towarzystwa' not in linijka and 'wartości' not in linijka and 'Polska'not in linijka and 'Instrukcja' not in linijka and 'Endokrynologia' not in linijka and 'referencyjne' not in linijka and 'wykonano' not in linijka and 'dawki' not in linijka and 'Uwaga!'not in linijka and'Analizator'not in linijka and not re.match( r'\b\d{2}-\d{2}-\d{4}\b',linijka[0]) and 'Materiał:' not in linijka and 'Metoda:' not in linijka and 'SCORE' not in line[k] and 'Zmiana' not in linijka and 'ryzyka' not in linijka and'wyliczona'not in linijka and not linijka[0].startswith('>') and 'badania'not in linijka and 'metoda' not in linijka and 'Ocena' not in linijka and 'organizmu' not in linijka and 'grup' not in linijka ):
                    nazwa=""
                    for słowo in linijka:
                        try:
                            float(słowo)
                            break
                        except:
                            nazwa=nazwa+słowo+' '
                    
                    z=0
                    linijka= list(filter(lambda x: x != '', linijka))
                
                    for s in range(len(linijka)):
                        linijka[s]=linijka[s].replace(',','.')
                    wartość=''
                    jednostka=''
                    for slowo in linijka:
                        z=z+1           
                        slowo=slowo.replace(',','.')
                        try: 
                            float(slowo)
                            if(slowo==linijka[0]):
                                break
                            wartość=float(slowo)
                            if(linijka[z]=='x10'):
                                jednostka='10^3/µL'
                                zakresMin=float(linijka[z+2])                              
                                linijka[z+3] = re.sub(r'[a-zA-Z]', '', linijka[z+3])
                                zakresMax=float(linijka[z+4])
                            elif(len(linijka)==z+1 or 'Witamina 25' in nazwa):
                                jednostka=linijka[z]
                                zakresMax='-'
                                zakresMin='-'
                                break
                           
                            else:
                                if(linijka[z]=='<'):
                                    jednostka='-'
                                    zakresMin=0
                                    zakresMax=float(linijka[z+1])
                                    break
                                else:
                                    if(re.match(r'^\d+-\d+$',linijka[z+1])):
                                        jednostka=linijka[z]
                                        zakresMin=linijka[z+1].split('-')[0]
                                        zakresMax=linijka[z+1].split('-')[1]
                                        break
                                    elif(linijka[z]!='mężczyźni'):
                                        jednostka=linijka[z]
                                         
                                    else:
                                        jednostka='-'
                                        zakresMax='-'
                                        zakresMin='-'
                                        break
                                try: 
                                    zakresMin=float(linijka[z+1])                              
                                    
                                    try:
                                        zakresMax=float(linijka[z+3])
                                    except:
                                        zakresMax=float(re.search(r'\d+(\.\d+)?',linijka[z+3]).group())
                                    
                                except:
                                    if(len(linijka)==z+1):
                                        zakresMax='-'
                                        zakresMin='-'
                                    elif(linijka[z+1]=='<'):
                                        zakresMin=0
                                        try:
                                            zakresMax=float(linijka[z+2])
                                        except:
                                            zakresMax=float(re.search(r'\d+(\.\d+)?',linijka[z+2]).group())
                                    elif(linijka[z+1]=='>'):

                                        zakresMax=float('inf')
                                        try:
                                            zakresMin=float(linijka[z+2])
                                        except:
                                            zakresMin=float(re.search(r'\d+(\.\d+)?',linijka[z+2]).group())
                                    elif(linijka[z+1].startswith('<')):
                                        zakresMin=0
                                        linijka[z+1]=linijka[z+1].replace('<', '')
                                    elif(linijka[len(linijka)-1]=='*' or linijka[z+1].isalpha):
                                        zakresMax='-'
                                        zakresMin='-'
                                   
                            break
                        except:
                            if(len(linijka)>1):
                                if(linijka[0]=='%' or linijka[1]=='%' ):
                                    zakre=""
                                elif(linijka[z-1].endswith('%') and linijka[z-1][-2].isdigit() ):
                                    if(linijka[z-1].startswith('↑')):
                                        wartość=float(linijka[z-1].replace('%','').replace('↑',''))
                                    else:
                                        wartość=float(linijka[z-1].replace('%',''))
                                    jednostka='%'
                                    try:
                                        zakresMin=float(linijka[z])
                                        zakresMax=float(linijka[z+2])
                                    except:
                                        if(linijka[z]=='<'):
                                            zakresMin=0
                                            zakresMax=float(linijka[z+1])
                                    break
                                elif(linijka[z-1].startswith('>=')):
                                    wartość=linijka[z-1].split('>=')[1]
                                    jednostka=linijka[z]
                                    if(len(linijka)==z+1):
                                        zakresMax='-'
                                        zakresMin='-'
                                elif(linijka[z-1].startswith('>')):
                                    wartość=linijka[z-1]
                                    jednostka=linijka[z]
                                    if(len(linijka)>=z+1):
                                        zakresMin=float(linijka[z+1].replace('>',''))
                                        zakresMax=float("inf")
                                    else:
                                        zakresMin="-"
                                        zakresMax="-"
                                    break
                            zakre=""
                            pass 
                    if('Witamina' in nazwa and 'D' in nazwa and zakresMin=='-'):
                        zakresMin='dokładny zakres w pliku zakresy.xml'
                    
                    if(nazwa!='' and not 'materia' in nazwa.lower()):
                        daneImmunochemia[nazwa.strip()] = (wartość,jednostka,zakresMin,zakresMax)
           
            elif('Wykonali' in linijka):
                break
        return daneImmunochemia
       
