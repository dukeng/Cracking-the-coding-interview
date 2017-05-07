#include<string>
#include<iostream>


int main() {
	std::string a = "This is solution to chapter 1.1.4 in Craking the coding interview";
	std::string add = "%20\0";
	for (int k = 0; k < a.length(); k++) {
		if (a[k] == ' ') {
			a.erase(k, 1);
			a.insert(k, add);
		}
	}
	std::cout << a;
	return 0;
}