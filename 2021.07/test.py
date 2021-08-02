nums = [0, 1, 2, 3, 4]
pop_nums = []
for i in range(len(nums) // 2):
    zero_pop = nums.pop(0)
    last_pop = nums.pop(-1)
    pop_nums.append(zero_pop)
    pop_nums.append(last_pop)
    print(nums)
    print(pop_nums)
# print(sorted(a))