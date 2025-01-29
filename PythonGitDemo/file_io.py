FILE_NAME="input.txt"

def read_greeting():
    greeting_file=open(FILE_NAME,'r')
    content = greeting_file.read()
    return content

if __name__ == '__main__' :
    print(read_greeting())
