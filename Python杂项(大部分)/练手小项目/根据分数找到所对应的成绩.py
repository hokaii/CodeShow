import bisect
def grade(score,breakpoints=[60,70,80,90],grades='FDCBA'):
	i=bisect.bisect(breakpoints,score)
	return grades[i]

print([grade(score) for score in [34,66,97,78,56,43,23]])