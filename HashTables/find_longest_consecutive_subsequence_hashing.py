
def findLongestConseqSubseq(arr, n):

	s = set()
	ans = 0

	# Hash all the array elements
	for ele in arr:
		s.add(ele)

	# check each possible sequence from the start
	# then update optimal length
	for i in range(n):

		# if current element is the starting
		# element of a sequence
		if (arr[i]-1) not in s:

			# Then check for next elements in the
			# sequence
			j = arr[i]
			while(j in s):
				j += 1

			# update optimal length if this length
			# is more
			ans = max(ans, j-arr[i])
	return ans

def getMaxConsecutiveSubSeq(arr):
	sorted_arr = sorted(arr)
	max_count = -1

	n = len(arr)
	i = 0
	j = i+1
	count = 1
	while(i < n and j < n):
		if sorted_arr[j] - sorted_arr[i] == 1:
			count +=1		
		else:
			count = 1

		#print(count)
		i += 1
		j += 1
		max_count = max(max_count, count)

	print("Max subsequence = "+str(max_count))

# Driver code
if __name__ == '__main__':
	n = 7
	arr = [5, 11, 3, 4, 23, 12, 43, 13, 45, 14]
	#print("Length of the Longest contiguous subsequence is "\
	#	+  str(findLongestConseqSubseq(arr, n)))

	getMaxConsecutiveSubSeq(arr)

