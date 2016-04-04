#include <iostream>
#include <string>


void reverseChar(std::string a) {
	for (int k = 0; k < a.length() / 2; k++) {
		char temp = a[k];
		a[k] = a[a.length() - 1 - k];
		a[a.length() - 1 - k] = temp;
	}
	std::cout << " reveresed string is: " << a;
}

int main() {
	std::string a = "properties";
	std::string b = "neccessary";
	reverseChar(a);
	reverseChar(b);
	return 1;
}

