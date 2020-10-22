// Copyright (c) 2020 Rifa I. Achrinza
// This document is licensed under MIT license (See LICENSE for details)
// SPDX-Short-Identifier: MIT

#include <iostream>

void print_each_digit(int x, bool firstTime)
{
    if (x >= 10)
        print_each_digit(x / 10, false);

    int digit = x % 10;

    std::cout << digit;

    if (!firstTime) {
        std::cout << "   ";
    }
    else {
        std::cout << std::endl;
    }
}

int main()
{
    do {
        int num;
        int numThousands;

        std::cout << "Enter a 5 digit number: ";
        std::cin >> num;

        numThousands = num / 10000;

        if (numThousands > 9 || numThousands == 0) {
            std::cout << "Invalid number." << std::endl;
            continue;
        }

        print_each_digit(num, true);
        break;
    } while (true);
}
