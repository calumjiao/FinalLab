# pylint: disable= too-few-public-methods
# I should not be important how many method are we using in any class..
"""
this is test file
"""
class QA(object):
    """
    this is class
    """
    def __init__(self, question, answer):
        """
        this is defination
        """
        self.question = question
        self.function = None
        self.value = None
        if hasattr(answer, '__call__'):
            self.function = answer
        else:
            self.value = answer
