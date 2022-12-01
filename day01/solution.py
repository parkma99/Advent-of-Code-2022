def solve(input):
    with open(input) as f:
        food_list = f.read().split('\n')
        food_cal = 0
        cals_list = []
        for food in food_list:
            try:
                food_cal += int(food)
            except:
                cals_list.append(food_cal)
                food_cal = 0
        max_cals =  max(cals_list)
        sum_cals = 0
        for _ in range(3):
            sum_cals += max(cals_list)
            cals_list.remove(max(cals_list))
        return (max_cals, sum_cals)
if __name__ == "__main__":
    print(solve("./input.txt"))