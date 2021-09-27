
def skywalker(name):
    relations = {
        'Darth Vader': 'father',
        'Leia': 'sister',
        'Han': 'brother in law',
        'R2D2': 'droid'
    }
    return f'Luke, I am your {relations[name]}.'

print(skywalker('Darth Vader'))
print(skywalker('Leia'))
print(skywalker('Han'))
print(skywalker('R2D2'))