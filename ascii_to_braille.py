
class ndbraille:
    

    def __init__(self, grade=1, lang="english"):
        '''
            Prepare translating ascii string to appropriate language and grade
            default is English and grade 1
            Dots are not shown by default
            Braille strings are not reversed by default
        '''
        self.__dots = False
        self.__reverse = False
        self.__show_ascii = False

        if lang.lower() == "english":
            self.english(grade)
            
    def english(self, grade):
        '''
            Use english braille
            Grade is passed
            the "global" braille will be set
            to the appropriate braille grade
        '''
        
        if (grade == 1):
            self.__braille = {
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


    
    def symbol_as_string(self, symbol):
        '''
            Takes a braille symbol and
            converts it to an ascii representation.
            If self.dots is set, then a period will
            be shown instead of a space.
            Space character is not converted to dots
        '''
        
        output = ''
        matrix = [[0,3], [1,4], [2,5]]
        
        total_columns = len(matrix[0])

        for row in range(len(matrix)): # y
            for letter in range(len(symbol)):
                for column in range(total_columns): #x
                    x = matrix[row][column]
                    value = symbol[letter][x]

                    if [symbol[letter]] == self.__braille[' ']:
                        # special case -- don't convert spaces between characters to dots
                        output += " "
                    else:
                        if value != 0:
                            output += "*"
                        else:
                            if self.__dots:
                                output += '.'
                            else:
                                output += ' '
                        
                output += " "
            output += "\n"
        return output
        


    def append(self, s, t):
        '''
            Takes two ascii braille strings and appends them
            returning the result
        '''
    
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


    def ascii_to_braille_string(self, s):
        '''
            Takes an ascii string and converts it to braille.
            display__ascii if set to True will display the ascii
            character above the braille symbol
            If the "global" reverse is set to true, the
            string returned will be reversed
        '''
        
        bstr = ""
        ascii = ""
        
        open_double_quote = True
        open_single_quote = True
        
        if self.__show_ascii:
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
                
                
                ascii += c1
                if len(self.__braille[c])>1:
                    ascii += " "
                    
                ascii += " " * (len(self.__braille[c]) * 2)
            ascii += "\n"
            
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
                
            bstr = self.append(bstr, self.symbol_as_string(self.__braille[letter]))


        if self.__show_ascii:
            bstr = ascii + bstr
        
        if self.__reverse:
            bstr = self.reverse_braille(bstr)
        return bstr
    
    def reverse_braille(self, s):
        '''
            Takes a braille string and returns the reverse of it
        '''
        s = s.split('\n')
        
        r = ""
        for line in range(len(s)-1):
            s1 = s[line]
            r += s1[::-1] + "\n"
    
        return r
        
    def print(self, s):
        '''
            print braille to the console
        '''
        bstr = self.ascii_to_braille_string(s)
        print(bstr)
        
    def show_ascii(self, show=True):
        '''
            show the ascii string above the braille
        '''
        self.__show_ascii = show

    def hide_ascii(self, show=False):
        '''
            do not show the ascii string
        '''
        self.__show_ascii = show

    def reverse(self, set_reverse=True):
        '''
            reverse the braille string so it
            could be used in an embosser
        '''
        self.__reverse = set_reverse
            
    def normal(self, set_reverse=False):
        '''
            do not reverse the braille string
        '''
        self.__reverse = set_reverse
            
    def show_dots(self, dots=True):
        '''
            show dots on braille characters but
            not on spaces
        '''
        self.__dots = dots

    def hide_dots(self, dots=False):
        '''
            braille characters appear 'normal'
        '''
        self.__dots = dots

if __name__ == "__main__":            
    braille = ndbraille()

    braille.show_dots()
    braille.show_ascii()

    braille.print("This is a 'test' of braille")
    braille.reverse()
    braille.print("This is a 'test' of braille")    
            
 
    
    