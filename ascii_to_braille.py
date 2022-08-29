
global braille

    # 1   4
    # 2   5
    # 3   6
    
braille = {
        'a': [[1,0,0,0,0,0]],
        'b': [[1,1,0,0,0,0]],
        'c': [(1,0,0,1,0,0)],
        'd': [(1,0,0,1,1,0)],
        'e': [(1,0,0,0,1,0)],
        'f': [(1,1,0,1,0,0)],
        'g': [(1,1,0,1,1,0)],
        'h': [(1,1,0,0,1,0)],
        'i': [(0,1,0,1,0,0)],
        'j': [(0,1,0,1,1,0)],
        'k': [(1,0,1,0,0,0)],
        'l': [(1,1,1,0,0,0)],
        'm': [(1,0,1,1,0,0)],
        'n': [(1,0,1,1,1,0)],
        'o': [(1,0,1,0,1,0)],
        'p': [(1,1,1,1,0,0)],
        'q': [(1,1,1,1,1,0)],
        'r': [(1,1,1,0,1,0)],
        's': [(0,1,1,1,0,0)],
        't': [(0,1,1,1,1,0)],
        'u': [(1,0,1,0,0,1)],
        'v': [(1,1,1,0,0,1)],
        'w': [(0,1,0,1,1,1)],
        'x': [(1,0,1,1,0,1)],
        'y': [(1,0,1,1,1,1)],
        'z': [(1,0,1,0,1,1)],
        '1': [(0,0,1,1,1,1,),(1,0,0,0,0,0)],
        '2': [(0,0,1,1,1,1,),(1,1,0,0,0,0)],
        '3': [(0,0,1,1,1,1,),(1,0,0,1,0,0)],
        '4': [(0,0,1,1,1,1,),(1,0,0,1,1,0)],
        '5': [(0,0,1,1,1,1,),(1,0,0,0,1,0)],
        '6': [(0,0,1,1,1,1,),(1,1,0,0,1,0)],
        '7': [(0,0,1,1,1,1,),(1,1,0,1,1,0)],
        '8': [(0,0,1,1,1,1,),(1,1,0,0,1,0)],
        '9': [(0,0,1,1,1,1,),(0,1,0,1,0,0)],
        '0': [(0,0,1,1,1,1,),(0,1,0,1,1,0)]
    }
    
    
def display_braille(symbol):
    
    print(symbol)

    
    matrix = [[0,3], [1,4], [2,5]]
    
    
    for l in range(len(symbol)):
        s = symbol[l]
        print("'", end='')
        for m in range(len(matrix[l])):
            columns = matrix[m]
            
            for c in columns:
                if (s[c]):
                    print("*", end='')
                else:
                    print(" ", end='')
                    
        print()
                    
            
            
            
            

    

display_braille(braille['0'])

    