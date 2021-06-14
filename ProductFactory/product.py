class _Product():
    pass
    # def __str__(self):
    #     return f"{self.name} {self.price} {self.quantity}"

# funcția care primește ca argument un tuple
# def new_product(name, price, quantity):
#     _newz = _Product()
#     _newz.name = name
#     _newz.price = price
#     _newz.quantity = quantity
#     return _newz


# funcția care primește ca argument un dicționar
def new_product(dict_prod):
    _newz = _Product()
    _newz.name = dict_prod["name"]
    _newz.price = dict_prod["price"]
    _newz.quantity = dict_prod["quantity"]
    return _newz


def print_product(_newp):
    print(
        f'avem {_newp.quantity} {_newp.name} cu prețul de {_newp.price} Lei per bucată.')


def compare_products(_x, _y):
    if _x.price > _y.price:
        print(f'Produsul {_y.name} este mai ieftin')
    elif _x.price < _y.price:
        print(f'Produsul {_x.name} este mai ieftin')
    else:
        print(f'Produsele {_x.name} și {_y.name} au același preț')
