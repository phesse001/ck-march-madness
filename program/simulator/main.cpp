#include "Simulator.h"
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>



int main(int argc, char *argv[])
{

  //cout << argv[0] << endl;
  //cout << argv[1] << endl;
  //cout << argv[2] << endl;
  //char *env = getenv("TEST");
  //cout << env << endl;
	//int home_field_advantage = std::stoi(argv[1]);
	//bool apply_scaling = argv[2];
    run(7,true,argv[1]);
}
