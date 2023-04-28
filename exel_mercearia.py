import openpyxl

planilha = openpyxl.Workbook()
planilha.create_sheet("Página 1", 0)

pagina1 = planilha["Página 1"]

pagina1["A1"] = "Produto"
pagina1["B1"] = "Preço Unitário"
pagina1["C1"] = "Quantidade"
pagina1["D1"] = "Valor total"
pagina1["E1"] = "Faturamento total"

pagina1["A2"] = "Arroz 5kg"
pagina1["B2"] = 18.00
pagina1["C2"] = 1500
pagina1["D2"] = "=B2*C2"
pagina1["E2"] = "=D2*0.1"

pagina1["A3"] = "Macarrão"
pagina1["B3"] = 3.00
pagina1["C3"] = 2000
pagina1["D3"] = "=B3*C3"
pagina1["E3"] = "=D3*0.1"

planilha.save("planilha_mercearia.xlsx")