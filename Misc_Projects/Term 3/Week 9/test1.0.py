

class CommentsSM():
    start_state = 2
    """
    3 states for get_next_values:
    1 - take in: Collect the string
    2 - Don't: Return None
    3 - siols: that fuckshit in the middle where you need to look for n

    3 states for isit_two_char:
    1 - [n:n+2] has 1 char
    2 - [n:n+2] has 2 char
    3 - exiting loop that encloses this function

    """

    def __init__(self):
        self._state = self.start_state
        self._mainState = 2

    def get_next_values(self, state, inp):
        """
        The function takes 2 char (string) as input. This is to get around \n and the 2 chars that has \ as the first char. state is for self._state
        """
        print(inp)
        if state == 1:
            if inp == '\n':
                print('---------------------------------------------')
                self._state = 2
                return [None, None]
            elif inp[1] == '\\':
                self._state = 3
                return [inp[0]]
            else:
                return [inp[0], inp[1]]
        elif state == 2:
            if inp[0] == '#':
                self._state = 1
                return ['#', inp[1]]
            elif inp[1] == '#':
                self._state = 1
                return [None, '#']
            else:
                return [None, None]
        elif state == 3:
            if inp[0] == 'n':
                self._state = 2
                return [None, None]
            else:
                return ['\\', inp[0], inp[1]]

    def isit_two_char(self, state, inp):
        """
        The function is for determining the [n:n+2] of the list has 1 or 2 elements, and react accordingly. Depends on state of get_next_values (by reading self._state) but mainly uses its own state (self._mainState)

        Inp would be list
        state is int

        """
        if state == 1:
            self._mainState = 3
            inp += ['DELETE']
        elif state == 2:
            if len(inp) == 1:
                self._mainState = 1
            elif len(inp) == 2:
                self._mainState = 2
            elif len(inp) == 0:
                self._mainState = 3
            else:
                print('error')
        elif state == 3:
            self._mainState = 3
            print('error')

    def transduce(self, inp):
        counter = 0
        outputList = []
        while self._mainState != 3:
            self.isit_two_char(self._mainState, inp[counter:counter + 2])
            if self._mainState != 3:
                outputList += self.get_next_values(self._state, inp[counter:counter + 2])
            counter += 2
        if outputList[-1] == 'DELETE':
            del outputList[-1]
        else:
            pass
        return outputList




test = 'def f(x): # comment\n  return 1'
x = CommentsSM()
print(x.transduce(test))




































