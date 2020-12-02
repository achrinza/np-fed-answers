// Copyright (c) 2020 Rifa I. Achrinza
// This document is licensed under MIT license (See LICENSE for details)
// SPDX-Short-Identifier: MIT

// CustomerCheckoutSimulator.cpp : This file contains the 'main' function. Program execution begins and ends there.

#include <iostream>
#include<time.h>
#include "Queue.h"
#include "Customer.h"

int main()
{
	std::srand(time(NULL));
	const int duration = 100000;
	int customerServedCounter = 0;
	int serveDurationCounter = 0;

	Queue customers;

	for (int i = 1; i <= duration; i++) {
		const int customerRand = rand() % 4 + 1;
		Customer dequeuedCustomer;

		if (!customers.isEmpty()) {
			customers.dequeue(dequeuedCustomer);
			customerServedCounter++;
			serveDurationCounter += i - dequeuedCustomer.getQueueNum();
		}

		switch (customerRand) {
		case 2:
			customers.enqueue(Customer{ "", i });
		case 1:
			customers.enqueue(Customer{ "", i });
			break;
		}
	}

	int calc;

	if (customerServedCounter > 0) {
		calc = serveDurationCounter / customerServedCounter;
	} else
		calc = 0;

	std::cout << "Avg. duration: " << calc;
}
