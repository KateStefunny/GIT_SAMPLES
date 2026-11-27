book = 24.95
discount = 0.40
shipping = 3.00
additional_copy = 0.75
def total_wholesale(copies):
    book_discount = (1.0 - discount)
    book_cost = book_discount * copies
    shipping_cost = shipping + (additional_copy * (copies - 1))
    print(f"book discount {book_discount}")
    return book_cost + shipping_cost
   
print(f"total wholesale cost for 60 copies is {total_wholesale(60):.2f}$")



