import re


# Check on exist grep and .txt in line
def check():
    global args
    # It should be 'grep'
    first = args[0]
    # It should be filename with .txt extension
    last = args[-1]

    if first != 'grep':
        msg = "Please, input line with 'grep':\n"
    elif not last.endswith('.txt'):
        msg = "Not find txt file:\n"
    else:
        return True

    command_line = input(msg)
    while not command_line:
        command_line = input(msg)
    args = command_line.split()
    return False


def find(file, args):
    # Check length list
    count_args = len(args)
    if count_args == 2 and args[0] == '-v':
        for line in file:
            if args[1] in line:
                continue
            print(line.rstrip())
    elif count_args:
        search_regex = r"{0}".format(args[0].strip('\"'))
        for line in file:
            if re.search(search_regex, line):
                print(line.rstrip())


if __name__ == '__main__':
    command_line = input("Hello, it's grep. Input please your request with 'grep' and another requirements:\n")
    while not command_line:
        command_line = input("Hello, it's grep. Input please your request with 'grep' and another requirements:\n")

    args = command_line.split()

    right_command = check()

    while not right_command:
        right_command = check()

    # Deleted 'grep' from list and get filename. As result, args list consists only necessary parameters
    del args[0]
    filename = args.pop()
    file = open(filename)

    if args:
        find(file, args)
    else:
        print('You not input mask, restart program with requirements ')





