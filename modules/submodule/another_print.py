from modules.useless_print import useless_print

def another_print(content):
    '''Prints the argument recieved'''
    print(content)
    useless_print(content)

if __name__ == "__main__":
    import sys
    another_print(sys.argv[1])