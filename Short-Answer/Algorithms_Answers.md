#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(1). The amount of operations perfomed are constant.


b) O(n). The amount of operations depend on the size of n.



c) O(2^n) due to the recursion occuring on line 29. The function will have to perform an n time of operations, but will at least recurse once.

## Exercise II

To help determining the floor height I will use a binary search.

Asuming the building has 20 floors for example

1. Half the buiding's number of floors and use that as our pivot case.
2. Drop the egg off the 10th floor.
3. If the egg breaks, we can assume going any higher up the building will guarantee a broken egg as well/If the egg doesn't brake, we can assume at the very least the 10th floor isn't enought height for the egg to break. But we can't automatically assume that another higher is going to break an egg.
4. Let's assume the egg breaks on the 10th floor. We will then half the ground level to the 10th floor and get the fifth floor.
5. We will then repeat the pattern on the fifth floor and see if the egg breaks when dropping it.
6. If it does break, half the floors again and go to the second floor. We will repeat this process until we find a floor where the egg doesn't break.

Out of the gate an issue for this solution is that the desired floor might be the third or the fourth floor. So doing it this way may require multiple iterations.

The runtime complexity is O(log n) because we are only performing operations on one instance of n. It isn't exponentialy growing. After the a certain point given an n amount of input the amount of operations is nearly constant. 