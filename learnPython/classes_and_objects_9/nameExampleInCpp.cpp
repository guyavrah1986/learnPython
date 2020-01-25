#include <iostream>

using namespace std;

int main(int argc, char** argv)
{
	string funcName = "main - ";
	cout << funcName + "start" << endl; 
	
	const char* str1 = "str1";
	const char* str2 = "str1";
	cout << funcName + "the address of str1 is:" << static_cast<const void*>(str1) << ", and it points to:" << str1 << endl;
	cout << funcName + "the address of str2 is:" << static_cast<const void*>(str2) << ", and it points to:" << str2 << endl;
	cout << funcName + "end" << endl; 	
	return 0;
}
