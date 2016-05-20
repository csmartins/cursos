import re

#file = open('regex_sum_445822.txt')
file = open('regex_sum_ends_with_378.txt')
count = 0 
for line in file:
	strings = re.findall('[0-9]+', line)
	if strings:
		#print(strings)
		numbers = map(int, strings)
		count += sum(numbers)

print count
