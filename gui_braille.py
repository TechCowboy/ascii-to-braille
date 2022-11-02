'''
 Created by Norman Davie
'''
import PySimpleGUI as sg
from ascii_to_braille import ndbraille
import threading
import time

class gui_braille(ndbraille):
    
    def __init__(self, grade=1, lang="english", theme="light blue"):
        super().__init__(grade, lang)
        
        self.theme = theme
        self.window = None
        
        self.set_language(lang)
        self.set_grade(grade)
        
        self.window_started = False
        
        self._old_text = ""
        
        x = threading.Thread(target=self.event_thread)

        x.start()

        
        while not self.window_started:
            time.sleep(0.1)

    def event_thread(self):
        
        print("Event Thread")
        self.theme = sg.theme(self.theme)
        text_font = (sg.DEFAULT_FONT, 15)
        
        layout = [ [sg.Multiline(key="text", size=(160,40), font=text_font) ] ]
        
        self._old_text = ""
        
        self.window = sg.Window('Braille GUI', layout,finalize=True, resizable=True)
        
        self.window_started = True
        while True:
            event, values = self.window.read()
            print(f"event: {event}\nvalues: {values}")
            
            if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
                break        

            if event == "text":
                self._old_text = values["text"]
                print(f"_old_text : {self._old_text}")
        
    def english(self, grade):
    
        super().english(grade)
        braille_base = 0x2800
        braille_dots = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20]
        self._braille_basic_unicode = { }
        for key in self._braille_basic:
            dots_list = self._braille_basic[key]
            c = ""
            
            for dots in dots_list:
                value = braille_base
                for i in range(6):
                    value += braille_dots[i]*dots[i]
                c += chr(value)
                
            self._braille_basic_unicode[key] = c
              
        
        if (grade == 1):
            self.__braille_endings    = { }
            self.__braille_whole_word = { }
            self.__braille_pattern    = { }
                    

        if (grade == 2):
            self._braille_endings_unicode = { }
            for key in self._braille_endings:
                dots_list = self._braille_endings[key]
                c = ""
                
                for dots in dots_list:
                    value = braille_base
                    for i in range(6):
                        value += braille_dots[i]*dots[i]
                    c += chr(value)
                    
                self._braille_endings_unicode[key] = c
 
 
            self._braille_whole_word_unicode = { }
            for key in self._braille_whole_word:
                dots_list = self._braille_whole_word[key]
                c = ""
                
                for dots in dots_list:
                    value = braille_base
                    for i in range(6):
                        value += braille_dots[i]*dots[i]
                    c += chr(value)
                    
                self._braille_whole_word_unicode[key] = c


            self._braille_pattern_unicode = { }
            for key in self._braille_pattern:
                dots_list = self._braille_pattern[key]
                c = ""
                
                for dots in dots_list:
                    value = braille_base
                    for i in range(6):
                        value += braille_dots[i]*dots[i]
                    c += chr(value)
                    
                self._braille_pattern_unicode[key] = c

    def set_language(self, lang):
        '''
            Set language for the braille to be translated to.
            If the language doesn't exist, no change occurs
            to the current settings and this function returns False
        '''
        super().set_language(lang)
        
        if lang.lower() == "english":
            self.english(self._grade)
            self.__language = lang.lower()
            return True
        else:
            return False


        
    def set_grade(self, grade):
        '''
            Set the grade for the braille; does not change the language
            If the grade for the currently selected language doesn't
            exist, no change occurs to the crrent settings and this
            function returns False
        '''
        super().set_grade(grade)
        
  
    def print(self, words):
        
        print(f"old_text: '{self._old_text}'")        
        self.window["text"].update(self._old_text + "\n" + words)
        
    def word_to_braille_string(self, s):
        ends_with = ''
        output = ''
        
        complete_word = False
        for key in self._braille_whole_word:
            if s == key:
                output = self._braille_whole_word_unicode[key]
                complete_word = True
                break
            
        if not complete_word:
            # check for special ending
            for key in self._braille_endings:
                if s.endswith(key):
                    ends_with = self._braille_endings_unicode[key]
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
                        output += self._braille_pattern_unicode[pattern]
                        i += len(pattern)
                    else:
                        output += self._braille_basic_unicode[substring[0]]
                        i += 1
            
        output = self.append(output, ends_with)
        return output

    
if __name__ == "__main__":            
    braille = gui_braille()

    braille.show_dots()
    braille.show_ascii()

    #braille.get_info()
    
    string = "Experience Hong Kong, with it's wonderful tradition of Happiness, enchantment and hospitality."
    
    braille.print(string)
   
    braille.set_grade(2)
    braille.get_info()
    braille.print(string)
    #print()
    
    w = braille.word_to_braille_string(string)        
    braille.print(w)
    #help(ndbraille)
    
    #time.sleep(5)
    #braille.print(help(ndbraille))
    time.sleep(30)
    