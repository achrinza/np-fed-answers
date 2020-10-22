// Copyright (c) 2020 Rifa I. Achrinza
// This document is licensed under MIT license (See LICENSE for details)
// SPDX-Short-Identifier: MIT

#include <iostream>

int main()
{
    // a
    int value1 = 200000;

    // b
    int value2;

    // c
    int* ptr;

    // d
    ptr = &value1;

    // e
    std::cout << "ptr value: " << *ptr << std::endl;

    // f
    value2 = *ptr;

    // g
    std::cout << "value2 value: " << value2 << std::endl;

    // h
    std::cout << "value1 address: " << &value1 << std::endl;

    // i
    std::cout << "ptr ref. address: " << ptr << std::endl;

    // j
    value2 = *ptr;

    // k
    *ptr = 2000;

    // l
    std::cout << "value1 value: " << value1 << std::endl;
    std::cout << "value2 value: " << value2 << std::endl;
}
