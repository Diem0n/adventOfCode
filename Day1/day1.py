elves = []
elf = []

with open ('calories.txt', 'r') as f:
    for line in f:
        if (line.strip() == ''):
            elves.append(elf)
            elf = []
        else:
            elf.append(int(line.strip()))

maxcal = 0
for elf in elves:
    if sum(elf) > maxcal:
        maxcal = sum(elf)

print(f'max calories are: {maxcal}')

calories = []
for elf in elves:
    calories.append(sum(elf))

calories.sort(reverse=True)
print(f'the top 3 elves are: {calories[0:3]}')
print(f'the total number of calories by the top 3 elves is: {sum(calories[:3])}')

