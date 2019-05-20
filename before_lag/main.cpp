// Created by Sir Rina to run JanCreate Studio ;
// Include ;
#include <iostream>

using namespace std;

int main()
{
	// SET PATH : ;
	system("setx path = %path%%~dp0\data\python/");

	// FIND PYTHON : ;
	system("cd data\python\ ");

	// PYTHON COMPILE APLICATION : ;
	system("python '%~dp0\data\_JanDat.py'");
	
	system("pause");
}
