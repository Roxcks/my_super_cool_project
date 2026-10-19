n = int(input())
products = [input() for _ in range(n)]

with open('desyatochka.txt','r') as d_store, open('kubit.txt', 'r') as k_store, open('polosa.txt', 'r') as p_store:
    d_list = [info.rstrip().split(': ') for info in d_store.readlines()]
    d_dict = {name: int(price) for name, price in d_list}
    k_list = [info.rstrip().split(': ') for info in k_store.readlines()]
    k_dict = {name: int(price) for name, price in k_list}
    p_list = [info.rstrip().split(': ') for info in p_store.readlines()]
    p_dict = {name: int(price) for name, price in p_list}

def product_comparer(product1, *shops):
    best_shop = None
    best_price = None
    for name, shop in shops:
        if product1 in shop:
            price = shop[product1]
            if best_price is None or price < best_price:
                best_shop = name
                best_price = price
    return best_shop

lowest_price_list = []
for product in products:
    cheapest_shop = ''
    cheapest_shop = product_comparer(product, ('Десяточка', d_dict), ('Кубит', k_dict), ('Полоса', p_dict))
    lowest_price_list.append(tuple([product, cheapest_shop]))

def group_by_shop(data):
    result = {}
    for product, shop in data:
        result.setdefault(shop, []).append(product)
    return result

grouped = group_by_shop(lowest_price_list)
shops_order = ['Десяточка', 'Кубит', 'Полоса']

for shop in shops_order:
    products_in_shop = grouped.get(shop, []) 
    print(f'{shop}:')
    if not products_in_shop:
        print('–')
    else:
        print(', '.join(products_in_shop))

    
    




