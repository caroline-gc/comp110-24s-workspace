"""Scratch Code"""

def view(my_list: list[str]):
    idx: int = 0
    while idx < len(my_list):
        print(my_list[idx])
        idx += 1

msg: list[str] = ["Hello", "World"]
view(msg)
print(msg)


def lessen(my_list1: list[str]):
    idx1: int = 0
    while idx1 < len(my_list1):
        my_list1[idx1] = my_list1[idx1] - 1
        idx1 += 1

msg1: list[str] = [4, 5, 6]
lessen(msg1)

print(msg1)

x: list[float] = [1.0, 2.0]
y: list[float] = [3.0, 4.0]
y = x
x[0] = 3.0

print(x)
print(y)


def double(x: int) -> int:
    return x * 2

def double_display(y: int):
    print(y * 2)

double_display(2)
    
if __name__ == "__main__":
    print(double(3))

from b.a import double, double_display

print(double(1))
double_display(4)
