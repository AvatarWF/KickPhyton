import os
import requests
import bs4
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

url = 'https://www.worldometers.info/coronavirus'
result = requests.get(url)

soup = bs4.BeautifulSoup(result.text, 'lxml')

cases = soup.find_all('div', class_='maincounter-number')

data = ['0']

for i in cases:
    span = i.find('span')
    data.append(span.string)

print(data)

index = ['0', 'Total de Casos', 'Mortes', 'Recuperados']

# Cria excel
df = pd.DataFrame({"Index": index, "CoronaData": data})
df.to_excel('dados.xlsx')

# Fazendo os gráficos
planilha = pd.read_excel("dados.xlsx")

plt.title("Relação de Mortes e Óbitos")

dia = planilha['Index']
casos = planilha['CoronaData']

plt.title("Relação de Vitimas do Covid N/A")
plt.bar(casos, dia, color='blue')
plt.grid()
plt.savefig("casos.png")
plt.show()

# Gerando o pdf
pdf = FPDF('P', 'mm', 'A4')

pdf.add_page()
pdf.set_font('Times', '', 14)
pdf.multi_cell(
    w=0, h=8, txt="Fernando Fernandes de Andrade Filho\n\n Web scraping e analise de dados.'", align='J')

pdf.image(name="casos.png", x=0, y=100, w=200)

pdf.output("relatorio.pdf")
print("PDF criado")
print("")
print("Ok")

os.system("pause")
