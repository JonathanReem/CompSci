import time
import random
from collections import defaultdict
import numpy as np
import numpy.random as nprnd

def flatten(listOfLists):
    "Flatten one level of nesting"
    return chain.from_iterable(listOfLists)


from itertools import chain, repeat

def pure_countsort(unsorted_list):
    counts = {}
    for num in unsorted_list:
        try:
            counts[num] += 1
        except KeyError:
            counts[num] = 1

    sorted_list = list(
        chain.from_iterable(
            repeat(num, counts[num])
            for num in xrange(min(counts), max(counts) + 1)))
    return sorted_list


def timed_countsort(unsorted_list):
	start_time = time.clock()
	counts = (np.bincount(np.array(unsorted_list))).tolist()

	end_time = time.clock()
	print "Making the count took:"
	print end_time - start_time
	
	start_time = time.clock()
	sorted_list = []
	for num in xrange(min(unsorted_list), max(unsorted_list) + 1):
		sorted_list += [num]*counts[num]	
	end_time = time.clock()
	print "Constructing the sorted list took:"
	print end_time - start_time
	
	print "Total time:"
	return sorted_list

def countsort(unsorted_list):
	"Sort a list of integers (ONLY INTEGERS) in linear time. 2-3x faster than sorted() for certain lists."
	counts = (np.bincount(np.array(unsorted_list))).tolist()
	sorted_list = []
	for num in xrange(min(unsorted_list), max(unsorted_list) + 1):
		sorted_list += [num]*counts[num]
	return sorted_list

def smedSort(unsorted_list):
    if len(unsorted_list)<=14:
        for i in range(1,len(unsorted_list)):
            value=unsorted_list[i]
            hole=i
            
            while hole>0 and value<unsorted_list[hole-1]:
                unsorted_list[hole]=unsorted_list[hole-1]
                hole-=1
            unsorted_list[hole]=value
        return unsorted_list
    
    pivot = smedSort([unsorted_list.pop(len(unsorted_list) / 2), unsorted_list.pop(0), unsorted_list.pop(-1)])
     
    less=[]
    firstMiddle=[]
    secondMiddle=[]
    greater=[]
    
    for x in unsorted_list:
        if x <= pivot[0]:
            less.append(x)
        elif x > pivot[0] and x < pivot[1]:
            firstMiddle.append(x)
        elif x >= pivot[1] and x < pivot[2]:
            secondMiddle.append(x)
        else:
            greater.append(x)
    
    less = smedSort(less)
    firstMiddle = smedSort(firstMiddle)
    secondMiddle = smedSort(secondMiddle)
    greater = smedSort(greater)

    return less + list(pivot1) + firstMiddle + list(pivot2) + secondMiddle + list(pivot3) + greater

def np_sort(a):
    "Blazingly fast sort for INTEGERS ONLY that is 40 times faster than sorted() for lists with len > 100"
    return np.repeat(np.arange(a.min(), 1+a.max()), 
    	             np.bincount(a))
def simple_np_sort(unsorted_np_array):
	return unsorted_np_array.sort()

def main():
	size_random_sample = 10 ** 6
	range_upper_limit = 10 ** 5
	print "Generating %i random ints..." % (size_random_sample)
	start_time = time.clock()
	a = nprnd.randint(range_upper_limit, size=size_random_sample).tolist()
	end_time = time.clock()
	print end_time - start_time

	print "Pure Countsort... "
	start_time = time.clock()
	pure_countsort_a = pure_countsort(a)
	end_time = time.clock()
	print_time = end_time - start_time
	print print_time

	print "Jonathan's Sort... "
	start_time = time.clock()
	timed_countsort_a = timed_countsort(a)
	end_time = time.clock()
	print_time = end_time - start_time
	print print_time

	print "Jonathan's Noprint Sort... "
	start_time = time.clock()
	countsorted_a = countsort(a)
	end_time = time.clock()
	noprint_time = end_time - start_time
	print noprint_time

	print "Numpy countsort... "
	np_a = np.asarray(a)
	start_time = time.clock()
	np_sort_a = np_sort(np_a)
	end_time = time.clock()
	np_sort_a_list = np_sort_a.tolist()
	np_sort_time = end_time - start_time
	print np_sort_time
	
	print "Default numpy sort..."
	start_time = time.clock()
	simple_np_sort_a = np_a.sort()
	end_time = time.clock()
	print end_time - start_time

	print "Timsort... "
	start_time = time.clock()
	timsorted_a = sorted(a)
	end_time = time.clock()
	timsort_time = end_time - start_time
	print timsort_time

	if timsort_time > min(noprint_time, print_time):
		times_faster = (timsort_time / min(noprint_time, print_time))
		print "    Your sort is %f times faster than timsort." % (times_faster)

	if timsort_time > np_sort_time:
		times_faster = (timsort_time / np_sort_time)
		print "    Numpy countsort is %f times faster than timsort." % (times_faster)

	if min(noprint_time, print_time) > np_sort_time:
		times_faster = (min(noprint_time, print_time) / np_sort_time)
		print "    Numpy countsort is %f times faster than your sort." % (times_faster)

	try:
		print "Checking sorts... "
		start_time = time.clock()
		assert(countsorted_a == timsorted_a)
		end_time = time.clock()
		print end_time - start_time

		print "Raw countsort is correct. Checking timed countsort..."
		start_time = time.clock()
		assert(timed_countsort_a == timsorted_a)
		end_time = time.clock()
		print end_time - start_time
		
		print "Timed countsort is correct. Checking bucket numpy sort..."
		start_time = time.clock()
		assert(np_sort_a_list == timsorted_a)
		end_time = time.clock()
		print end_time - start_time
		print "Bucket numpy sort is correct."

	except AssertionError:
		print len(timsorted_a), len(timed_countsort_a), len(countsorted_a)

		b = nprnd.randint(100, size=10).tolist()
		pure_counsort_b = 

		timed_countsort_b = timed_countsort(b)
		print timed_countsort_b
		countsort_b = countsort(b)
		print countsort_b
		sorted_b = sorted(b)
		print sorted_b

		if timed_countsort_b != sorted_b and countsort_b != sorted_b:
			malfunc_sort = 'both timed and raw countsorts are'
		elif timed_countsort_b != sorted_b:
			malfunc_sort = 'timed count sort is'
		elif countsort_b != sorted_b:
			malfunc_sort = 'raw count sort is'

		raise AssertionError, '%s not sorting correctly.' % (malfunc_sort)

if __name__ == '__main__':
	main()