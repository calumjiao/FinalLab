#pylint: disable=invalid-name
# this invalid name is not hurting theh program.
#pylint: disable = bare-exception
# does not effecting anything in the program
# pylint: disable= bare-except
# I already catch the specific exception before the generic one.
# pylint: disable= useless-else-on-loop
# I dont see if this is hurting anything
"""
this is a new class
"""
import difflib
from source.question_answer import QA
from source.shape_checker import get_triangle_type, get_quadrilateral_type
from source.answer_funcs import feet_to_miles, hal_20, get_git_branch, get_git_url
NOT_A_QUESTION_RETURN = "Was that a question?"
UNKNOWN_QUESTION = "I don't know, please provide the answer"
NO_QUESTION = 'Please ask a question first'
NO_TEACH = 'I don\'t know about that. I was taught differently'


class Interface(object):
    """
    this is class
    """
    def __init__(self):
        """
        this is class
        """
        self.how_dict = {}
        self.what_dict = {}
        #self.where_dict = {}
        self.who_dict = {}

        self.keywords = ['How', 'What', 'Where', 'Who', "Why", "Open", "Please"]
        self.question_mark = chr(0x3F)

        self.question_answers = {
            'What type of triangle is ': QA('What type of triangle is ', get_triangle_type),
            'What type of quadrilateral is '
            : QA('What type of quadrilateral is ', get_quadrilateral_type),
            'Open the door hal ': QA('Open the door hal ', hal_20),
            'How about a valid match'
            : QA('How about a valid match ', 'This is the answer for a valid match'),
            'What is feet in miles': QA('What is feet in miles', feet_to_miles),
            'Please clear memory ': QA('Please clear memory ', 'Memory is cleared'),
        }
        self.last_question = None

    def ask(self, question=""):
        """
        Ask function
        """
        if not isinstance(question, str):
            self.last_question = None
            raise Exception('Not A String!')
        if question[-1] != self.question_mark or question.split(' ')[0] not in self.keywords:
            self.last_question = None
            return NOT_A_QUESTION_RETURN
        else:
            parsed_question = ""
            args = []
            for keyword in question[:-1].split(' '):
                try:
                    args.append(float(keyword))
                except:
                    parsed_question += "{0} ".format(keyword)
            parsed_question = parsed_question[0:-1]
            self.last_question = parsed_question
            for answer in self.question_answers.values():
                if difflib.SequenceMatcher(a=answer.question, b=parsed_question).ratio() >= .90:
                    if answer.function is None:
                        return answer.value
                    else:
                        try:
                            return answer.function(*args)
                        except:
                            raise Exception("Too many extra parameters")
            else:
                return UNKNOWN_QUESTION

    def teach(self, answer=""):
        """
        teach function
        """
        if self.last_question is None:
            return NO_QUESTION
        elif self.last_question in self.question_answers.keys():
            return NO_TEACH
        else:
            self.__add_answer(answer)

    def correct(self, answer=""):
        """
        Correct Function
        """
        if self.last_question is None:
            return NO_QUESTION
        else:
            self.__add_answer(answer)

    def __add_answer(self, answer):
        """
        Add Answer function
        """
        self.question_answers[self.last_question] = QA(self.last_question, answer)
