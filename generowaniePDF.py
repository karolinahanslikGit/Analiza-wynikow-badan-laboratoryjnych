from fpdf import FPDF
from PIL import Image
import os
logoIb=Image.open("ilustracje\logo_ib.png")
w,h=logoIb.size


class GenerowaniePDF:
    def GenerowaniePlikuPDF(self,tabelaMorfologia,tabelaAnalityka,tabelaBiochemia, tabelaImmunochemia,danePacjenta,tabWartMorf,tabWartBiochem,tabWartImmuno,tabWartAnalityka):
        pdf = FPDF()
        pdf.add_page()

        pdf.add_font('Roboto', '', 'fonts/Roboto-Regular.ttf', uni=True)
        pdf.add_font('Roboto', 'B', 'fonts/Roboto-Bold.ttf', uni=True)
        pdf.add_font('Roboto', 'I', 'fonts/Roboto-Italic.ttf', uni=True)

    
        pdf.set_font('Roboto','',12)
        pdf.image('ilustracje\logo_ib.png',x=10,y=10,w=30,h=30)
        pdf.image('ilustracje\logo_polsl.png',x=170,y=10,w=33,h=33)
        pdf.set_font('Roboto','',16)
        pdf.multi_cell(190, 15, 'Aplikacja do analizy wyników krwi \nInterpretacja wyników', align='C') 
        pdf.set_font('Roboto','',13)
        pdf.cell(30,50,'Dane pacjenta:',ln=True)
        pdf.cell(10,20,'')
        pdf.cell(70,-20,f'Imię: {danePacjenta["Imie"]}')
       
        pdf.cell(120,-20,f'PESEL: {danePacjenta["PESEL"]}',ln=True,align='L')
        pdf.cell(10,20,'')
        pdf.cell(70,50,f'Nazwisko: {danePacjenta["Nazwisko"]}')
       
        pdf.cell(120,50,f'Data Urodzenia: {danePacjenta["DataUrodzenia"]}',ln=True,align='L')
        pdf.set_font('Roboto','B',12)
        pdf.cell(200,10,'Analiza Morfologi',align='C',ln=True)
        pdf.set_font('Roboto','',12)
        if(len(tabWartMorf)>0):
            for tabMorf in tabWartMorf:
                słowa=tabMorf.split(' ')
                for słowo in słowa:
                    szer= pdf.get_string_width(słowo) 
                    if('parametr' in słowo.lower() or 'zakresy' in słowo.lower() or 'zakres' in słowo.lower() or  słowo.lower()=='wartość:'):
                        pdf.set_font('Roboto','B',12)
                        pdf.cell(szer+4,10,słowo+' ',align='C',ln=False) 
                    else:
                        pdf.set_font('Roboto','',12)
                        pdf.cell(szer+1,10,słowo+' ',align='C',ln=False)
                     
                    
                pdf.ln(10) 
        if(len(tabelaMorfologia)>0):
            pdf.set_font('Roboto','B',12)
            pdf.cell(200,20,'Interpretacja wyników', align='C',ln=True)
            for t in tabelaMorfologia:
                if(type(t[0])==str):
                    pdf.set_font('Roboto','',12)
                    pdf.multi_cell(0,6,t[0],align='J')
                    pdf.set_font('Roboto','',7)
                    zr=t[1]
                    if(type(t[1])==list and len(t[1])>1):
                        pdf.cell(10,3,'Zródła:',ln=True)  
                        for z in t[1]:        
                            pdf.multi_cell(0,4,z,align='J')
                    else:
                       pdf.multi_cell(0,4,f'Zródło: {t[1]}',align='J')  
                    pdf.cell(10,4,"",ln=True)
                else:
                    pdf.set_font('Roboto','',12)
                    pdf.multi_cell(0,4,t[0][0],align='J')
                    pdf.set_font('Roboto','',7)
                    pdf.multi_cell(0,4,f'Zródło: {t[1][0]}',align='J') 
                    pdf.cell(10,4,"",ln=True)
        else:
            pdf.cell(200,10,'Brak nieprawidłowości',align='C',ln=True)

        pdf.set_font('Roboto','B',12)
        pdf.cell(200,20,'Analiza Analityki',align='C',ln=True)
        pdf.set_font('Roboto','',12)
        if(len(tabWartAnalityka)>0):
            for tabAnalityka in tabWartAnalityka:
                słowa=tabAnalityka.split(' ')
                for słowo in słowa:
                    szer= pdf.get_string_width(słowo) 
                    if('parametr' in słowo.lower() or 'zakresy' in słowo.lower() or 'zakres' in słowo.lower() or 'wartość' in słowo.lower()):
                        pdf.set_font('Roboto','B',12)
                        pdf.cell(szer+4,10,słowo+' ',align='C',ln=False) 
                    else:
                        pdf.set_font('Roboto','',12)
                        pdf.cell(szer+1,10,słowo+' ',align='C',ln=False)
                pdf.ln(10) 
        if(len(tabelaAnalityka)>0):
            pdf.set_font('Roboto','B',12)
            pdf.cell(200,20,'Interpretacja wyników', align='C',ln=True)
            pdf.set_font('Roboto','',12)
            for a in tabelaAnalityka:
                pdf.set_font('Roboto','',12)
                pdf.multi_cell(0,6,a[0],align='J')
                pdf.set_font('Roboto','',7)
               
                if(type(a[1])==list and len(a[1])>1):
                    pdf.cell(10,3,'Zródła:',ln=True)  
                    for z in a[1]:        
                        pdf.multi_cell(0,4,z,align='J')
                else:
                    pdf.multi_cell(0,4,f'Zródło: {a[1]}',align='J')  
                pdf.cell(10,4,"",ln=True)
        else:
            pdf.cell(200,10,'Brak nieprowidłowości',align='C',ln=True)
        pdf.set_font('Roboto','B',12)
        pdf.cell(200,20,'Analiza Biochemii',align='C',ln=True)
        pdf.set_font('Roboto','',12)
        if(len(tabWartBiochem)>0):
            for tabBiochem in tabWartBiochem:
                słowa=tabBiochem.split(' ')
                for słowo in słowa:
                    szer= pdf.get_string_width(słowo) 
                    if('parametr' in słowo.lower() or 'zakresy' in słowo.lower() or 'zakres' in słowo.lower() or 'wartość' in słowo.lower()):
                        pdf.set_font('Roboto','B',12)
                        pdf.cell(szer+4,10,słowo+' ',align='C',ln=False) 
                    else:
                        pdf.set_font('Roboto','',12)
                        pdf.cell(szer+1,10,słowo+' ',align='C',ln=False)
                pdf.ln(10) 
        if(len(tabelaBiochemia)>0):
            pdf.set_font('Roboto','B',12)
            pdf.cell(200,20,'Interpretacja wyników', align='C',ln=True)
            for a in tabelaBiochemia:
                pdf.set_font('Roboto','',12)
                pdf.multi_cell(0,6,a[0],align='J')
                pdf.set_font('Roboto','',7)
               
                if(type(a[1])==list and len(a[1])>1):
                    pdf.cell(10,3,'Zródła:',ln=True)  
                    for z in a[1]:        
                        pdf.multi_cell(0,4,z,align='J')
                else:
                    pdf.multi_cell(0,4,f'Zródło: {a[1]}',align='J')  
                pdf.cell(10,4,"",ln=True)
        else:
            pdf.cell(200,10,'Brak nieprawidłowości',align='C',ln=True)

        pdf.set_font('Roboto','B',12)
        
        pdf.cell(200,20,'Analiza Immunochemii',align='C',ln=True)
        pdf.set_font('Roboto','',12)
        if(len(tabWartImmuno)>0):
            for tabImmuno in tabWartImmuno:
                słowa=tabImmuno.split(' ')
                for słowo in słowa:
                    szer= pdf.get_string_width(słowo) 
                    if('parametr' in słowo.lower() or 'zakresy' in słowo.lower() or 'zakres' in słowo.lower() or 'wartość' in słowo.lower()):
                        pdf.set_font('Roboto','B',12)
                        pdf.cell(szer+4,10,słowo+' ',align='C',ln=False) 
                    else:
                        pdf.set_font('Roboto','',12)
                        pdf.cell(szer+1,10,słowo+' ',align='C',ln=False)
                pdf.ln(10) 
        if(len(tabelaImmunochemia)>0):
            pdf.set_font('Roboto','B',12)
            pdf.cell(200,20,'Interpretacja wyników', align='C',ln=True)
            for a in tabelaImmunochemia:
                pdf.set_font('Roboto','',12)
                pdf.multi_cell(0,6,a[0],align='J')
                pdf.set_font('Roboto','',7)
               
                if(type(a[1])==list and len(a[1])>1):
                    pdf.cell(10,3,'Zródła:',ln=True)  
                    for z in a[1]:        
                        pdf.multi_cell(0,4,z,align='J')
                else:
                    pdf.multi_cell(0,4,f'Zródło: {a[1]}',align='J')  
                pdf.cell(10,4,"",ln=True)
        else:
            pdf.cell(200,10,'Brak nieprawidłowości',align='C',ln=True)
        sciezkaDoPulpitu = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') 
        nazwisko=danePacjenta["Nazwisko"]
        if(nazwisko!=""):
            pdf.output(f'{sciezkaDoPulpitu}\Interpretacja_wyników_{nazwisko}.pdf')
        else:
            pdf.output(f'{sciezkaDoPulpitu}\Interpretacja_wyników.pdf')

    
