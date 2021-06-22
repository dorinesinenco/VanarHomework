

def build_pizza(type):
    types = ("Neapolitan", "Sicilian")
    if type in types:
        pizza = {
            "type": type,
            "ingredients": ["dough"]
        }
    else:
        raise TypeError(f"pizza can be made only of types: {types}")
    return pizza


def with_ingredient(pizza, *ingredient):
    # HW2: check for duplicates
    for arg in ingredient:
        if arg in pizza["ingredients"]:
            print(f"{arg} deja este ca ingredient")
            continue
        else:
            pizza["ingredients"].append(arg)
    return pizza


# HW1 retrage un ingredient
def without_ingredient(pizza, *ingredient):
    # retragerea unui ingredient inexistent
    for arg in ingredient:
        if arg == "dough":
            print("there is no pizza without DOUGH")
            continue
        elif arg in pizza["ingredients"]:
            pizza["ingredients"].remove(arg)
        else:
            print(f" {arg} do not exists in ingredients")
    return pizza


def print_pizza(pizza):
    print("#"*20)
    print(f"{pizza['type']}")
    if 'ingredients' in pizza:
        print(" ingredients:")
        for ing in pizza["ingredients"]:
            print(f"   - {ing}")
    else:
        raise KeyError("a pizza obj cannot exist without ingredients")
    print("#"*20)


# p1 = {
#     "type": "Neapolitan",
#     "ingredients": ["dough", "cheese", "tomato"],
# }
# p2 = {
#     "type": "Sicilian",
#     "ingredients": ["dough", "cheese", "tomato", "mozzarella"],
# }
p1 = build_pizza("Neapolitan")
print(p1)

p1 = with_ingredient(p1, "tomato", "cheese", "mushrooms",
                     "garlic", "spinach", "patrunjel", "ceapa")
print("optional", p1)

p1 = without_ingredient(p1, "dough", "tomato")
print("optional", p1)

# p1 = without_ingredient(p1, "patrunjel")
# print("optional", p1)

print_pizza(p1)
