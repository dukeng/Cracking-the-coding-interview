#include <iostream>
#include <string>
using namespace std;

int main() {
	string a;
	cout << "Enter a word: ";
	cin >> a;
	for (int k = 0; k < a.length(); k++) { // loop through from the first char
		for (int h = k + 1; h < a.length() - 1; h++) { // compare it to the rest of the string
			if (a.at(k) == a.at(h)) {
				cout << "not an unique word";
				return 1;
			}
		}
	}

	cout << "is an unique word";
	return 0;
}