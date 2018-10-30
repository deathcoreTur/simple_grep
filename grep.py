import re


# Check on exist grep and .txt in line
def validate(args):
    command_line = False
    # It should be 'grep'
    first = args[0]
    # It should be filename with .txt extension
    last = args[-1]

    if first != 'grep':
        msg = "Please, input line with 'grep':\n"
    elif not last.endswith('.txt'):
        msg = "Not find txt file:\n"
    else:
        return True, args

    while not command_line:
        command_line = input(msg)
    args = command_line.split()
    return False, args


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


# For big file where strings are very long
def read_in_chunks(file_object, chunk_size=1024):
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data


if __name__ == '__main__':
    command_line = False
    while not command_line:
        command_line = input("Hello, it's grep. Input please your request with 'grep' and another requirements:\n")

    args = command_line.split()

    right_command, args = validate(args)

    while not right_command:
        right_command, args = validate(args)

    # Deleted 'grep' from list and get filename. As result, args list consists only necessary parameters
    del args[0]
    filename = args.pop()
    file = open(filename)

    if args:
        # I don't use yield for reading, because the file is line-based,
        # the file object is already a lazy generator of lines:
        find(file, args)
    else:
        print('You not input mask, restart program with requirements ')





