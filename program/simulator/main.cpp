#include "Simulator.h"
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <string>



int main(int argc, char *argv[])
{

  //cout << argv[0] << endl;
  //cout << argv[1] << endl;
  //cout << argv[2] << endl;
  char *var1 = getenv("home_field_advantage");
  char *var2 = getenv("apply_scaling");
  int home_field_advantage = std::stoi(var1);
  int apply_scaling = std::stoi(var2);
  //cout << env << endl;
	//int home_field_advantage = std::stoi(argv[1]);
	//bool apply_scaling = argv[2];
	//int home_field_advantage = argv[1];
	//bool apply_scaling = argv[2];
	//run(home_field_advantage,apply_scaling);

    run(home_field_advantage,apply_scaling);
}
