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
