#copied or original with 2 features num of lines and language

def java_code(lines):
    if lines > 5:
        print ('copied')
    else:
        print( 'not copied')
def python_code(lines):
    if lines >= 1:
        print( 'copied' )
    else:
        print( 'not copied' )

if __name__ == '__main__':
    lang = input("Enter the languane and number of lines: ")
    lines = int(input())
    if lang == 'python':
        python_code(lines)
    elif lang == 'java':
        java_code(lines)
    else:
        print("Invalid Language")
    
    
