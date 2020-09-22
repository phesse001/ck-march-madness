#include "Simulator.h"
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <string>
#include "Team.h"



int main(int argc, char *argv[])
{
char *var1 = getenv("home_field_advantage_3");
char *var2 = getenv("apply_scaling_3");
int home_field_advantage = std::stoi(var1);
int apply_scaling = std::stoi(var2);
run(home_field_advantage,apply_scaling,argv[1]);
}
