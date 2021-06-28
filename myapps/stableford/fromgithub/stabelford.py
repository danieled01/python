#disecting the code

#import the sys module
import sys

#dictionary with key value pairs for score/points on stableford
d = { -4:6, -3:5, -2:4, -1:3, 0:2, 1:1 }

#empty dictionary
golfers = {}

#lines variable assigned to sys.stdin.readlines()
lines = sys.stdin.readlines()

#pars variable assigned to a first value of lines list with strip and split method applied
pars = lines[0].strip().split()

#indices variable assigned to second value of lines list with strip and split method applied
indices = lines[1].strip().split()

#i variable assigned to a value of 2
i = 2

#longest name variable assigned to a value of 0
longest_name = 0

#while loop which states that while i is smaller than len of lines
while i < len(lines):

#line is assigned to the second value of lines list with strip and split method applied
	line = lines[i].strip().split()

#name variable has the the join method applied for ' ' to the line list from 1st to 18th item
	name = ' '.join(line[:-19])

#if statements checking if the len of name is bigger than longest_name
	if len(name) > longest_name:

#if that equals to yes then longest_name will be assigned to the length name instead of 0
		longest_name = len(name)

#added and entry to the golfers dictionary with key of name and value of 0
	golfers[name] = 0

#opened and empty list called stats
	stats = []

#j is assigned to the value of 0
	j = 0

#while loop started which states that whilst j is smaller than 18 do
	while j < 18:

#start appending to the empty stats list with lists within the list
		stats.append([pars[len(pars)-1-j],indices[len(indices)-1-j],line[-1-j],0])

#increase the count of j
		j += 1


	stats = sorted(stats,key= lambda x:int(x[1]))

# handicap variable assigned to the first value of line list
	handicap = int(line[-19])

# handicap variable assigned to the integer division of hcp/18
	extra_shots = int(handicap / 18)

# leftover_shots variable assigned to the integer of hcp % 18 (modulus operator) divide hcp by 18 and give the remainder
	leftover_shots = int(handicap % 18)

# for loop that uses the range of 0 to leftover_shots for a loop counts
	for k in range(0,leftover_shots):

# something being done to the stats list which has had the lambda funtion applied to it above
		stats[k][3] += 1

# for loop on the lambda function
	for stat in stats:
		stat[3] += extra_shots
		try:
			total_score =   int(stat[2]) - int(stat[0]) - int(stat[3])
			if total_score in d:
				golfers[name] += d[total_score]

		except ValueError:
			pass
	i += 1
tuples = []
for key in golfers:
	tuples.append((key,golfers[key]))
tuples = reversed(sorted(tuples,key= lambda x:x[1]))
for(k,v) in tuples:
	sentence = "{:>{}} : {:>2}".format(k,longest_name,v)
	print(sentence)
