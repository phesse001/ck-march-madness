import json
import os
import re
import sys

#stdout_path gives the path to the output file containing the standard output
#correct_path gives the path to the file containing the correct results
#output_file gives the path to latex table

def ck_postprocess(i):
    ck=i['ck_kernel']
    rt=i['run_time']
    deps=i['deps']
    meta = i['meta']
    misc = i['misc']
    rf1=rt['run_cmd_out1']

    #getting path to output file
    stdout_path = misc['path'] + "/" + misc['tmp_dir'] + "/" + rf1
    correct_path = misc['path'] + "/correct.txt"
    num_displayed_teams = 10
    output_file = "out_table.tex"

    correct = []
    file_1_array = []

    #copy tex/bib files to temp
    os.system("cp " + misc['path'] + "/SOTF.bib " + misc['path'] + "/" + misc['tmp_dir'])
    os.system("cp " + misc['path'] + "/SOTF.tex " + misc['path'] + "/" + misc['tmp_dir'])

    #create table
    with open(correct_path, 'r') as correct_data:
        for line in correct_data:
            correct.append(line.partition(" ")[2].strip())

    with open(stdout_path, 'r') as file_1:
        for line in file_1:
            file_1_array.append(line.partition(" ")[2].strip())

    with open(output_file, 'w') as output:
        output.write('\\begin{tabular}{ |p{2cm}|p{2cm}|  }\n')
        output.write('\\hline\n')
        output.write('\\multicolumn{2}{|c|}{CK Simulated Results} \\\\\n')
        output.write('\\hline\n')
        output.write(' 2019 Results &  Home-Field Advantage 0\\\\\n')
        output.write('\\hline\n')
        for x in range(num_displayed_teams):
            output.write('{} & {}\\\\\n'.format(correct[x], file_1_array[x]))
            output.write('\\hline\n')
        output.write('\\end{tabular}\n')

	#compiile files
    os.system("pdflatex SOTF")
    os.system("bibtex SOTF")
    os.system("pdflatex SOTF")
    os.system("pdflatex SOTF")

    r=ck.load_text_file({'text_file':rf1,'split_to_list':'yes'})
    if r['return']>0: return r
    return {'return':0}