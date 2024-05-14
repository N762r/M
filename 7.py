# Количество страниц для каждого запроса
proton_boson_pages = 165
photon_proton_boson_pages = 80
photon_boson_pages = 125

# Расчет общего количества страниц для запроса (протон|фотон) & бозон
total_pages = (proton_boson_pages + photon_boson_pages) - photon_proton_boson_pages

print(f'Количество страниц, найденных по запросу (протон|фотон) & бозон: {total_pages} тысяч')
