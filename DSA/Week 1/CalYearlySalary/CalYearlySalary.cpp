#include <iostream>
#include <string>

class Employee {
private:
	std::string firstName;
	std::string lastName;
	int monthlySalary;

public:
	Employee() {}

	Employee(
		std::string _firstName,
		std::string _lastName,
		int _monthlySalary
	) {
		firstName = _firstName;
		lastName = _lastName;
		monthlySalary = _monthlySalary;
	}

	std::string getFirstName() {
		return firstName;
	}

	void setFirstName(std::string _firstName) {
		firstName = _firstName;
	}

	std::string getLastName() {
		return lastName;
	}

	void setLastName(std::string _lastName) {
		lastName = _lastName;
	}

	int getMonthlySalary() {
		return monthlySalary;
	}

	void setMonthlySalary(int _monthlySalary) {
		if (_monthlySalary < 0) {
			monthlySalary = 0;
		}
		else {
			monthlySalary = _monthlySalary;
		}
	}
};

int main()
{
	Employee x("James", "Liew", 4200);
	Employee y("Adam", "Tan", 3900);

	std::cout << x.getFirstName() << " " << x.getLastName() << " - $" << x.getMonthlySalary() << std::endl;
	std::cout << y.getFirstName() << " " << y.getLastName() << " - $" << y.getMonthlySalary() << std::endl;

	x.setMonthlySalary(x.getMonthlySalary() * 1.1);
	y.setMonthlySalary(y.getMonthlySalary() * 1.1);

	std::cout << x.getFirstName() << " " << x.getLastName() << " - $" << x.getMonthlySalary() << std::endl;
	std::cout << y.getFirstName() << " " << y.getLastName() << " - $" << y.getMonthlySalary() << std::endl;
}
