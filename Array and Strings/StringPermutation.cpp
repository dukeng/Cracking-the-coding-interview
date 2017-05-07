#include <iostream>
#include <string>


bool isPermutation(std::string a, std::string b) {
	std::string small;
	std::string large;
	if (a.length() > b.length()) {
		large = a;
		small = b;
	}
	else {
		large = b;
		small = a;
	}
	for (int k = 0; k < small.length(); k++) {
		bool isPermuted = false;
		for (int h = 0; h < large.length(); h++) {
			if (small[k] == large[h]) {
				isPermuted = true;
				break;
			}
		}
		if (!isPermuted) {
			return false;
		}
	}
	return true;
}

int main() {
	std::string a = "x";
	std::string b = "abcd";
	std::cout << "is a or b a permutation of the other:";
	std::cout << std::boolalpha << isPermutation(a, b) << "/n";
	return 1;
}
