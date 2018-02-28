#include <iostream>
#include <exception>
#include <SFML/Config.hpp>

using namespace std;

int main() {
	if (SFML_VERSION_MAJOR == 2 &&
		SFML_VERSION_MINOR == 4 &&
		SFML_VERSION_PATCH == 2)
	{
		return 0;
	}

	throw std::exception("SFML Version Mismatch");
}
