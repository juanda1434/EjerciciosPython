n = int(input())
nums = numbers = input().split()

for i in range(0, n):
    nums[i] = int(nums[i])

restas = []

for i in range(0, n):
    for j in range((i+1), n):
        if j < n:
            restas.append(abs(nums[i]-nums[j]))

restas.sort()
print(restas)
print(restas[0])
