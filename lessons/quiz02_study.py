"""Quiz02 Study Practice."""

# original 

stats: list[int] = [7, 8, 9]
index: int = 0
total: int = 100
while index < len(stats):
    total -= stats[index]
    index += 1
print(total)

# for...in loop

stats: list[int] = [7, 8, 9]
total: int = 100
for elem in stats:
    total -= elem
print(total)


# for...in...range 

stats: list[int] = [7, 8, 9]
total: int = 100
for elem in range(0, len(stats)):
    total -= stats[elem]
print(total)
