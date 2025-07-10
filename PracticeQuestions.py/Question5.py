

for i in range(5):
    n = int(input(f"Enter number{i + 1}"))

print("\nYou entered;" , n)

maximum = max(n)
minimum = min(n)
average = sum(n) / len(n)


print(f"Maximum{maximum}")
print(f"Minimum{minimum}")
print(f"Average{average:}")