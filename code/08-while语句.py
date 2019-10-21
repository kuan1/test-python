# while语句
i = 0
total = 0
while i < 100:
    i += 1
    total += i

print(total)

# break
i = 0
while i < 100:
    i += 1
    if i > 50:
        break
print(i)

# continue
i = 0
while i < 100:
    i += 1
    if i % 10:
        continue
    print(i)
