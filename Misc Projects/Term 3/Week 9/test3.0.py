
class FirstWordSM(sm.SM):
    start_state = None
    """
    2 states:
    1 - taking value
    2 - don't take value    
    """

    def __init__(self):
        self.state = self.start_state

    def get_next_values(self, state, inp):
        if state == 1:
            if inp == ' ':
                self.state = 2
                return (self.state, None)
            else:
                return (self.state, inp)
        elif state == 2:
            if inp == '\n':
                self.state = 1
                return (self.state ,None)
            else:
                return (self.state, None)

    def transduce(self, inp):
        outputList = []
        for i in inp:
            outputList += [self.get_next_values(self.state ,i)[1]]




test = 'def f(x): # comment\n  return 1'
x = CommentsSM()
print(x.transduce(test))





















