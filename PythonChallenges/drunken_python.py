
import builtins

def int(input):
    return builtins.int(input)
def str(input):
    return builtins.str(input)
def int_to_str(int):
    return str(int)
def str_to_int(str):
    return int(str)

print(f'INT TO STR : {(type(int_to_str(4)), int_to_str(4))}')
print(f'STR TO INT : {(type(str_to_int("4")), str_to_int("4"))}')