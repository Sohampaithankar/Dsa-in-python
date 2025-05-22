n = int(input("Enter the number of elements: "))
# Input the array
arr = [int(input()) for _ in range(n)]
print(arr)
# Precompute the hash array
hash_array = [0] * 13
for num in arr:
    hash_array[num] += 1

# # Handle the queries
q = int(input("Enter the number of queries: "))
for _ in range(q):
    number = int(input())
    # Fetching the result
    print(hash_array[number])