// Copyright (c) 2020 Rifa I. Achrinza
// This document is licensed under MIT license (See LICENSE for details)
// SPDX-Short-Identifier: MIT

#pragma once
#include <iostream>
#include "ItemType.h"

class Stack
{
private:
	struct Node
	{
		ItemType item;   // to store data
		Node* next;  // to point to next node
	};

	Node* topNode{ NULL };

public:
	Stack();		// constructor
	~Stack();		// destructor
	bool push(ItemType item);
	bool pop();
	bool pop(ItemType& item);
	void getTop(ItemType& item);
	bool isEmpty();
	void displayInOrder();
	void displayInOrderOfInsertion();
};
