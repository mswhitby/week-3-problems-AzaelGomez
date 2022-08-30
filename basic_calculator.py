def list_of_multiples(num, length)
return[(i+1)*num for i in range(length)]

result = list_of_multiples(5, 10)
print(result)
