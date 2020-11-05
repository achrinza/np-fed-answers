#include "List.h"

List::List() {}

List::~List() {}

bool List::add(ItemType item) {
	return add(size, item);
}

bool List::add(int index, ItemType item) {
	if (index < 0 || index > size) return false;

	Node* newNode = new Node{ item, NULL };

	if (index == 0) {
		newNode->next = firstNode;
		firstNode = newNode;
	}
	else {
		Node* workingNode = firstNode;

		for (int i = 0; i < index - 1; i++)
			workingNode = workingNode->next;

		newNode->next = workingNode->next;
		workingNode->next = newNode;
	}

	size++;
	return true;
}

void List::remove(int index) {
	if (index < 0 || index >= size) {
		return;
	}

	Node* workingNode = firstNode;

	if (index == 0) {
		firstNode = workingNode->next;
		delete workingNode;
	}
	else {
		for (int i = 0; i < index-1; i++)
			workingNode = workingNode->next;

		Node* nextNode = workingNode->next;
		workingNode->next = nextNode->next;
		delete nextNode;
	}

	size--;
}

ItemType List::get(int index) {
	if (index < 0 || index >= size)
		return ItemType{};

	Node* workingNode = firstNode;

	if (index != 0) {
		for (int i = 0; i < index; i++)
			workingNode = workingNode->next;
	}

	return workingNode->item;
}

bool List::isEmpty() {
	return size == 0;
}

int List::getLength() {
	return size;
}

void List::print() {
	Node* workingNode = firstNode;
	std::cout << "---\n";
	while (workingNode != NULL) {
		std::cout << workingNode->item << "\n";
		workingNode = workingNode->next;
	}
	std::cout << "---\n" << std::endl;
}
