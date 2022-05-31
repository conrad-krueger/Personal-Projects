Python Speed
=============================================

This folder contains python scripts that measure the actual speed of certain python operations and utilize that to develop better coding habits. 

-------------------------------------------
speed.py
-------------------------------------------
Short: Finds the quickest way to do common python tasks like: initialize a list of length n, fastest Iterative Control Structure.

Long: One thing I like and hate about Python is that there is a lot of abstraction. That makes things a lot easier when writing code but when it comes to efficency (where the nanosecond counts)
then its difficult to know which method of doing a task is quicker. For example, say I want to initalize a list (don't know the elements yet) of length n. Should I do:
[None] * n 
[None for _ in range(n)]
Or should I just do an empty list and just use .append() for all the elements once I receive them.

This file uses the Python Module time's perf_counter() to answer these questions.


-------------------------------------------
mevsTim.py & mevsTimV2.py
-------------------------------------------
Short: Attempted to create a sorting algorithm faster than Python's builtin sort() function. Ended Up with Modified Counting Sort on Integers where the minimum value of the list is 0, the maximum value of the list is in O(n), and n >= 2,000,000.

Long: After taking Data Structures and Algorithms (having learned a plethora of sorting algorithms, some of which have their own advantages), I recalled python having a built in sort() algorithm and thinking to myself, why? There has got to be certain scenarios in which 
a different sorting algorithm is faster than the one implemented here. I did some research and found out Python uses TimSort as its sorting algorithm for large lists (and insertion sort for small scale). My first instinct was to try out out all of the common sorting algorithms that had the same or 
better time complexity than TimSort (TimSort has O(n log n) time complexity in all cases). Thus, msvsTim.py has the implementation of recursive QuickSort (O(n log n) and is very fast), Counting Sort (O(n+k) where k is the maximum value of the list), and Bucket Sort (O(n+k)). Not dealing with floating 
point numbers yet so I didn't bother with Radix. I also didn't bother with merge since while it does have the same complexity, Tim Sort seems to be one of the fastest, if not the fastest, O(n log n) algorithms out there. After running theses tests on different list sizes, Tim Sort always came ahead. This shocked me
since I was only testing scenarios where integers were used and the maximum integer (k) was not larger than O(n). Thus, Bucket Sort and Counting Sort have actual time complexities of O(n). After doing a bit more digging, I found out, like many of the prewritten functions in Python, Tim Sort was written in C.
This givens Tim a massive advantage over me. Even if I have better time complexity, Python's sort would run faster (for pretty large n's) simply becuase it was written in C. However, I knew that at some point, the better time complexity of Counting/Bucket Sort would eventually overtake Tim Sort if n got large enough.
Also, its worth noting Quick Sort had awful timing. It was the slowest implemented which makes sense (and it was the recursive implementation which is even slower). So I created mevsTim2.py to just focus on Counting Sort.

I decided to optimize Counting Sort by not including the step where it accumulates the values of the axuillary list. That is one less O(n) for loop, which does not change the time complexity but does make it faster timing wise. At this point, I am just try to save every nanosecond I can and find an n in which
this will go faster. mevsTimv2.py does the same thing as mevsTim.py but just tests my modified counting sort. These results are much more impressive. As long as the list size is over 1,000,000 elements long, Modified Counting Sort is faster. mevsTimv2.py also attempts to see how far this sorting algorithm can go.
mevsTimv2.py's Counting Sort had a bunch of preconditions that will make it faster than Tim Sort:
- The maximum value is less than or equal to O(n)
- Minimum element in the list is 0.
- Must only be working with integers


