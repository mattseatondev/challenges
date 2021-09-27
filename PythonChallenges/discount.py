
def discount(price, dis):
    return price - (price * float(f'.{dis}'))

print(discount(1500, 50))