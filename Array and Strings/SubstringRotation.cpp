#include <iostream>
#include <string>


bool isSubstring(std::string &a, std::string &b) {
	if (a.length() != b.length()) {
		return false;
	}
	else {
		for (int k = 0; k < b.length(); k++) {
			if (a[0] == b[k]) { // if temp matches any char in string b
				for (int h = 1; h < a.length(); h++) { // loop through the rest of string a to see if it matches with string b
					char temp2 = b[(k + h) % b.length()];
					if (temp2 != a[h]) {
						break;
					}
					else if (h == a.length() - 1) {
						return true;
					}
				}
			}
		}
	}
	return false;
}
int main() {
	std::string a = "waterbottle";
	std::string b = "aterbottlew";
	std::cout << isSubstring(a, b);
}