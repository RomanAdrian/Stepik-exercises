first_number = int(input())
number_list = []
for i in range(0, first_number):
    number_list.append(int(input()))
number_list.sort()
  
def divisible_numbers(first_number, num):
    dictionary = {}
    
    for i in range(2, num-1):
        if (num % i == 0):
            dictionary.setdefault(num, []).append(i)
    
    for k,v in dictionary.items():
        if len(dictionary):
            print(str(k) + ": " + str(v))
     
for i in number_list:
    print(divisible_numbers(first_number, i))