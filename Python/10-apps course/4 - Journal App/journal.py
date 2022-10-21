
def load(name):
    #todo: populate from file if it exists.
    return([])
    pass

def save(name,journal_data):
    base_dir = "~/myworkingfolder"
    rel_dir =  "data/temp.txt"
    filename = './journals/' + name + '.jrl'
    file_output = open(filename,'w')
    return(file_output)

def add_entry(text, journal_data):
    return None