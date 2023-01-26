# The Pascal's Triangle Technical Interview Challenge.
---
#### My approach is to use two for loops(nested), the outer loop iterates over the rows of the triangle, while the inner loop iterates over a temp list which keeps adding the value at the first index to the value at the next index. The temp list is then added a new row list. The new row list is then added to the the triangle list which contains all other row lists.

#### This approach takes a O(n^2) time complexity and a space complexity of O(n^2).
