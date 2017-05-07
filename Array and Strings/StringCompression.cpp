#include <iostream>
#include <string>

std::string compressString(std::string &a) {
	int count = 0;
	std::string b;
	char temp = a[0];
	for (int k = 1; k < a.length(); k++) {
		if (temp == a[k]) {
			count++;
			if (k == a.length() - 1) {
				b += temp + std::to_string(count + 1);
				count = 0;
				temp = a[k];
			}
		}
		else {
			b += temp + std::to_string(count + 1);
			count = 0;
			temp = a[k];
		}

	}
	if (b.length() >= a.length()) {
		return a;
	}
	else {
		return b;
	}
}
int main() {
	std::string a = "aaabbbcccc";
	std::string b = "zahlergrg";
	std::string compressed1 = compressString(a);
	std::string compressed2 = compressString(b);
	std::cout << compressed1;
	std::cout << compressed2;
	return 1;
}