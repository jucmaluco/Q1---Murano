<h1> Sorting Algorithim Comparison </h1>
Comparison of the speed of three different sorting algorithms (Quick Sort, Merge Sort, and Bubble Sort) for sorting arrays with N integers, containing numbers ranging from -100,000 to 100,000.

<h1> Libraries used </h1>

<h2> Matplotlib </h2>
This library is used to visualize the performance of the sorting algorithms. It generates plots showing the execution time of each algorithm for different array sizes, making it easier to analyze and compare their efficiency.
To install the library for usage, simply run "pip install Matplotlib" on your code terminal. 

<h2> Others </h2>
Both the time ("import time") and random ("import random") were also used, but are part of Python's standard library, which means it is included with Python by default and do not need to be manually installed.

<h1> Running the code </h1>

After installing the required libraries, users can compare the performance of the sorting algorithms by downloading the file Questão1Murano.py. Once Python and its dependencies are properly set up, running the code is all that’s needed.

To determine the size of the array the user wants to test the sorting algorithims with, all it needs to do is to change the "sizes" variable: 
ie: sizes = [100, 400, 1000, 5000, 10000]  
This variable is used to determine N, the number of integers the arrays will have for each comparison (with 5 comparisons being made in total). 

<h1> Analyzing the results </h1>
The code with the smallest coomputational complexity, even though not the fastest running one, would be Merge Sort. Both Merge and Quick Sort have a complexity of O(n log n), but, the bad selection of the pivot element can cause Quick Sort to have a complexity of O(n²).   

Running Questão1Murano.py, we can generate a graph comparing the sorting speed of the 3 algorithms. With small values of N (varrying from 10 to 1000), we can already notice a significant speed difference: 

![image](https://github.com/user-attachments/assets/e9162772-a25d-4281-b6a1-96552686725c)

When comparing with larger values of N, with N varrying from 10³ to 10⁷, Bubble Sort is an incredibly inneficient way to order an array. Due to it's exponencial growth, computing the sorting of 10⁷ integers on a normal computer would take days. To visualize better the difference between Merge and Quick Sort when dealing with bigger numbers, we can make such graph without adding Bubble Sort: 

![image](https://github.com/user-attachments/assets/1fbc7d14-93e8-4266-8947-cf31940c9115)



