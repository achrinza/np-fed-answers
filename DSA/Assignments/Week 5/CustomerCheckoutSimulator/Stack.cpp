// Copyright (c) 2020 Rifa I. Achrinza
// This document is licensed under MIT license (See LICENSE for details)
// SPDX-Short-Identifier: MIT

#include "Stack.h"

Stack::Stack() {}

Stack::~Stack() {
	while (pop());
}

bool Stack::push(ItemType item) {
	return topNode = new Node{ item, topNode };
}

bool Stack::pop() {
	ItemType tmp;
	return pop(tmp);
}

bool Stack::pop(ItemType& item) {
	if (isEmpty())
		return false;

	auto deletableNode = topNode;
	topNode = topNode->next;
	item = deletableNode->item;
	delete deletableNode;
	return true;
}

void Stack::getTop(ItemType& item) {
	if (!isEmpty())
		item = topNode->item;
}

bool Stack::isEmpty() {
	return !topNode;
}

void Stack::displayInOrder() {
	auto workingNode = topNode;

	while (workingNode) {
		std::cout << workingNode->item.getName() << workingNode->item.getQueueNum() << std::endl;
		workingNode = workingNode->next;
	}
}

void Stack::displayInOrderOfInsertion() {
	auto tmpStack = new Stack{};
	auto workingNode = topNode;

	while (workingNode) {
		tmpStack->push(workingNode->item);
		workingNode = workingNode->next;
	}

	tmpStack->displayInOrder();
	delete tmpStack;
}
