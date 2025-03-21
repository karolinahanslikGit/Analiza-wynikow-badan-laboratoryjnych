import xml.etree.ElementTree as ET
class OdczytZakresow:
    def AnalizaDodatkowychZakresow(self,klucz,wartosc,jednostka,zakresMin):
        tree = ET.parse('zakresy.xml')
        root = tree.getroot()

        if('LDL' in klucz and "zakresy.xml" in zakresMin and 'mg/dl' in jednostka):
            chol_ldl=root.find(".//parametr[@nazwa='Cholesterol LDL mg/dl']")
            zakresy = chol_ldl.find('zakresy')
            z=[]
            for zakres in zakresy.findall('zakres'):
                zakresy_wart=zakres.find('wartości').text.split('-')
                z.append(float(zakresy_wart[1]))
            for zakres in zakresy.findall('zakres'):
                zakresy_wart=zakres.find('wartości').text.split('-')
                opis=zakres.find('wartości').attrib.get('opis')
                try:
                    float(wartosc)
                    if(float(zakresy_wart[0])<float(wartosc) and float(wartosc)<float(zakresy_wart[1])):
                    
                    
                        return(f'{klucz}-{wartosc}-{zakresy_wart[0]}-{zakresy_wart[1]}-{opis}')
                        
                    elif(float(wartosc)>max(z)):
                      
                        return(f'{klucz}-{wartosc}-{zakresy_wart[0]}-{f"{max(z)}"}-{"wartość nie spełnia żadnej normy"}')
                except:
                    if('Triglicerydy' in wartosc):
                     
                        return(f'{klucz}-{wartosc}-{zakresy_wart[0]}-{zakresy_wart[1]}-{"Stężenie triglicerydów w cholesterolu powyżej 350 uniemożliwia wyliczenie cholesterolu LDL"}')
                        
        if('LDL' in klucz and "zakresy.xml" in zakresMin and 'mmol/l' in jednostka):
            chol_ldl=root.find(".//parametr[@nazwa='Cholesterol LDL mmol/l']")
            
            zakresy = chol_ldl.find('zakresy')
            z=[]
            for zakres in zakresy.findall('zakres'):
                zakresy_wart=zakres.find('wartości').text.split('-')
                z.append(float(zakresy_wart[1]))
            for zakres in zakresy.findall('zakres'):
                zakresy_wart=zakres.find('wartości').text.split('-')
                opis=zakres.find('wartości').attrib.get('opis')
                if(float(zakresy_wart[0])<float(wartosc) and float(wartosc)<float(zakresy_wart[1])):
                
                 
                    return(f'{klucz}-{wartosc}-{zakresy_wart[0]}-{zakresy_wart[1]}-{opis}')
                elif(float(wartosc)>max(z)):
                 
                    return(f'{klucz}-{wartosc}-{zakresy_wart[0]}-{zakresy_wart[1]}-{"wartość nie spełnia żadnej normy"}')
        if('egfr' in klucz.lower() and 'zakresy.xml' in zakresMin):
            egfr=root.find(".//parametr[@nazwa='eGFR']")
            
            zakresy = egfr.find('zakresy')
            z=[]
            for zakres in zakresy.findall('zakres'):
                zakresy_wart=zakres.find('wartości').text
                if(zakresy_wart==wartosc or zakresy_wart=='>=90'):
       
                    return ""
                else:
                 
                    return(f'{klucz}-{wartosc}-{zakresy_wart}')

                
        if('HDL' in klucz and "zakresy.xml" in zakresMin and 'mg/dl' in jednostka ):
            chol_ldl=root.find(".//parametr[@nazwa='Cholesterol Nie-HDL mg/dl']")
            zakresy = chol_ldl.find('zakresy')

            z=[]
            for zakres in zakresy.findall('zakres'):
                zakresy_wart=zakres.find('wartości').text.split('-')
                z.append(float(zakresy_wart[1]))
            
            for zakres in zakresy.findall('zakres'):
                zakresy_wart=zakres.find('wartości').text.split('-')
                opis=zakres.find('wartości').attrib.get('opis')
                if(float(zakresy_wart[0])<float(wartosc) and float(wartosc)<float(zakresy_wart[1])):
                

                    return (f'{klucz}-{wartosc}-{zakresy_wart[0]}-{zakresy_wart[1]}-{opis}')
                elif(float(wartosc)>max(z)):
       
                    return (f'{klucz}-{wartosc}-{zakresy_wart[0]}-{zakresy_wart[1]}-{"wartość HDL nie spełnia żadnej normy"}')
                
        if('HDL' in klucz and "zakresy.xml" in zakresMin and 'mmol/l' in jednostka ):
            chol_hdl=root.find(".//parametr[@nazwa='Cholesterol Nie-HDL mmol/l']")
            zakresy = chol_hdl.find('zakresy')

            z=[]
            for zakres in zakresy.findall('zakres'):
                zakresy_wart=zakres.find('wartości').text.split('-')
                z.append(float(zakresy_wart[1]))
            
            for zakres in zakresy.findall('zakres'):
                zakresy_wart=zakres.find('wartości').text.split('-')
                opis=zakres.find('wartości').attrib.get('opis')
                if(float(zakresy_wart[0])<float(wartosc) and float(wartosc)<float(zakresy_wart[1])):
                
              
                    return (f'{klucz}-{wartosc}-{zakresy_wart[0]}-{zakresy_wart[1]}-{f"wartość HDL spełniona {opis}"}')

                elif(float(wartosc)>max(z)):
        
                    return (f'{klucz}-{wartosc}-{zakresy_wart[1]}-{zakresy_wart[1]}-{"wartość HDL nie spełnia żadnej normy"}')
                
        if('aterogenny' in klucz and "zakresy.xml" in zakresMin ):
            atero=root.find(".//parametr[@nazwa='Wskaźnik aterogenny']")
            zakresy = atero.find('zakresy')
            for zakres in zakresy.findall('zakres'):
                zakresy_wart=zakres.find('wartości').text.split('-')
                opis=zakres.find('wartości').attrib.get('opis')
                if(float(zakresy_wart[0])<float(wartosc) and float(wartosc)<float(zakresy_wart[1]) and opis=='Kobiety'):
         
                    return(f'{klucz}-{wartosc}-{zakresy_wart[0]}-{zakresy_wart[1]}-{"spełniona jest wartość dla kobiet i mężczyzn"}')
                elif(float(wartosc)<float(zakresy_wart[1]) and opis=='Mężczyźni'):
             
                    return(f'{klucz}-{wartosc}-{zakresy_wart[0]}-{zakresy_wart[1]}-{"spełniona jest wartość dla mężczyzn"}')
                
                elif(float(wartosc)>float(zakresy_wart[1])):
      
                    return(f'{klucz}-{wartosc}-{zakresy_wart[0]}-{zakresy_wart[1]}-{"wartość jest za wysoka dla kobiet i mężczyzn"}')
        if('Cholesterol' in klucz and 'całkowity' in klucz and "zakresy.xml" in zakresMin ):
            chol=root.find(".//parametr[@nazwa='Cholesterol całkowity']")
            zakresy = chol.find('zakresy')
            z=[]
            for zakres in zakresy.findall('zakres'):
                zakresy_wart=zakres.find('wartości').text.split('-')
                z.append(float(zakresy_wart[1]))
            for zakres in zakresy.findall('zakres'):
                zakresy_wart=zakres.find('wartości').text.split('-')
               
                if(float(zakresy_wart[0])<float(wartosc) and float(wartosc)<float(zakresy_wart[1])):
                
                    print(f'spełniona jest norma ')
                    return ""
                elif(float(wartosc)>max(z)):
       
                    return(f'{klucz}-{wartosc}-{f"{max(z)}"}-{"wartość nie spełnia normy"}')
        if('Glukoza' in klucz and "zakresy.xml" in zakresMin ):
            glukoza=root.find(".//parametr[@nazwa='Glukoza']")
            zakresy = glukoza.find('zakresy')
            z=[]
            a=[]
            for zakres in zakresy.findall('zakres'):
                zakresy_wart=zakres.find('wartości').text.split('-')
                z.append(float(zakresy_wart[1]))
                a.append(float(zakresy_wart[0]))
            for zakres in zakresy.findall('zakres'):
                zakresy_wart=zakres.find('wartości').text.split('-')
                opis=zakres.find('wartości').attrib.get('opis')
                if(float(zakresy_wart[0])<float(wartosc) and float(wartosc)<float(zakresy_wart[1])):
                
         
                    return(f'{klucz}-{wartosc}-{zakresy_wart[0]}-{zakresy_wart[1]}-{opis}')
                elif(float(wartosc)>max(z)):
        
                    return(f'{klucz}-{wartosc}-{zakresy_wart[0]}-{zakresy_wart[1]}-{"wartość za wysoka"}')
                elif(float(wartosc)<min(a)):
       
                    return(f'{klucz}-{wartosc}-{zakresy_wart[0]}-{zakresy_wart[1]}-{"wartość za niska"}')


        if('Witamina' in klucz and 'D' in klucz and "zakresy.xml" in zakresMin ):
            wit_d=root.find(".//parametr[@nazwa='Witamina D']")
            zakresy = wit_d.find('zakresy')
            for zakres in zakresy.findall('zakres'):
                zakresy_wart=zakres.find('wartości').text.split('-')
                opis=zakres.find('wartości').attrib.get('opis')
                if(float(zakresy_wart[0])<float(wartosc) and float(wartosc)<float(zakresy_wart[1])):
                
                 
                    if(opis!="stężenie optymalne"):
                        return(f'{klucz}-{wartosc}-{zakresy_wart[0]}-{zakresy_wart[1]}-{opis}')
                    else:
                        return ""
    
        
                
        
     
   
