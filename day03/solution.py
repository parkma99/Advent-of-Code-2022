def same_item(args):
    same= set(args[0])
    for strs in args:
        tmp_set = set(strs)
        same = same & tmp_set
    return same.pop()    
priority = {}
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i, c in enumerate(ascii_lowercase):
    priority[c] = i + 1
for i, c in enumerate(ascii_uppercase):
    priority[c] = i + 27

def solve1(input):
    result = 0
    with open(input) as f:
        rucksacks_list = f.read().split('\n')
        for rucksack  in rucksacks_list:
            size = len(rucksack)
            half_first = rucksack[:size//2]
            half_last = rucksack[size//2:]
            item = same_item((half_first, half_last))
            result += priority[item]
        return result
def solve2(input):
    result = 0
    with open(input) as f:
        rucksacks_list = f.read().split('\n')
        for i in range(0, len(rucksacks_list),3):
            rucksack1 = rucksacks_list[i]
            rucksack2 = rucksacks_list[i + 1]
            rucksack3 = rucksacks_list[i + 2]
            item = same_item((rucksack1, rucksack2, rucksack3))
            result += priority[item]
        return result
if __name__ == "__main__":
    print(solve1("./input.txt"), solve2("./input.txt"))
