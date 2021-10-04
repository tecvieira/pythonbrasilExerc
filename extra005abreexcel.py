import openpyxl

book = openpyxl.load_workbook('Planilhe de Teste.xlsx')
# lendo a planilha selecionada
frutas_page = book['Frutas']
# lendo a aba selecionada
for rows in frutas_page.iter_rows(min_row= 2, max_row=4):
    # limitando a impressão apartir da segunda linha excluindo o título a linha definida por você
    print(f'{rows[0].value}, {rows[1].value}, {rows[2].value}')
    # imprimindo de forma formatada
