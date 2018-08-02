class CommentsSM():
    """
    3 states for get_next_values:
    1 - take in: Collect the string
    2 - Don't: Return None
    """
    start_state = 2

    def __init__(self):
        self._state = self.start_state

    def get_next_values(self, state, inp):
        if state == 1:
            if inp == '\n':
                self._state = 2
                return [None,None]
            else:
                return [inp]
        elif state == 2:
            if inp == '#':
                self._state = 1
                return ['#']
            else:
                return [None]

    def transduce(self,inp):
        outputList = []
        for i in inp:
            outputList += self.get_next_values(self._state,i)
        return outputList



test = 'def f(x): # comment\n  return 1'
x = CommentsSM()
print(x.transduce(test))