

def main():
    print_header()
    run_event_loop()


def print_header():
    print('-------------------')
    print('    Journal App')
    print('-------------------')

def run_event_loop():
    print('What do you want to do with your journal?')
    cmd = None
    journal_data=[] #empty list
    while cmd != x:
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it: ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_journal_entries()
        elif cmd == 'a':
            add_entry()
        elif cmd != 'x':
            print('{0} is not a valid input'.format(cmd))


def add_entry():
    pass