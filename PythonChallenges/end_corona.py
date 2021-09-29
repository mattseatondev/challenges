
def end_corona(recovers, new_cases, active_cases):
    counter = 0
    while active_cases > 0:
        counter += 1
        active_cases -= recovers - new_cases
    return counter

print(end_corona(4000, 2000, 77000))

print(end_corona(3000, 2000, 50699))

print(end_corona(30000, 25000, 390205))