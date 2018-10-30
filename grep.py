import re


# Check on exist grep and .txt in line
def check(args):
    if args[0] != 'grep' and not args[-1].endswith('.txt'):
        command_line = input("Please, input line with 'grep' and point out filename.text:\n")
        args = command_line.split()
        return check(args)
    elif args[0] != 'grep' and args[-1].endswith('.txt'):
        command_line = input("Please, use 'grep' word:\n")
        args = command_line.split()
        return check(args)
    elif not args[-1].endswith('.txt'):
        command_line = input("Not find txt file:\n")
        args = command_line.split()
        return check(args)
    else:
        return args


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
    args = check(command_line.split())

    # Deleted 'grep' from list and get filename. As result, args list consists only necessary parameters
    del args[0]
    filename = args.pop()
    file = open(filename)

    if args:
        find(file, args)
    else:
        print('You not input mask, restart program with requirements ')





