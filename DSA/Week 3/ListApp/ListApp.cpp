// ListApp.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include "List.h"

int main()
{
    List nameList;

    nameList.add("Annie");
    nameList.add("Jackie");
    nameList.add("Wendy");
    nameList.print();
    nameList.add(1, "Brenda");
    nameList.print();
    nameList.remove(3);
    nameList.print();
    nameList.remove(0);
    nameList.print();

}
