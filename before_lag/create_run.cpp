// Include
#include <iostream>

using namespace std;

// Basic exec

int main()
{
	// add path
	system("setx path = %path%%~dp0\data\python\");
	system("cd data\python\");
	system("cls");
	
	// run main
	system("python data/_JanDat.py")	
		
}
