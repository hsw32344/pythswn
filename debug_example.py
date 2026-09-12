def calculate_total(raw_price, fee):
    price = float(raw_price)
    total = price + fee
    return total

def hello():
    print('hello')
    return None

result = calculate_total("18.5", 2)
breakpoint()
hello()
print(result)