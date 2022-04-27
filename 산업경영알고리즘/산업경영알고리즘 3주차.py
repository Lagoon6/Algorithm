import random

def binary_search(list, item):
    low = 0
    high = len(list)-1
    count = 0
    
    while low <= high:
        mid = (low+high)//2
        guess = list[mid]
        count +=1

        if guess == item:
            print(f"{count}번 횟수만에 찾았습니다")
            print(f"리스트의 {mid+1}번째에 있습니다")
            return mid
        elif guess > item:
            high = mid -1
        else:
            low = mid +1
    return print("찾지못하였습니다")

my_list = []
for i in range(0,100):
    number = random.randint(0,100)
    my_list.append(number)
my_list.sort()
    
target = random.randint(0,100)

print(my_list)
print(f"뽑은 숫자는{target}")


print binary_search(my_list,target)

