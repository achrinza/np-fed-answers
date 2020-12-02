// Copyright (c) 2020 Rifa I. Achrinza
// This document is licensed under MIT license (See LICENSE for details)
// SPDX-Short-Identifier: MIT

#include <iostream>
#include "Stack.h"

int main()
{
    Stack s;
    s.push(3);
    s.push(4);
    int stackTop;
    s.getTop(stackTop);
    std::cout << stackTop << std::endl;
    s.displayInOrderOfInsertion();
    s.pop();
    s.displayInOrderOfInsertion();
}
