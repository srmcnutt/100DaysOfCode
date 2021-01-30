with open("file1.txt", "r") as file:
  file1 = file.readlines()

with open("file2.txt", "r") as file:
  file2 = file.readlines()

list1 = [int(num) for num in file1]
list2 = [int(num) for num in file2]

result = [num for num in list1 if (num in list2) ]
#result = [num for ]
# Write your code above 👆

print(result)
