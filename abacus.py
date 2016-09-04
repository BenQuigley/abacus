from __future__ import print_function

class abacus:
    # Reference: https://www.youtube.com/watch?v=CvsnftXXKdw
    def __init__(self):
        self.value    = 0.0
        self.places   = 6
        self.decimals = 2
        self.length   = self.places + self.decimals
    
    def display(self):
        self.string = str(int(self.value*100)).zfill(9)
        self.board = ['','','','','','','','','','']

        print('Displaying abacus showing value:', self.value)
        place = 0
        stop = len(self.string) # min of 9 because of zfill
        while place <  stop:
            digitvalue = int(self.string[place])
            spacing = False
            if len(self.board[0]) % 2 != 0:
                spacing = True
            for i, row in enumerate(self.board):
                if i in [0, 3, 9]:
                    self.board[i] += '='
                elif stop - place == 2 and spacing:
                    self.board[i] += '|'
                elif spacing:
                    self.board[i] += ' '
                else:
                    heavennum = int(digitvalue/5)
                    earthnum = digitvalue % 5
                    # "heaven"
                    if i <= 2:
                        if heavennum == i-1:
                            self.board[i] += '-'
                        else:
                            self.board[i] += ' '
                    # "earth"
                    else:
                        if earthnum == i - 4:
                            self.board[i] += ' '
                        else:
                            self.board[i] += '-'
            if not spacing:
                place += 1

        print('\n'.join(self.board),'\n')

def main():
    test = abacus()
    prompt = 'Enter a number to display on the pretty abacus here:\n>'
    while True:
        try:
            test.value += float(input(prompt))
            test.display()
        except ValueError:
            print('That\'s not a number.')
        prompt = 'Great job! Now enter a number to add or subtract:\n>'

if __name__ == '__main__':
    main()
