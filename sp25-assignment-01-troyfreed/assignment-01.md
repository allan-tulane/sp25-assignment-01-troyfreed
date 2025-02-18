

# CMPS 2200 Assignment 1

**Name:**Troy Freed


In this assignment, you will learn more about asymptotic notation, parallelism, functional languages, and algorithmic cost models. As in the recitation, some of your answer will go here and some will go in `main.py`. You are welcome to edit this `assignment-01.md` file directly, or print and fill in by hand. If you do the latter, please scan to a file `assignment-01.pdf` and push to your github repository. 
  
  

1. (2 pts ea) **Asymptotic notation** (12 pts)

  - 1a. Is $2^{n+1} \in O(2^n)$? Why or why not? 
.Yes this is True, because Big O notation based on the growth pattern and even though it will always be 1 power higher
.you can use constant 2, to make 2^{n+1} = 2 * 2^n. Because this can be equaled by using a constant
.it shows they grow at the same rate and make this statement true.
.  
. 
  - 1b. Is $2^{2^n} \in O(2^n)$? Why or why not?     
.  To see if 2^{2^n} ∈ O(2^n) need to check if there exists a constant, c where 2^2^n = c * 2^n.
.  If we make 2^2^n = (2^2)^n = 4^n, then we have 4^n = c * 2^n
.  by dividing both side by 2^n we are left with 2^n = c, however there is no
.  constant that can keep up with exponential growth, making this false.
.  
  - 1c. Is $n^{1.01} \in O(\mathrm{log}^2 n)$?    
.  This is false because n^1.01 grows polynomially and log^2(n) grows logarithmically
.  There is no constant you can multiply by a logarithmic function to be faster than 
.  a polynomial function when n grows large enough, making it false.
.  

  - 1d. Is $n^{1.01} \in \Omega(\mathrm{log}^2 n)$?  
.  
.  This is true because if looking at all n > 0, a polynomial function grows much faster than a logarithmic function,
.  No matter what constant multiple you put on log^2(n), at some point if n is large enough n^1.01 will be much larger.
.  This means that log^2(n) is a lower bound making the statement true.

  - 1e. Is $\sqrt{n} \in O((\mathrm{log} n)^3)$?  
.  No this is false because there is no constant that will make log(n)^3 faster than n^1/2.
.  Even though n^1/2 grows slower than linear, it still increases at a rate proportional to square root of n
.  logarithmic functions grow exponentially slower, so even though it is cubed at a certain point n^1/2 will be much larger
.  making the statement false.
  - 1f. Is $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$?  
.Yes this is true, as the same reasons listed above even though n^1/2 grows slower than linear it still grows at
. a rate that is faster than a logarithmic function even if it is cubed. No matter what constant gets put in
. for log(n)^3, at some point when n is large enough n^1/2 will become larger, making log(n)^3 a lower bound and the statement true


2. **SPARC to Python** (12 pts)

Consider the following SPARC code of the Fibonacci sequence, which is the series of numbers where each number is the sum of the two preceding numbers. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ... 
$$
\begin{array}{l}
\mathit{foo}~x =   \\
~~~~\texttt{if}{}~~x \le 1~~\texttt{then}{}\\
~~~~~~~~x\\   
~~~~\texttt{else}\\
~~~~~~~~\texttt{let}{}~~(ra, rb) = (\mathit{foo}~(x-1))~~,~~(\mathit{foo}~(x-2))~~\texttt{in}{}\\  
~~~~~~~~~~~~ra + rb\\  
~~~~~~~~\texttt{end}{}.\\
\end{array}
$$ 

  - 2a. (6 pts) Translate this to Python code -- fill in the `def foo` method in `main.py`  

  - 2b. (6 pts) What does this function do, in your own words?  

.  
.  This is a recursive function for the Fibonacci sequence. It starts off taking input x, if x = 1 it will return 1, and if x = 0 it will return 0. 
.  Otherwise, it will take the sum of foo(x - 1) +foo( x - 2). The function creates a tree, which ends when it returns 0 and 1. 
.  The function creates a pattern where the sum of the last 2 numbers in the sequence creates the next number, replicating the Fibonacci sequence.
.  

  

3. **Parallelism and recursion** (26 pts)

Consider the following function:  

```python
def longest_run(myarray, key)
   """
    Input:
      `myarray`: a list of ints
      `key`: an int
    Return:
      the longest continuous sequence of `key` in `myarray`
   """
```
E.g., `longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3`  
 
  - 3a. (7 pts) First, implement an iterative, sequential version of `longest_run` in `main.py`.  

  - 3b. (4 pts) What is the Work and Span of this implementation?  

.  
.  
.  Because we have a single loop that iterates over each element of my_array exactly once doing the same amount of work for each iteration, Work = O(n), 
.  because the total amount of work directly depends on the number of elements.
.  
.  Each iteration depends on the updated value of current_count from the previous iteration. Meaning iteration i + 1, needs iteration i to finish before it can start. 
.  This means the longest chain of dependencies is the my_array loop, making Span = O(n)


  - 3c. (7 pts) Next, implement a `longest_run_recursive`, a recursive, divide and conquer implementation. This is analogous to our implementation of `sum_list_recursive`. To do so, you will need to think about how to combine partial solutions from each recursive call. Make use of the provided class `Result`.   

  - 3d. (4 pts) What is the Work and Span of this sequential algorithm?  
.  
.  For the sequential algorithm you process each element exactly once and do the same amount of work making total work
.  proportial to number of element so work is O(n)
.  
.  Because the algorithm is sequential, the algorithm still has to process each element once, making each iteration
.  dependent on the previous one, and making span O(n) as well. Typically if the divide and conquer alogirthm was used
.  in a setting where you have many processors it would lead to O(log(n)), but if solving sequentially
.  you have S(n/2) + S(n/2) + O(1), and both of the S(n/2) are dependent on each other. This makes it 2 * S(N/2), and 
. the answer for the span O(n)


  - 3e. (4 pts) Assume that we parallelize in a similar way we did with `sum_list_recursive`. That is, each recursive call spawns a new thread. What is the Work and Span of this algorithm?  

.  
.  When you parallelize the recrusive calls so that the two halves are processed at the same time
.  the time becomes T(n) = T(n/2) + T(n/2) + O(1), with the T(n/2) representing both halves and O(1) the 
.  work to merge. 
.  
.  The Work measures the number of operations done whether it is concurrent or sequentially. This 
.  means that even if these operations can be done recursively the work stays the same, equalling O(n)
. 
.  For the span since the two recursive calls can run in parellel, the span is determined by the longest function
.  which is S(n/2), making S(n) = S(n/2) + O(1), which equals O(log(n)) 
. 

