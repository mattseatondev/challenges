
def today_i_am_feeling(mood):
    m = 'neutral' if not locals().keys() else mood
    return 'Today, I am feeling ' + m

print(today_i_am_feeling('happy'))
print(today_i_am_feeling())