import json
import os
import re
import sys

#exports variable to be used in jupyter notebook to give path to files

def ck_postprocess(i):
    misc = i['misc']
    path = misc['path']
    with open(os.path.expanduser("~/.bashrc"), "a") as outfile:
    # 'a' stands for "append"  
        outfile.write("export MARCH_MADNESS_PATH=" + path)

    os.system("echo $MARCH_MADNESS_PATH")
    return {'return':0} 