import os
#
# Collective Knowledge ()
#
# 
# 
#
# Developer: 
#

cfg={}  # Will be updated by CK (meta description of this module)
work={} # Will be updated by CK (temporal data)
ck=None # Will be updated by CK (initialized CK kernel) 

# Local settings

##############################################################################
# Initialize module

def init(i):
    """

    Input:  {}

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """
    return {'return':0}

##############################################################################
# TBD: action description

def explore(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """
    r=ck.access({'action':'find', 'module_uoa':'program', 'data_uoa':'simulator'})
    if r['return']>0: return r # use standard error handling in the CK
    program_path=r['path']

    #change to tmp directory where all run files are
    os.chdir(program_path + "/tmp")

    #getting path to output file
    stdout_path = program_path + "/tmp/stdout.log"
    correct_path = program_path + "/correct.txt"
    num_displayed_teams = 10
    output_file = "out_table.tex"

    correct = []
    file_1_array = []

    #get CK entry with the paper template
    r=ck.access({'action':'find', 'module_uoa':'paper', 'data_uoa':'ck-march-madness'})
    if r['return']>0: return r # use standard error handling in the CK
    paper_path=r['path']

    #copy tex/bib files to temp
    os.system("cp " + paper_path + "/SOTF.bib " + program_path + "/tmp")
    os.system("cp " + paper_path + "/SOTF.tex " + program_path + "/tmp")

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

    return {'return':0}

##############################################################################
# generate paper

def generate_paper(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import os

    r=ck.access({'action':'find', 'module_uoa':'program', 'data_uoa':'simulator'})
    if r['return']>0: return r # use standard error handling in the CK
    program_path=r['path']

    #change to tmp directory where all run files are
    os.chdir(program_path + "/tmp")

    #compile files
    os.system("pdflatex SOTF")
    os.system("bibtex SOTF")
    os.system("pdflatex SOTF")
    os.system("pdflatex SOTF")

    return {'return':0}
