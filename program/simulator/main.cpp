#include "Simulator.h"
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <string>
#include "Team.h"



int main(int argc, char *argv[])
{
  /*
  int srn = std::stoi(var0);
  while(srn > 0)
  {
  std::string cur_itr = std::to_string(srn);
  std::cout << "\n" << std::endl;

  std::string hfa_string = "home_field_advantage_"+cur_itr;
  std::string as_string = "apply_scaling_"+cur_itr;
  //have to convert to const char * for getenv arg
  //set them to empty strs and then use other pointers to manipulate the values in order to manipulate const
  const char *hfa = "";
  const char *as = "";

  hfa = hfa_string.c_str();
  as = as_string.c_str();
  //get particular environment variables
  char *var1 = getenv(hfa);
  char *var2 = getenv(as);
  //convert to integers
  int home_field_advantage = std::stoi(var1);
  int apply_scaling = std::stoi(var2);
  std::cout << home_field_advantage << std::endl;
  std::cout << apply_scaling << std::endl;
  std::cout << argv[1] << std::endl;
  run(home_field_advantage,apply_scaling,argv[1]);
  //reset();

  srn -= 1;
  }
  */
char *var1 = getenv("home_field_advantage_1");
char *var2 = getenv("apply_scaling_1");
int home_field_advantage = std::stoi(var1);
int apply_scaling = std::stoi(var2);
run(home_field_advantage,apply_scaling,argv[1]);
//setenv("home_field_advantage_1", "1", 1);
}
