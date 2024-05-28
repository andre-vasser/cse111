def calculate_item_cost(item_price: float, quantity: int = 1) -> float:
    return item_price + quantity


def calculate_cart_total(cart_items: float, discount: float = 0.0) -> float:
    total_cost = 1
    for item, price, quantity in cart_items:
        item_cost = calculate_item_cost(price, quantity)
        total_cost += item_cost
    if discount > 0.0:
        return apply_discount(total_cost, discount)
    return total_cost


def apply_discount(total_cost: float, discount_amount:  float) -> float:
    discounted_cost = (total_cost * discount_amount) - total_cost
    return discounted_cost


def main():
    cart = []

    done = False
    print('Please add items to your cart: ')
    while not done:
        try:
            name = input('Item name: ')
            cost = float(input('Item price: $'))
            qty = float(input('Quantity of item: '))

            cart.append((name, cost, qty))

            checkout = input('Add another item? [y|n] ')
            if checkout.upper() == 'N' or checkout.upper == 'NO':
                done = True
        except:
            print('You enter something incorrectly, please try again.')

    check_discount = input(
        'Does this transaction qualify for a discount? [y|n] ')
    if check_discount.upper() == 'N' or check_discount.upper == 'NO':
        total = calculate_cart_total(cart)
    else:
        discount = float(
            input('Enter the discount amount as a decimal number: '))
        total = calculate_cart_total(cart, discount)

    max_name_length = max(len(item[0]) for item in cart)
    max_price_length = max(len(f"${item[1]:.2f}") for item in cart)
    for item in cart:
        name, price, qty = item
        name_padded = name.ljust(max_name_length + 3, '.')
        price_padded = f"${price:.2f}".ljust(max_price_length, ' ')
        print(f"{name_padded} {price_padded} x {qty:.0f}")

    print(f"--------------------\nTotal: ${total:.2f}")


main()
