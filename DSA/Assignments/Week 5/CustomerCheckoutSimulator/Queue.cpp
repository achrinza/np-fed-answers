// Copyright (c) 2020 Rifa I. Achrinza
// This document is licensed under MIT license (See LICENSE for details)
// SPDX-Short-Identifier: MIT

#include "Queue.h"

Queue::Queue() {
	frontNode = NULL;
	backNode = NULL;
}

Queue::~Queue() {
	while (!isEmpty())
		dequeue();
}

bool Queue::enqueue(ItemType item) {
	Node* newNode = new Node{ item, NULL };
	if (frontNode == NULL) {
		frontNode = newNode;
		backNode = newNode;
	}
	else {
		backNode->next = newNode;
		backNode = backNode->next;
	}

	return true;
}

bool Queue::dequeue() {
	ItemType tmp;
	dequeue(tmp);
	return true;
}

bool Queue::dequeue(ItemType& item) {
	Node* newFrontNode = frontNode->next;
	item = frontNode->item;
	delete frontNode;
	frontNode = newFrontNode;
	return true;
}

void Queue::getFront(ItemType& item) {
	item = frontNode->item;
}

bool Queue::isEmpty() {
	return frontNode == NULL;
}

void Queue::displayItems() {
	Node* workingNode = frontNode;

	while (workingNode != NULL) {
		std::cout << workingNode->item.getName() << workingNode->item.getQueueNum() << std::endl;
		workingNode = workingNode->next;
	}
}
