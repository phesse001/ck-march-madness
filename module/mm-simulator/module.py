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
# runs march madness program with three sets of inputs
# tbd retrieve actual inputs from meta

def run(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """
    #find simulator entry
    r=ck.access({'action':'find', 'module_uoa':'program', 'data_uoa':'simulator'})
    if r['return']>0: return r # use standard error handling in the CK
    path = r['path']

    #find results entry
    r=ck.access({'action':'find', 'module_uoa':'mm-simulator', 'data_uoa':'results'})
    if r['return']>0: return r # use standard error handling in the CK
    r_path = r['path']

    r=ck.access({'action':'compile', 'module_uoa':'program', 'data_uoa':'simulator'})
    if r['return']>0: return r # use standard error handling in the CK
    
    print("\nHome_Field_Advantage: 0\nApply_Scaling: True")
    r=ck.access({'action':'run', 'module_uoa':'program', 'data_uoa':'simulator'})
    if r['return']>0: return r # use standard error handling in the CK

    os.system("cp " + path + "/tmp/stdout.log " + path + "/tmp/stdout1.log")

    print("\nHome_Field_Advantage: 4\nApply_Scaling: True")
    r=ck.access({'action':'run', 'module_uoa':'program', 'data_uoa':'simulator', 'env.home_field_advantage':'4'})
    if r['return']>0: return r # use standard error handling in the CK

    os.system("cp " + path + "/tmp/stdout.log " + path + "/tmp/stdout2.log")
    
    print("\nHome_Field_Advantage: 8\nApply_Scaling: True")
    r=ck.access({'action':'run', 'module_uoa':'program', 'data_uoa':'simulator', 'env.home_field_advantage':'8'})
    if r['return']>0: return r # use standard error handling in the CK

    os.system("cp " + path + "/tmp/stdout.log " + path + "/tmp/stdout3.log")

    #copy files to results entry to use for dashboard graph later

    os.system("cp " + path + "/tmp/stdout1.log " + r_path)
    os.system("cp " + path + "/tmp/stdout2.log " + r_path)
    os.system("cp " + path + "/tmp/stdout3.log " + r_path)

    #removes duplicate file of stdout1.log
    os.system("rm stdout.log")
    print("\nResults can be found in " + path + "/tmp directory\n\nRun 'ck {action} mm-simulator --help to learn more about a specified action\n")

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
    r=ck.access({'action':'find', 'module_uoa':'program', 'data_uoa':'simulator'})
    if r['return']>0: return r # use standard error handling in the CK
    program_path=r['path']

    #change to tmp directory where all run files are
    os.chdir(program_path + "/tmp")

    #getting path to output file
    stdout_path1 = program_path + "/tmp/stdout1.log"
    stdout_path2 = program_path + "/tmp/stdout2.log"
    stdout_path3 = program_path + "/tmp/stdout3.log"
    correct_path = program_path + "/correct.txt"
    num_displayed_teams = 10
    output_file = "out_table.tex"

    correct = []
    file_1_array = []
    file_2_array = []
    file_3_array = []

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

    with open(stdout_path1, 'r') as file_1:
        for line in file_1:
            file_1_array.append(line.partition(" ")[2].strip())

    with open(stdout_path2, 'r') as file_2:
        for line in file_2:
            file_2_array.append(line.partition(" ")[2].strip())

    with open(stdout_path3, 'r') as file_3:
        for line in file_3:
            file_3_array.append(line.partition(" ")[2].strip())

    with open(output_file, 'w') as output:
        output.write('\\begin {table}')
        output.write('\\caption{CK Simulated Results}')
        output.write('\\begin{tabular}{ |p{2cm}|p{2cm}|p{2cm}|p{2cm}|  }\n')
        output.write('\\hline\n')
        output.write(' 2019 Results &  Home-Field Advantage 0 & Home-Field Advantage 4& Home-Field Advantage 8\\\\\n')
        output.write('\\hline\n')
        for x in range(num_displayed_teams):
            output.write('{} & {} & {} & {}\\\\\n'.format(correct[x], file_1_array[x], file_2_array[x], file_3_array[x] ))
            output.write('\\hline\n')
        output.write('\\end{tabular}\n')
        output.write('\\end{table}\n')

    #compile files
    os.system("pdflatex SOTF")
    os.system("bibtex SOTF")
    os.system("pdflatex SOTF")
    os.system("pdflatex SOTF")

    return {'return':0}
##############################################################################
# open notebook from experiment run

def open_notebook(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """
    r=ck.access({'action':'run', 'module_uoa':'jnotebook', 'data_uoa':'notebook'})
    if r['return']>0: return r # use standard error handling in the CK
##############################################################################

def push(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    r=ck.access({'action':'list_files','repo_uoa':'march-madness',
                 'module_uoa':'mm-simulator', 'data_uoa':'results',
                 'skip_sort':'yes'})
    if r['return']>0: return r # use standard error handling in the CK
    file_info = r['list']
    num_files = r['number']
    res = []
    selection = None
    if num_files == 0:
    	ck.out('No results to push')
    elif num_files == 1:
        for item in file_info:
            selection = item
            print(str(count) + ") " + item)
    else:
        ck.out('')
        ck.out('There is more than one result')
        ck.out('')
        count = 0;
        for item in file_info:
        	print(str(count) + ") " + item)
        	count += 1
        	res.append(item)

    y='\nSelect UOA (or press Enter for 0)'

    rx=ck.inp({'text':y})
    x=rx['string'].strip()
    if x=='': x='0'

    selection = res[int(x)]
    print("\nSelected " + selection)

    r=ck.access({'action':'find','module_uoa':'mm-simulator', 'data_uoa':'results'})
    path = r['path']

    file1 = open(path + "/" + selection, 'r') 

    for line in reversed(list(file1)):
    	if "Standard Error" in line:
            se = line.split()[2]

    

    return {'return':0}
