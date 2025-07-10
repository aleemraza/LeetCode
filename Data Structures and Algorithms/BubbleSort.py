my_array = [7,12,9,11,3,2,1,0]
n = len(my_array)
for i in range(n-1):
    for j in range(n-i-1):
        if my_array[j] > my_array[j+1]:
            my_array[j] , my_array[j+1] = my_array[j+1], my_array[j]
print(my_array)