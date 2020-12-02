// Copyright (c) 2020 Rifa I. Achrinza
// This document is licensed under MIT license (See LICENSE for details)
// SPDX-Short-Identifier: MIT

#include <iostream>
#include <string>
#include "Stack.h"
int main()
{
    Stack back_stack;
    std::string temp;
    while (temp != "0")
    {
        std::cout << "[1] Visit URL\n[2] Back\n[0] Exit\nYour Choice: ";
        std::cin >> temp;
        if (temp == "0")
            break;
        else if (temp == "1") {
            std::string url;
            std::cout << "URL: ";
            std::cin >> url;
            back_stack.push(url);
        }
        else if (temp == "2") {
            back_stack.pop();
        }
    }
    return 0;
}
