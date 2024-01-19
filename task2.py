def calculate_discounted_total(basket, discount_percentage=10):

    total_cost = sum(basket.get(product, 0) for product in basket)

    discount_amount = (discount_percentage / 100) * total_cost

    discounted_total = total_cost - discount_amount

    return discounted_total

products_prices = {
    'apple': 2.50,
    'banana': 1.50,
    'orange': 3.00,
    'grapes': 4.50,
}

basket = {
    'apple': 3,
    'banana': 2,
    'grapes': 1,
}

discounted_total = calculate_discounted_total(basket)

print("discounted total:", discounted_total)

