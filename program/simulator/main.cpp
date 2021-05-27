#include "Simulator.h"
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include "Team.h"

#ifdef XOPENME
<<<<<<< HEAD
  #include <xopenme.h>
=======
#include <xopenme.h>
>>>>>>> 8b7c9a7f962720948d9fdd313cc2c109fb538466
#endif

int main(int argc, char *argv[])
{
#ifdef XOPENME
  xopenme_init(1,3);
#endif
<<<<<<< HEAD

=======
  
>>>>>>> 8b7c9a7f962720948d9fdd313cc2c109fb538466
char *var1 = getenv("home_field_advantage");
char *var2 = getenv("apply_scaling");
int home_field_advantage = std::stoi(var1);
std::stringstream ss(var2);
bool b;
std::istringstream(var2) >> b;

#ifdef XOPENME
  xopenme_clock_start(0);
#endif

run(home_field_advantage,b,argv[1]);

#ifdef XOPENME
  xopenme_clock_end(0);
#endif

#ifdef XOPENME
  xopenme_dump_state();
  xopenme_finish();
#endif
}
