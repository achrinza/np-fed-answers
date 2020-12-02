// Copyright (c) 2020 Rifa I. Achrinza
// This document is licensed under MIT license (See LICENSE for details)
// SPDX-Short-Identifier: MIT

#include <iostream>
#include <time.h>
#include <random>
#include "Stack.h"
#include "Queue.h"

bool isPalindrome(std::string workingData) {
	Queue queue;
	Stack stack;
	int workingDataLength = workingData.length();
	for (int i = 0; i <= workingDataLength / 2; i++) {
		char workingCharQueue = workingData[i];
		char workingCharStack;

		if (workingDataLength % 2 > 0)
			workingCharStack = workingData[workingDataLength / 2 + i];
		else
			workingCharStack = workingData[workingDataLength / 2 + i - 1];

		queue.enqueue(workingCharQueue);
		stack.push(workingCharStack);
	}

	while (!queue.isEmpty()) {
		ItemType workingCharQueue;
		ItemType workingCharStack;
		queue.dequeue(workingCharQueue);
		stack.pop(workingCharStack);

		if (workingCharQueue != workingCharStack)
			return false;
	}

	return true;
}

int main()
{
	Queue q;
	q.enqueue('a');
	q.enqueue('b');
	q.displayItems();
	q.dequeue();
	q.displayItems();

	std::cout << "Enter a string: ";
	std::string userInput;
	std::cin >> userInput;
	std::cout << std::endl;

	if (isPalindrome(userInput))
		std::cout << "The string is a palindrome";
	else
		std::cout << "The string is not a palindrome";

	std::srand(time(NULL));

	Queue customers;

	for (int i = 0; true; i++) {
		int customerRand = rand() % 100 + 1;

		if (customerRand <= 50) {

		}
	}
}
