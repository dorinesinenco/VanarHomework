class _Product():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


def new_product(name, price, quantity):
    return _Product(name, price, quantity)


def print_product(new_p):
    print(
        f'avem {new_p.quantity} {new_p.name} cu prețul de {new_p.price} Lei per bucată.')


def compare_products(x, y):
    if x.price > y.price:
        print(f'Produsul {y.name} este mai ieftin')
    elif x.price < y.price:
        print(f'Produsul {x.name} este mai ieftin')
    else:
        print(f'Produsele {x.name} și {y.name} au același preț')

# print_product(new_product('mere', 8, 2))
