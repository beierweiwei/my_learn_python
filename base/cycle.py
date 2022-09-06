# for in
names = ['a', 'b', 'c']
for name in names:
  print(name)

print(list(range(5)))

sum = 0
for x in range(101):
    sum = sum + x
print(sum)


# break continue
print('while continue...')
n = 0
while n < 10:
  n = n + 1
  if n % 2 == 0:
    continue
  print(n)
