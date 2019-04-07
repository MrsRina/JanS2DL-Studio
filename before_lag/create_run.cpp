// Include
#include <windows.h>
#include <iostream>

using namespace std;

// Basic exec

int main()
{
	// add path
	system("path = data/python/");
	system("cls");
	
	// run main
	system("python data/_JanDat.py");
	
	ShowWindow( GetConsoleWindow(), SW_HIDE );	
		
}
