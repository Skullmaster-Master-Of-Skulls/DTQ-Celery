from tasks import add, subtract, multiply, divide

result_add = add.delay(4, 6)
print("Add task dispatched")

result_subtract = subtract.delay(10, 4)
print("Subtract task dispatched")

result_multiply = multiply.delay(3, 7)
print("Multiply task dispatched")

result_divide = divide.delay(8, 2)
print("Divide task dispatched")

try:
    print(f'Add result: {result_add.get(timeout=60)}')
except Exception as e:
    print(f'Add task error: {e}')

try:
    print(f'Subtract result: {result_subtract.get(timeout=60)}')
except Exception as e:
    print(f'Subtract task error: {e}')

try:
    print(f'Multiply result: {result_multiply.get(timeout=60)}')
except Exception as e:
    print(f'Multiply task error: {e}')

try:
    print(f'Divide result: {result_divide.get(timeout=60)}')
except Exception as e:
    print(f'Divide task error: {e}')
