
def count_vowels(txt):
    counter = 0
    vowels = 'aeiou'
    for i in txt:
        if i.lower() in vowels: counter += 1
    return counter

print(count_vowels("Prediction"))