from utils import utils

u = utils()

print("--- reversed tests ---")
print("integer:", u.reversed(12345))
try:
    print("string:", u.reversed("12345"))
except TypeError as e:
    print("string:", e)
try:
    print("float:", u.reversed(12345.0))
except TypeError as e:
    print("float:", e)

print("--- formatter tests ---")
print("integer:", u.formatter(12345))
try:
    print("string:", u.formatter("12345"))
except TypeError as e:
    print("string:", e)
try:
    print("float:", u.formatter(12345.0))
except TypeError as e:
    print("float:", e)
