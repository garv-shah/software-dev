import itertools

num_list = ['45', '76', '233', '39']

#for nums in list(itertools.permutations(num_list)):
    # print('.'.join(nums))

list1 = ['45', '27', '27', '27']
list2 = ['99', '76', '99', '76']
list3 = ['969', '969', '233', '969']
list4 = ['67', '67', '57', '39']

current_code = []
full_codes = []

for num1 in list1:
    for num2 in list2:
        for num3 in list3:
            for num4 in list4:
                current_code.append(num1)
                current_code.append(num2)
                current_code.append(num3)
                current_code.append(num4)
                print('.'.join(current_code))
                full_codes.append('.'.join(current_code))
                current_code.clear()

print(len(full_codes))