## Problem #1: Multiples of 3 and 5

### Question
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below N.

### Answer
We can get a complexity of O(n) by iterating through the elements and checking whether it is a multiple and summing it up but that's not a good option as it would quickly get out of bounds.
We can look at a simpler solution with O(1) by getting the number of multiples by dividing the number N (actually N-1 beacause below N) with the numbers 3(to get number of multiples of 3)(N3), 5(to get number of multiples of 5)(N5) and also 15(to eliminate the common multiples of 3 and 5 so we include them only once)(N15).
Now that we have the numbers we can use the ((N)(N+1))/2 formula for getting the sum of numbers upto N and multiply that with the required number so as to get the multiples of that number.
Hence it would be 3 x (AP formula for sum of N3) + 5 x (AP formaula for sum of N5) - 15 x (AP formaula for sum of N15)
If you're using python, JS or some other language that automatically makes your variable a float on divide make sure you're using integer division.
Solution at solution.py