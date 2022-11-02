#!/usr/bin/env python3
# Nov 2, 2022 16:00
# ascii_to_braille.py

# Copyright (c) Norman Davie

class ndbraille:
    '''
        ndbraille = Braille creator by Norman Davie
        This class translates ascii strings into their
        braille equivalent
    '''

    def __init__(self, grade=1, lang="english"):
        '''
            Prepare translating ascii string to appropriate language and grade
            default is English and grade 1
            Dots are not shown by default
            Braille strings are not reversed by default
            Currently supported Languages and Grades
                English - Grades: 1
        '''
        self._dots = False
        self._reverse = False
        self._show_ascii = False
        self._grade = 1
        self._language = "english"
        
        self.set_language(lang)
        self.set_grade(grade)
    
    
    def set_language(self, lang):
        '''
            Set language for the braille to be translated to.
            If the language doesn't exist, no change occurs
            to the current settings and this function returns False
        '''
        if lang.lower() == "english":
            self.english(self._grade)
            self._language = lang.lower()
            return True
        else:
            return False
        
    def get_language(self):
        '''
            Returns the currently selected language
        '''
        return self._language
    
    def set_grade(self, grade):
        '''
            Set the grade for the braille; does not change the language
            If the grade for the currently selected language doesn't
            exist, no change occurs to the crrent settings and this
            function returns False
        '''
        if grade in [1,2]:
            self._grade = grade
            self.set_language(self._language)
            return True
        else:
            return False
    
    def get_grade(self):
        '''
            Returns the currently selected grade
        '''
        return self._grade

    def get_info(self):
        '''
            Displays the current language and grade
            and various flags
        '''
        print(f"Language:        {self._language}")
        print(f"Grade:           {self._grade}")
        print(f"Show Dots:       {self._dots}")
        print(f"Reverse Braille: {self._reverse}")
        print(f"Show ASCII:      {self._show_ascii}")
        
        
    def english(self, grade):
        '''
            Use english braille
            Grade is passed
            the "global" braille will be set
            to the appropriate braille grade
        '''
        
        self._braille_basic = {
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
            "'":  [[0,0,1,0,0,0]],
            '#':  [[0,0,1,1,1,1]]
        }
        
        if (grade == 1):
            self._braille_endings    = { }
            self._braille_whole_word = { }
            self._braille_pattern    = { }
                    

        if (grade == 2):
            self._braille_endings = {
                            # only at end of word
                'ence': [[0,0,0,0,1,1],[1,0,0,0,1,0]],
                'ong':  [[0,0,0,0,1,1],[1,1,0,1,1,0]],
                'ful':  [[0,0,0,0,1,1],[1,1,1,0,0,0]],
                'tion': [[0,0,0,0,1,1],[1,0,1,1,1,0]],
                'ness': [[0,0,0,0,1,1],[0,1,1,1,0,0]],
                'ment': [[0,0,0,0,1,1],[0,1,1,1,1,0]],
                'ity':  [[0,0,0,0,1,1],[1,0,1,1,1,1]],
                'ation': [[0,0,0,0,0,1],[0,0,0,0,0,0]],
                'ally': [[0,0,0,0,0,1],[1,0,1,1,1,1]],
                'ound': [[0,0,0,1,0,1],[1,0,0,1,1,0]],
                'ance': [[0,0,0,1,0,1],[1,0,0,0,1,0]],
                'sion': [[0,0,0,1,0,1],[1,0,1,1,1,0]],
                'less': [[0,0,0,1,0,1],[0,1,1,1,0,0]],
                'ount': [[0,0,0,1,0,1],[0,1,1,1,1,0]]
                }

            self._braille_whole_word = {
                    # whole word
                    'but':    [[1,1,0,0,0,0]],
                    'can':    [[1,0,0,1,0,0]],
                    'do':     [[1,0,0,1,1,0]],
                    'every':  [[1,0,0,0,1,0]],
                    'from':   [[1,1,0,1,0,0]],
                    'have':   [[1,1,0,1,1,0]],
                    'just':   [[1,1,0,0,1,0]],
                    'knowledge': [[0,0,0,1,0,1]],
                    'like':   [[1,1,1,0,0,0]],
                    'more':   [[1,0,1,1,0,0]],
                    'not':    [[1,0,1,1,1,0]],
                    'people': [[1,1,1,1,0,0]],
                    'quite':  [[1,1,1,1,1,0]],
                    'rather': [[1,1,1,0,1,0]],
                    'so':     [[0,1,1,1,0,0]],
                    'that':   [[0,1,1,1,1,0]],
                    'us':     [[1,0,1,1,0,0]],
                    'very':   [[1,1,1,0,0,1]],
                    'will':   [[0,1,0,1,1,1]],
                    'it':     [[1,0,1,1,0,1]],
                    'you':    [[1,0,1,1,1,1]],
                    'as':     [[1,0,1,0,1,1]],
                    'and':    [[1,1,1,1,0,1]],
                    'for':    [[1,1,1,1,1,1]],
                    'of':     [[1,1,1,0,1,1]],
                    'the':    [[0,1,1,1,0,1]],
                    'with':   [[0,1,1,1,1,1]],
                    'child':  [[1,0,0,0,0,1]],
                    'ch':     [[1,0,0,0,0,1]],
                    'gh':     [[1,1,0,0,0,1]],
                    'shall':  [[1,0,0,1,0,1]],
                    'sh':     [[1,0,0,1,0,1]],
                    'this':   [[1,0,0,1,1,1]],
                    'which':  [[1,0,0,0,1,1]]
                }
                
            self._braille_pattern = {
                    'wh':     [[1,0,0,0,1,1]],
                    'ed':     [[1,1,0,1,0,1]],
                    'er':     [[1,1,0,1,1,1]],
                    'out':    [[1,1,0,0,1,1]],
                    'ou':     [[1,1,0,0,1,1]],
                    'ow':     [[0,1,0,1,0,1]],
                    'bb':     [[0,1,1,0,0,0]],
                    'cc':     [[0,1,0,1,0,0]],
                    'dd':     [[0,1,0,0,1,1]],
                    'en':     [[0,1,0,0,0,1]],
                    'were':   [[0,1,1,0,1,1]],
                    'gg':     [[0,1,1,0,1,1]],
                    'in':     [[0,0,1,0,1,0]],
                    'st':     [[0,0,1,1,0,0]],
                    'ing':    [[0,0,1,1,0,1]],
                    'arn':    [[0,0,1,1,1,0]]
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

                    if [symbol[letter]] == self._braille_basic[' ']:
                        # special case -- don't convert spaces between characters to dots
                        output += " "
                    else:
                        if value != 0:
                            output += "*"
                        else:
                            if self._dots:
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

    def word_to_braille_string(self, s):
        ends_with = ''
        output = ''
        
        complete_word = False
        for key in self._braille_whole_word:
            if s == key:
                output = self.symbol_as_string(self._braille_whole_word[key])
                complete_word = True
                break
            
        if not complete_word:
            # check for special ending
            for key in self._braille_endings:
                if s.endswith(key):
                    ends_with = self.symbol_as_string(self._braille_endings[key])
                    s = s[:-len(key)]
                    break
            
            # check for pattern
            
            pattern_found = True
            while pattern_found:
                i = 0
                while i < len(s):
                    pattern_found = False
                    pattern = ''
                    substring = s[i:]
                    for key in self._braille_pattern:
                        if substring.startswith(key):
                            pattern = key
                            pattern_found = True
                            break
                        
                    if pattern_found:
                        output = self.append(output, self.symbol_as_string(self._braille_pattern[pattern]))
                        i += len(pattern)
                    else:
                        output = self.append(output, self.symbol_as_string(self._braille_basic[substring[0]]))
                        i += 1
            
        output = self.append(output, ends_with)
        return output

    def ascii_to_braille_string(self, s):
        '''
            Takes an ascii string and converts it to braille.
            display_ascii if set to True will display the ascii
            character above the braille symbol
            If the "global" reverse is set to true, the
            string returned will be reversed
        '''
        
        bstr = ""
        ascii = ""
        
        open_double_quote = True
        open_single_quote = True
        
        if self._show_ascii:
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
                if len(self._braille_basic[c])>1:
                    ascii += " "
                    
                ascii += " " * (len(self._braille_basic[c]) * 2)
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
                
            bstr = self.append(bstr, self.symbol_as_string(self._braille_basic[letter]))


        if self._show_ascii:
            bstr = ascii + bstr
        
        if self._reverse:
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
        self._show_ascii = show

    def hide_ascii(self, show=False):
        '''
            do not show the ascii string
        '''
        self._show_ascii = show

    def reverse(self, set_reverse=True):
        '''
            reverse the braille string so it
            could be used in an embosser
        '''
        self._reverse = set_reverse
            
    def normal(self, set_reverse=False):
        '''
            do not reverse the braille string
        '''
        self._reverse = set_reverse
            
    def show_dots(self, dots=True):
        '''
            show dots on braille characters but
            not on spaces
        '''
        self._dots = dots

    def hide_dots(self, dots=False):
        '''
            braille characters appear 'normal'
        '''
        self._dots = dots

if __name__ == "__main__":            
    braille = ndbraille()

    braille.show_dots()
    braille.show_ascii()

    #braille.get_info()
    
    string = "Experience Hong Kong, with it's wonderful tradition of Happiness, enchantment and hospitality."
    
    #braille.print(string)
    #print()
    
    braille.set_grade(2)
    braille.get_info()
    #braille.print(string)
    #print()
    
    w = braille.word_to_braille_string("Experience")        
    print(w)
    #help(ndbraille) 
    