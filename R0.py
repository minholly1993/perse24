# Q1
x = int(input())
y = int(input())
z = int(input())
print(int(x+12*(y*z)))

# Q2
a = int(input())
b = int(input())
print(int(a // b))

# Q3
a = input()
print(str(a[2:] + a[:2]))

# Q4
a = input()
b = input()
c = input()
if a == b:
  if a == c:
    print("OK")
  else:
    print("ENTRY 3 MISMATCH")
else:
  if b == c:
    print("ENTRY 1 MISMATCH")
  else:
    if a == c:
      print("ENTRY 2 MISMATCH")
    else:
      print("BOTH MISMATCH")

# Q5
a = input()
if a == "t" or a == "c":
  n = int(input())
  print(str(n + 1))
else:
  print("1")

# Q6
a = 0
while a < 12:
  a += int(input())
print(a-12)

# Q7
