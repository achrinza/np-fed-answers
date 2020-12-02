// Copyright (c) 2020 Rifa I. Achrinza
// This document is licensed under MIT license (See LICENSE for details)
// SPDX-Short-Identifier: MIT

#include <iostream>

//Calculates the value of a given integer raised to the power of a second integer
//param a - the base integer (to be raised to a power).
//param n - the power
//pre: a > 0
//post: return the value of a raised to the nth power.
long power(int a, int n) {
    if (n < 1)
        return 1;

    return a * power(a, n - 1);
}

//print the numbers in an array in the backward manner
//param array - the array in concern
//param n - number of elements in the array
void printBackward(int array[], int n) {
    std::cout << array[n-1];

    if (n > 1)
        printBackward(array, n-1);
}

//return the maximum value in an array of integers
//param array - the array in concern
//param start - start index of the array
//param end   - last index of the array
int maxArray(int array[], int start, int end) {
    if (end - start == 0)
        return array[start];
    else if (end - start == 1)
        if (array[start] > array[end])
            return array[start];
        else
            return array[end];

    int arrayLen = end - start + 1;

    int lowerResult = maxArray(array, start, start + arrayLen / 2);
    int higherResult = maxArray(array, start + arrayLen / 2, end);

    if (lowerResult > higherResult)
        return lowerResult;
    else
        return higherResult;
}


int main()
{
    std::cout << power(2,3) << std::endl;
    std::cout << power(2, 2) << std::endl;
    std::cout << power(2, 1) << std::endl;
    std::cout << power(2, 0) << std::endl;

    std::cout << "---" << std::endl;

    int array5[] = { 1,2,3,4,5 };
    int array4[] = { 1,2,3,4 };
    int array3[] = { 1,2,3 };
    int array2[] = { 1,2 };
    int array1[] = { 1 };
    int array0[1];

    printBackward(array5, 5);
    std::cout << std::endl;
    printBackward(array4, 4);
    std::cout << std::endl;
    printBackward(array3, 3);
    std::cout << std::endl;
    printBackward(array2, 2);
    std::cout << std::endl;
    printBackward(array1, 1);

    std::cout << "\n---" << std::endl;

    std::cout << maxArray(array1, 0, 0) << std::endl;
    std::cout << maxArray(array2, 0, 1) << std::endl;
    std::cout << maxArray(array3, 0, 2) << std::endl;
    std::cout << maxArray(array4, 0, 3) << std::endl;
    std::cout << maxArray(array5, 0, 4) << std::endl;
}
