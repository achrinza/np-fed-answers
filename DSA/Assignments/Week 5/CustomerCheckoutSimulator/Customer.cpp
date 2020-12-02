// Copyright (c) 2020 Rifa I. Achrinza
// This document is licensed under MIT license (See LICENSE for details)
// SPDX-Short-Identifier: MIT

// Customer.cpp - Implementation of Customer class
#include "Customer.h"

Customer::Customer() {}

Customer::Customer(string n, int qNum)
{
	name = n;
	queueNum = qNum;
}

void Customer::setName(string n) { name = n; }

string Customer::getName() { return name; }

void   Customer::setQueueNum(int q) { queueNum = q; }

int Customer::getQueueNum() { return queueNum; }
