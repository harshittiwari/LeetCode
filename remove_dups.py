#https://leetcode.com/discuss/57555/delete-duplicates-from-string-also-lexicographical-order

def remove_dups(s):
	# index,minimum,maximum
	# index, toggle
	li = [[False,True] for _ in range(26)]
	s1 = ""
	for i in range(len(s) - 1,-1,-1):
		ch = s[i]
		ind = ord(ch) - 97
		if not li[ind][0]:
			li[ind][0] = True
			s1 = ch + s1
			for j in range(len(li)):
				item = li[j]
				if item[0]:
					if j > ind:
						item[1] = False
					elif j < ind:
						item[1] = True
		else:
			if li[ind][1]:
				s1 = ch + s1.replace(ch,"")# s1[:li[ind][0]] + s1[li[ind][0]+1:]
				#li[ind][0] = 0
				li[ind][1] = False
	return s1

print(remove_dups("cbacdcbc"))
print(remove_dups("bcabc"))