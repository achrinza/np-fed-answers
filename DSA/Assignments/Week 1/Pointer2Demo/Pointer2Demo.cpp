// Copyright (c) 2020 Rifa I. Achrinza
// This document is licensed under MIT license (See LICENSE for details)
// SPDX-Short-Identifier: MIT

#include <iostream>

void changeValue(int x, int* y)
{
	x = 10;
	*y = 10;
}

int main()
{
	int x = 30;
	int y;
	y = x;
	changeValue(x, &y);

	std::cout << "x: " << x << std::endl;
	std::cout << "y: " << y << std::endl;
}
