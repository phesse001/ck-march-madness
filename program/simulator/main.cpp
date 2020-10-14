#include "Simulator.h"
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include "Team.h"



int main(int argc, char *argv[])
{
char *var1 = getenv("home_field_advantage");
char *var2 = getenv("apply_scaling");
int home_field_advantage = std::stoi(var1);
std::stringstream ss(var2);
bool b;
std::istringstream(var2) >> b;
run(home_field_advantage,b,argv[1]);
}
