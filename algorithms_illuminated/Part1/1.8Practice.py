# 1.1
# Fast forward to the moment after the two outermost recursive calls complete, but before the final Merge step.  Thinking of the two 5-element output arrays of the recursive calls as a glued-together 10-element array, which number is in the 7th position?
# A: 2
# 5 3 8 9 1 7 0 2 6 4
# A: 7th is 2

# 1.2 Consider the following modification to the MergeSort algorithm: divide the input array into thirds (rather than halves), recursively sort each third, and finally combine the results using a three-way Merge subroutine. What is the running time of this algorithm as a function of the length n of the input array, ignoring constant factors and lower-order terms? [Hint: Note that the Merge subroutine can still be implemented so that the number of operations is only linear in the sum of the input array lengths.]
# A: (b) nlogn

# 1.3
# time1 = n
# time2 = 2n
# time3 = 3n
# .
# .
# .
# time = kn
# total = (1+k)*k*n/2
# A: (e) nk*k


# 1.4
# time_1 = n * k/2
# time_2 = 2n *k/4 = n*k/2
# time_3 = 4n *k/8 = n*k/2
# .
# .
# .
# time_log(k/2) = kn/2 *k/k/4 = n*k/2
# A: (c) nklogk


# 1.5
# n + log2 n – 2
def find_2nd_largest(arr: list) -> int:
    first = second = -1
    for i in arr:
        if i > first:
            second = first
            first = i
        elif i > second:
            second = i
    return second


data = [2, 3, 12, 31, 2, 1212, 3, 12, 2121, 23, 4]
print(find_2nd_largest(data))
data.sort()
print(data[-2])


# 1.6
def Karatsuba(num1: str, num2: str) -> str:
    return ""
