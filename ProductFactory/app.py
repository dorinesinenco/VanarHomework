from product import *

p1 = new_product({'name': 'pere', 'price': 7, 'quantity': 9})
p2 = new_product({'name': 'mere', 'price': 8, 'quantity': 2})


# p1 = new_product('pere', 7, 6)
# p2 = new_product('mere', 1, 12)

print_product(p1)
print_product(p2)

compare_products(p1, p2)
