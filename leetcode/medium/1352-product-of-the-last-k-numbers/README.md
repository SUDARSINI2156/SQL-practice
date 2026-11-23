# Product of the Last K Numbers

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Design an algorithm that accepts a stream of integers and retrieves the product of the last `k` integers of the stream.

Implement the `ProductOfNumbers` class:

- ProductOfNumbers() Initializes the object with an empty stream.
- void add(int num) Appends the integer num to the stream.
- int getProduct(int k) Returns the product of the last k numbers in the current list. You can assume that always the current list has at least k numbers.

The test cases are generated so that, at any time, the product of any contiguous sequence of numbers will fit into a single 32-bit integer without overflowing.

 

 **Example:** 

```
Input
["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"]
[[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]

Output
[null,null,null,null,null,null,20,40,0,null,32]

Explanation
ProductOfNumbers productOfNumbers = new ProductOfNumbers();
productOfNumbers.add(3);        // [3]
productOfNumbers.add(0);        // [3,0]
productOfNumbers.add(2);        // [3,0,2]
productOfNumbers.add(5);        // [3,0,2,5]
productOfNumbers.add(4);        // [3,0,2,5,4]
productOfNumbers.getProduct(2); // return 20. The product of the last 2 numbers is 5 * 4 = 20
productOfNumbers.getProduct(3); // return 40. The product of the last 3 numbers is 2  *5*  4 = 40
productOfNumbers.getProduct(4); // return 0. The product of the last 4 numbers is 0  *2*  5 * 4 = 0
productOfNumbers.add(8);        // [3,0,2,5,4,8]
productOfNumbers.getProduct(2); // return 32. The product of the last 2 numbers is 4 * 8 = 32 

```

 

 **Constraints:** 

- 0 <= num <= 100
- 1 <= k <= 4 * 104
- At most 4 * 104 calls will be made to add and getProduct.
- The product of the stream at any point in time will fit in a 32-bit integer.

 

 **Follow-up:** Can you implement  **both**  `GetProduct` and `Add` to work in `O(1)` time complexity instead of `O(k)` time complexity?

## Solution

**Language:** Python  
**Runtime:** 178 ms (beats 18.75%)  
**Memory:** 28.6 MB (beats 75.00%)  
**Submitted:** 2026-11-23T15:21:01.850Z  

```py
class ProductOfNumbers(object):

    def __init__(self):
        # Initialize with 1 to handle multiplication smoothly
        self.prefix = [1]

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num == 0:
            # Reset prefix products because any future product including this 0 is 0
            self.prefix = [1]
        else:
            # Append the new running product
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        # If k >= len(self.prefix), a zero was added within the last k numbers
        if k >= len(self.prefix):
            return 0
        
        # Use // for integer division so it works in both Python 2 and Python 3
        return self.prefix[-1] // self.prefix[-1 - k]

```

---

[View on LeetCode](https://leetcode.com/problems/product-of-the-last-k-numbers/)