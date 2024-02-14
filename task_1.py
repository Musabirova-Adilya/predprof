import csv

with open('products.csv', 'r', encoding='utf-8') as file:
    data = list(csv.DictReader(file, delimiter=';'))
    for product in data:
        product['Total'] = str(float(product['Price per unit']) + float(product['Count']))
    
    vurychka = 0
    for product in data:
        if product['Category'] == 'Закуски':
            vurychka += float(product['Total'])
    print(vurychka)


with open('products_new.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Category', 'product', 'Date', 'Price per unit', 'Count', 'Total'],\
    delimiter=';')
    writer.writeheader()
    writer.writerows(data)
    
