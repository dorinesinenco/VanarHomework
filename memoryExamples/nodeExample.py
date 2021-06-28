# [HEAD]-- next -->[VALUE1]-- next -->[VALUE2]-- next --> None

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"[{self.value}] -- next --> {self.next}"


# adaugarea inca a 3 noduri
# first = Node(100)
# second = Node(200)
# third = Node(300)
# fourth = Node(400)
# fifth = Node(500)
# first.next = second
# second.next = third
# third.next = fourth
# fourth.next = fifth
# print(first)


#  adaugarea automat a 5 valori printr-un ciclu
for val in range(100, 600, 100):
    ob = Node(val)
    print(ob)
