
global braille

    # 1   4
    # 2   5
    # 3   6
    
braille = {
        'a': [[1,0,0,0,0,0]],
        'b': [[1,1,0,0,0,0]],
        'c': [[1,0,0,1,0,0]],
        'd': [[1,0,0,1,1,0]],
        'e': [[1,0,0,0,1,0]],
        'f': [[1,1,0,1,0,0]],
        'g': [[1,1,0,1,1,0]],
        'h': [[1,1,0,0,1,0]],
        'i': [[0,1,0,1,0,0]],
        'j': [[0,1,0,1,1,0]],
        'k': [[1,0,1,0,0,0]],
        'l': [[1,1,1,0,0,0]],
        'm': [[1,0,1,1,0,0]],
        'n': [[1,0,1,1,1,0]],
        'o': [[1,0,1,0,1,0]],
        'p': [[1,1,1,1,0,0]],
        'q': [[1,1,1,1,1,0]],
        'r': [[1,1,1,0,1,0]],
        's': [[0,1,1,1,0,0]],
        't': [[0,1,1,1,1,0]],
        'u': [[1,0,1,0,0,1]],
        'v': [[1,1,1,0,0,1]],
        'w': [[0,1,0,1,1,1]],
        'x': [[1,0,1,1,0,1]],
        'y': [[1,0,1,1,1,1]],
        'z': [[1,0,1,0,1,1]],
        'A': [[0,0,0,0,0,1],[1,0,0,0,0,0]],
        'B': [[0,0,0,0,0,1],[1,1,0,0,0,0]],
        'C': [[0,0,0,0,0,1],[1,0,0,1,0,0]],
        'D': [[0,0,0,0,0,1],[1,0,0,1,1,0]],
        'E': [[0,0,0,0,0,1],[1,0,0,0,1,0]],
        'F': [[0,0,0,0,0,1],[1,1,0,1,0,0]],
        'G': [[0,0,0,0,0,1],[1,1,0,1,1,0]],
        'H': [[0,0,0,0,0,1],[1,1,0,0,1,0]],
        'I': [[0,0,0,0,0,1],[0,1,0,1,0,0]],
        'J': [[0,0,0,0,0,1],[0,1,0,1,1,0]],
        'K': [[0,0,0,0,0,1],[1,0,1,0,0,0]],
        'L': [[0,0,0,0,0,1],[1,1,1,0,0,0]],
        'M': [[0,0,0,0,0,1],[1,0,1,1,0,0]],
        'N': [[0,0,0,0,0,1],[1,0,1,1,1,0]],
        'O': [[0,0,0,0,0,1],[1,0,1,0,1,0]],
        'P': [[0,0,0,0,0,1],[1,1,1,1,0,0]],
        'Q': [[0,0,0,0,0,1],[1,1,1,1,1,0]],
        'R': [[0,0,0,0,0,1],[1,1,1,0,1,0]],
        'S': [[0,0,0,0,0,1],[0,1,1,1,0,0]],
        'T': [[0,0,0,0,0,1],[0,1,1,1,1,0]],
        'U': [[0,0,0,0,0,1],[1,0,1,0,0,1]],
        'V': [[0,0,0,0,0,1],[1,1,1,0,0,1]],
        'W': [[0,0,0,0,0,1],[0,1,0,1,1,1]],
        'X': [[0,0,0,0,0,1],[1,0,1,1,0,1]],
        'Y': [[0,0,0,0,0,1],[1,0,1,1,1,1]],
        'Z': [[0,0,0,0,0,1],[1,0,1,0,1,1]],
        '1': [[0,0,1,1,1,1],[1,0,0,0,0,0]],
        '2': [[0,0,1,1,1,1],[1,1,0,0,0,0]],
        '3': [[0,0,1,1,1,1],[1,0,0,1,0,0]],
        '4': [[0,0,1,1,1,1],[1,0,0,1,1,0]],
        '5': [[0,0,1,1,1,1],[1,0,0,0,1,0]],
        '6': [[0,0,1,1,1,1],[1,1,0,0,1,0]],
        '7': [[0,0,1,1,1,1],[1,1,0,1,1,0]],
        '8': [[0,0,1,1,1,1],[1,1,0,0,1,0]],
        '9': [[0,0,1,1,1,1],[0,1,0,1,0,0]],
        '0': [[0,0,1,1,1,1],[0,1,0,1,1,0]],
        '?': [[0,1,1,0,0,1]],
        '!': [[0,1,1,0,1,0]],
        ',': [[0,1,0,0,0,0]],
        '-': [[0,0,1,0,0,1]],
        '@': [[0,0,1,1,1,0]],
        '+': [[0,1,1,0,1,0]],
        '=': [[0,1,1,0,1,1]],
        '.': [[0,0,0,0,0,1]],
        '(': [[0,1,1,0,0,1]],
        ')': [[0,0,1,0,1,1]],
        '*': [[0,0,1,0,1,0]],
        ':': [[0,1,0,0,1,0]],
        '/': [[0,0,1,1,0,0]],
        ' ': [[0,0,0,0,0,0]],
        ';': [[0,1,1,0,0,0]],
        '"(': [[0,1,1,0,0,1]],
        '")': [[0,0,1,0,1,1]],
        "'(": [[0,0,0,0,0,1], [0,1,1,0,0,1]],
        "')": [[0,0,1,0,1,1], [0,0,1,0,0,0]],
        '#':  [[0,0,1,1,1,1]]
    }
    
    
def symbol_as_string(symbol):
    
    output = ''
    matrix = [[0,3], [1,4], [2,5]]
    
    total_columns = len(matrix[0])

    for row in range(len(matrix)): # y
        for letter in range(len(symbol)):
            for column in range(total_columns): #x
                x = matrix[row][column]
                value = symbol[letter][x]
                if value != 0:
                    output += "*"
                else:
                    output += " "
                    
            output += " "
        output += "\n"
    return output
        
def display_symbol(s):
    print(symbol_as_string(s))



def append_braille_strings(s, t):
    
    s = s.split('\n')
    
    t = t.split('\n')
    
    output_list = [ "", "", ""]
    for row in range(3):
        if row < len(s):
            output_list[row] = s[row]
            
    for row in range(3):
        if row < len(t):
            output_list[row] += t[row]
            
    output = ""        
    for row in range(3):
        output += output_list[row] + '\n'
    
    
    return output


def display_string_as_braille(s, display_ascii=False):
    bstr = ""
    open_double_quote = True
    open_single_quote = True
    
    for letter in s:
        if letter == '"':
            if open_double_quote:
                letter = '"('
            else:
                letter = '")'
            
            open_double_quote = not open_double_quote

        if letter == "'":
            if open_single_quote:
                letter = "'("
            else:
                letter = "')"
            
            open_single_quote = not open_single_quote
            
        bstr = append_braille_strings(bstr, symbol_as_string(braille[letter]))
        
    print(bstr)
    
    if display_ascii:
        for c in s:
            c1 = c
            if c == '"':
                if open_double_quote:
                    c = '"('
                else:
                    c = '")'
                
                open_double_quote = not open_double_quote

            if c == "'":
                if open_single_quote:
                    c = "'("
                else:
                    c = "')"
            
            open_single_quote = not open_single_quote
            
            
            print(c1, end="")
            if len(braille[c])>1:
                print(" ", end='')
                
            print(" " * (len(braille[c]) * 2), end='')
        print()
        
            
display_string_as_braille("This is a 'test' of braille", True)            
            
display_string_as_braille("1234567", True)            

display_string_as_braille("######", True)    
    