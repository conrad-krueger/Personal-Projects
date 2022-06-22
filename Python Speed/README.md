Python Speed
=============================================

This folder contains python scripts that measure the actual speed of certain python operations and utilize that to develop better coding habits. 

-------------------------------------------
speed.py
-------------------------------------------
Short: Finds the quickest way to do common python tasks like initializing a list of length n and what the fastest Iterative 
Control Structure is.

Long: Python's abstraction makes it easier to use, yet difficult to know which method of doing a task is quicker. 
For example, say the user wants to initialize a list (don't know the elements yet) of length n. Should the user do:

[None] * n 

[None for _ in range(n)]

Or should the user just do an empty list and just use .append() for all the elements once they receive them.

This file uses the Python Module time's perf_counter() to answer these questions.


-------------------------------------------
mevsTim.py & mevsTimV2.py
-------------------------------------------
Short: Attempted to create a sorting algorithm faster than Python's built-in sort() function. Ended Up with 
Modified Counting Sort on Integers where the minimum value of the list is 0, the maximum value of the list is <= 
O(n), and n >= 2,000,000.

Long: Python's built-in sort() algorithm seems too good to be true. Given that certain sorting algorithms are 
better than others in certain situations, there had to be at least one scenario in which a different sorting 
algorithm was faster. After some research, Python uses TimSort as its sorting algorithm for large lists (and 
insertion sort for small scale). 

The first attempt at beating TimSort was to try out all of the common sorting algorithms that had the same or 
better time complexity than TimSort (TimSort has O(n log n) time complexity in all cases). Thus, msvsTim.py has 
the implementation of recursive QuickSort (O(n log n) but O(n^2) in worst case), Counting Sort (O(n+k) where k is 
the maximum value of the list), and Bucket Sort (O(n+k)). Not dealing with floating-point numbers yet so Radix 
sort was not implemented. Merge was also not implemented since while it does have the same complexity, Tim Sort 
seems to be one of the fastest, if not the fastest, O(n log n) algorithms out there. 

After running these tests on different list sizes, Tim Sort always came out ahead. This was shocking since only 
integers were used and the maximum integer (k) was not larger than O(n). Thus, Bucket Sort and Counting Sort have 
actual time complexities of O(n). 

However, sort() was written in C which gives Tim a massive timing advantage since C is faster than python.  
Still, at some point, the better time complexity of Counting/Bucket Sort would eventually overtake Tim Sort if n 
got large enough.

Also, it's worth noting Quick Sort had awful timing. So mevsTim2.py was created to just focus on Counting Sort.

Counting Sort was optimized by not including the step where it accumulates the values of the auxiliary list. That 
is one less O(n) for loop, which does not change the time complexity but does make it faster timing-wise. At this 
point, every nanosecond counts. mevsTimv2.py does the same thing as mevsTim.py but just tests Modified 
Counting Sort. These results are much more impressive. As long as the list size is over 2,000,000 elements long, 
Modified Counting Sort is faster. 

UPDATE: Added sort2() to mevsTimv2.py

Allows a user to sort a list of positive and/or negative integers. Time & Space Complexity is O(n + k) where k is 
the difference between the maximum and minimum element in the list. With testing, it seems the list has to 
contain over 5 million elements, with equal amounts of positive and negative integers, to be faster than Tim 
Sort. 

NOTE: Obviously these are not exact brightlines as to when Modified Counting Sort will be faster than Tim Sort. Every device is different.
