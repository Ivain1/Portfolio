import datetime
import journal as j
import UI as ui
def main():
    ui.print_header()
    run_event_loop()



def run_event_loop():
    print('What do you want to do with your Journal?')
    cmd = None
    journal_name = 'Default'
    journal_data = j.load(journal_name) #[] #list()
    while cmd != 'x':
        try:
            cmd = input('[L]ist entries, [A]dd entry, E[x]it: ')
            cmd = cmd.lower().strip()
            if cmd == 'l':
                list_entries(journal_data)

            elif cmd == 'a':
                add_entry(journal_data)

            elif cmd != 'x':
                print('Incorrect input')

            j.save(journal_name)
        except ValueError as error:
            print('Incorrect input:', error)

    print('Done, goodbye.')


def list_entries(data,display_type=0):
    print('Listing...')
    #Display type 0 lists only the titles, sorted alphabetically

    #Display type 1 lists the entries

    #Display type 2 lists the entries in their entirety
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        entry = decompile_content(entry)
        print("Your Journal Entries")
        print("*[{}] {}".format(idx+1,entry))
    #print(data)


def add_entry(data):
    title = input('Give a title to your entry, press <enter> to proceed:... ')
    #print(str(title))
    text = input('Type your entry, <enter> to proceed:... ')
    time = datetime.datetime.today()
    date = time.strftime("%A %d %B %Y")
    clocktime = time.strftime("%H:%M")
    timestamp = 'posted on {0} At {1}'.format(date, clocktime)
    #print(timestamp)
    content = compile_content(title,timestamp,text)
    #journal_entry = decompile_content(content)
    print('Adding...')
    #print(content)
    #print(journal_entry)
    j.add_entry(text,data)
    #data.append(content)
    print('Added entry to journal.')

def view_entry(data,id):
    id = int(id)
    entry = data[id]

def compile_content(title,timestamp,text):
    entry = '{0} \n {1} \n {2}'.format(title, timestamp, text)
    content = [title,timestamp,text,entry]
    return(content)

def decompile_content(content,element=3):
    '''title = content[0]
    timestamp = content[1]
    text = content[2]
    entry = content[3]
    #choose which element to return. Defaults to 3 for the journal entry itself.
    if element == 0:
        return(title)
    elif element == 1:
        return(timestamp)
    elif element == 2:
        return(text)
    elif element == 3:
        return(entry)'''
    return(content)

    #return('{0} - -- --- ----- ------- ----- --- -- -\n{1}\n {2}'.format(title, timestamp, text))




main()