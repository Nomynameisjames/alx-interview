                                            Rotate 2D Matrix

This algorithm is used to rotate a 2D matrix by 90 degrees in clockwise direction.
The input is a square matrix (n x n) and the output is the same matrix rotated by 90 degrees in clockwise direction.

    Approach

The approach used in this algorithm is to rotate the matrix layer by layer. For each layer, we select the top element,
rotate the elements in clockwise direction and place them in their new positions.
We then repeat this process for the remaining layers until the entire matrix is rotated.

    Algorithm Steps

Create a function that takes a square matrix as input.
Calculate the number of layers in the matrix.
For each layer, starting from the outermost layer and moving inwards:
a. Calculate the index of the first and last elements of the current layer.
b. For each element in the top row of the current layer, rotate it to its new position.
c. For each element in the right column of the current layer, rotate it to its new position.
d. For each element in the bottom row of the current layer, rotate it to its new position.
e. For each element in the left column of the current layer, rotate it to its new position.
Return the rotated matrix.

    Time and Space Complexity

The time complexity of this algorithm is O(n^2), where n is the number of elements in the matrix.
This is because we need to iterate through each element in the matrix in order to rotate it.

The space complexity of this algorithm is O(1), because we are rotating the matrix in-place and not using any additional data structures.
