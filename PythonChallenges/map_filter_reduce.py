
# ---MAP---

lst = list(range(0, 31))

temps = [('Berlin', 29), ('Cairo', 36), ('Buenas Aires', 20), ('LA', 23), ('Tokyo', 18)]
# conversion ˚C to ˚F : F = 9/5 * C + 32

def run_map(l):
    # radii -> area
    return list(map(area, l))

def area(r):
    return round((3.141592653589793 * r) ** 2)

def map_with_lambda():
    return list(map(c_to_f, temps))

c_to_f = lambda data: (data[0], (9/5) * data[1] + 32)

# print(run_map(lst))
# print(map_with_lambda())


# ---FILTER---

import statistics
data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
def run_filter(l):
    avg = statistics.mean(data)
    print(f'FULL LIST: {l}')
    print(f'AVG: {avg}')
    return list(filter(lambda x: x > avg, data))
# print(run_filter(data))

dinos = ['', '', 'Velociraptor', '', 'Steagasaurus', 'Cyclops', '', 'Tyranadon']
def elim_noval(l):
    return list(filter(None, l))
# print(elim_noval(dinos))


# ---REDUCE--- :: PROBABLY JUST USE A FOR LOOP
from functools import reduce
rng = range(1, 20)
def run_reduce(r):
    multiplier = lambda x, y: x*y
    return reduce(multiplier, r)
print(run_reduce(rng))
def reduce_with_for_loop(r):
    prod = 1
    for i in r:
        prod *= i
    return prod
print(reduce_with_for_loop(rng))