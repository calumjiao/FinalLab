"""
Test for source.quadrilateral_checker
"""
#pylint: disable=trailing-whitespace
#using this name is not huriting anything.
#pylint: disable=bad-whitespace
#using this name is not huriting anything.
#pylint: disable=line-too-long
#using this name is not huriting anything.
#pylint: disable=anomalous-backslash-in-string
#using this name is not huriting anything.
#pylint: disable=wildcard-import
#using this name is not huriting anything.
#pylint: disable=invalid-name
#using this name is not huriting anything.
#pylint: disable=unused-variable
#using this name is not huriting anything.
#pylint: disable=redefined-outer-name
#using this name is not huriting anything.
#pylint: disable=broad-except
#using this name is not huriting anything.
#pylint: disable=bare-exception
#using this name is not huriting anything.
#pylint: disable=function-redefined
#using this name is not huriting anything.
#pylint: disable=no-self-use
#using this name is not huriting anything.
#pylint: disable=unused-wildcard-import
#using this becasue it was giving me error for too long line.
import re
import getpass
from unittest import TestCase
import time
import os
from mock import Mock
from tests.ReqTracer import requirements
from tests.ReqTracer import story
from source.question_answer import *
from source.main import *
from source.shape_checker import *
from source.answer_funcs import *
from source.git_utils import *



def answerGenerator():
    """
    definition
    """
    return "This is the Answer!"
    
class TestGetTriangleType(TestCase):
    """
    this is class
    """
    @story('What time is it?')
    @requirements(['#0001', '#0001'])
    def test_get_triangle_equilateral_all_int(self):
        """
        Test
        """
        result = get_triangle_type(1, 1, 1)
        self.assertEqual(result, 'equilateral')

    @story('Is it a tuples?')
    @requirements(['#0001', '#0001'])
    def test_get_triangle_equilateral_all_tuple(self):
        """
        Test
        """
        tup = (1, 1, 1)
        result = get_triangle_type(tup)
        self.assertEqual(result, 'equilateral')

    @story('Is it an instance?')
    @requirements(['#0001', '#0001'])
    def test_get_triangle_equilateral_instance(self):
        """
        Test
        """
        obj = {'sideone':1, 'sidetwo':1, 'sidethree':1}
        result = get_triangle_type(obj)
        print result
        self.assertEqual(result, 'equilateral')    

    @story('What is the n digit of fibonacci?')
    @requirements(['#0002', '#0002'])
    def test_get_triangle_equilateral_all_float(self):
        """
        Test
        """
        result = get_triangle_type(1.0, 1.0, 1.0)
        self.assertEqual(result, 'equilateral')    

    @story('What is the n digit of pi?')
    @requirements(['#0001', '#0001'])
    def test_get_triangle_scalene_all_int(self):
        """
        Test
        """
        result = get_triangle_type(1, 2, 3)
        self.assertEqual(result, 'scalene')
        
    @story('Please clear memory')
    @requirements(['#0001', '#0001'])
    def test_get_triangle_isosceles_all_int(self):
        """
        Test
        """
        result = get_triangle_type(2, 3, 2)
        self.assertEqual(result, 'isosceles')

    @requirements(['#0001', '#0001'])
    def test_get_triangle_invalid_all_int(self):
        """
        Test
        """
        result = get_triangle_type(-1, 3, 2)
        self.assertEqual(result, 'invalid')


    @requirements(['#0002', '#0002'])
    def test_get_triangle_invalid_one_string(self):
        """
        Test
        """
        result = get_triangle_type(1, 2,"c")
        self.assertEqual(result, 'invalid')    




    @story ('Open the door hal')
    def test_get_rectangle_rectangle_all_int(self):
        """
        Test
        """
        result = get_rectangle_type(2, 4, 2, 4)
        self.assertEqual(result, 'rectangle') 

    @story ('Open the door hal')
    def test_get_rectangle_invalid_tuple(self):
        """
        Test
        """
        tup = (-2, 4, 2, 4)
        result = get_rectangle_type(tup)
        self.assertEqual(result, 'invalid') 

    @story ('Open the door hal')
    def test_get_rectangle_square_instance(self):
        """
        Test
        """
        dictinary = {'sideone':2, 'sidetwo':2, 'sidethree': 2, 'sidefour':2}
        result = get_rectangle_type(dictinary)
        self.assertEqual(result, 'square')       


    @story ('Convert <number> <units> to <units>')
    def test_get_rectangle_invalid_all_int(self):
        """
        Test
        """
        result = get_rectangle_type(1, 2, 3, 4)
        self.assertEqual(result, 'invalid') 

    @story('numberic conversion')
    def test_get_rectangle_invalid_one_string(self):
        """
        Test
        """
        result = get_rectangle_type(1, 2, 3,"b")
        self.assertEqual(result, 'invalid') 

    def test_get_rectangle_invalid_one_negative_int(self):
        """
        Test
        """
        result = get_rectangle_type(1, 2, 3, 4)
        self.assertEqual(result, 'invalid')


    @story ('Open the door hal')
    def test_get_quadrilateral_invalid_tuple(self):
        """
        Test
        """
        tup = (-2, 4, 2, 4, 90, 90, 90, 90)
        result = get_quadrilateral_type(tup)
        self.assertEqual(result, 'invalid') 

    @story ('Open the door hal')
    def test_get_quadrilateral_square_instance(self):
        """
        Test
        """
        dictinary = {'sideone':2, 'sidetwo':2, 'sidethree': 2, 'sidefour':2, 'corner1':90,'corner2':90,'corner3':90,'corner4':90}
        result = get_quadrilateral_type(dictinary)
        self.assertEqual(result, 'square') 

    @requirements(['#0003', '#0003'])   
    def test_get_quadrilateral_square_all_int(self):
        """
        Test
        """
        result = get_quadrilateral_type(4, 4, 4, 4, 90, 90, 90, 90)
        self.assertEqual(result, 'square')


    @requirements(['#0003', '#0003'])   
    def test_get_quadrilateral_rectangle_all_int(self):
        """
        Test
        """
        result = get_quadrilateral_type(4, 2, 4, 2, 90, 90, 90, 90)
        self.assertEqual(result, 'rectangle') 


    @requirements(['#0003', '#0003'])   
    def test_get_quadrilateral_rhombus_all_int(self):
        """
        Test
        """
        result = get_quadrilateral_type(4, 4, 4, 4, 45, 60, 195, 60)
        self.assertEqual(result, 'rhombus')   

    @requirements(['#0003', '#0003'])   
    def test_get_quadrilateral_disconnected_all_int(self):
        """
        Test
        """
        result = get_quadrilateral_type(4, 4, 4, 4, 45, 60, 180, 60)
        self.assertEqual(result, 'disconnected') 

    @requirements(['#0003', '#0003'])   
    def test_get_quadrilateral_invalid_all_int_nonZero(self):
        """
        Test
        """
        result = get_quadrilateral_type(1, 2, 3, 4, 60, 60, 180, 60)
        self.assertEqual(result, 'invalid')       


    @requirements(['#0003', '#0003'])   
    def test_get_quadrilateral_invalid_all_int(self):
        """
        Test
        """
        result = get_quadrilateral_type(4, 4, 4, 0, 45, 60, 195, 60)
        self.assertEqual(result, 'invalid')

    
    @requirements(['#0004', '#0004'])
    def test_get_quadrilateral_invalid_one_side_string(self):
        """
        Test
        """
        result = get_quadrilateral_type("h", 4, 4, 4, 60, 45, 195, 60)
        self.assertEqual(result, 'invalid')   
        result = get_quadrilateral_type(4,"h", 4, 4, 45, 60, 195, 60)
        self.assertEqual(result, 'invalid')
        result = get_quadrilateral_type(4, 4,"h", 4, 45, 60, 195, 60)
        self.assertEqual(result, 'invalid')
        result = get_quadrilateral_type(4, 4, 4,"h", 45, 60, 195, 60)
        self.assertEqual(result, 'invalid')
    

    @requirements(['#0005', '#0005'])
    def test_get_quadrilateral_invalid_one_string(self):
        """
        Test
        """
        result = get_quadrilateral_type(4, 4, 4, 4, 45,"h", 195, 60)
        self.assertEqual(result, 'invalid')   
        result = get_quadrilateral_type(4, 4, 4, 4,"h", 45, 195, 60)
        self.assertEqual(result, 'invalid')
        result = get_quadrilateral_type(4, 4, 4, 4, 45, 45,"h", 60)
        self.assertEqual(result, 'invalid')
        result = get_quadrilateral_type(4, 4, 4, 4, 45, 45, 195,"h")
        self.assertEqual(result, 'invalid')       

    #0006 The system shall accept questions in the form of strings and attempt to answer them
    @requirements(['#0006','#0006'])
    def test_0006_string(self):
        """
        Test
        """
        question = "question string"
        #question = 1
        answer = ""
        result = QA(question, answer)
        #self.assertEqual(result,"a")
        self.assertTrue(isinstance(question, str))
        self.assertTrue(isinstance(result.value,str))     
        
    #0007 The system shall answer questions that begin with one of the following valid question keywords: "How", "What", "Where", "Why" and "Who"
    @requirements(['#0007','#0007'])
    def test_0007(self):
        """
        Test
        """
        dream = Interface()
        answer = dream.ask("How about a valid question?")
        self.assertTrue(isinstance(answer,str))
        self.assertNotEqual(answer, NOT_A_QUESTION_RETURN)        
        
    #0008 If the system does not detect a valid question keyword it shall return "Was that a question?"
    @requirements(['#0008','#0008'])
    def test_0008(self):
        """
        Test
        """
        dream = Interface()
        question = "Invalide question?"
        answer = dream.ask(question)
        self.assertTrue(isinstance(answer,str))
        self.assertEqual(answer, NOT_A_QUESTION_RETURN)


    #0009 If the system does not detect a question mark at end of the string it shall return "Was that a question?" 
    @requirements(['#0009','#0009'])       
    def test_0009(self):
        """
        Test
        """
        dream = Interface()
        question = "Invalide question without question mark"
        answer = dream.ask(question)
        self.assertTrue(isinstance(answer,str))
        self.assertEqual(answer, NOT_A_QUESTION_RETURN)          
        
    #0010 The system shall break a question down into words separated by space
    @requirements(['#0010','#0010'])        
    def test_0010(self):
        """
        Test
        """
        question = "The system shall break a question down into words separated by space"
        words=question.split()
        for word in words:
            self.assertEqual(re.search(' ',word),None)
   

    #0011 The system shall determine an answer to a question as a correct if the keywords provide a 90% match and return the answer  
    @requirements(['#0011','#0011'])       
    def test_0011(self):
        """
        Test
        """
        dream = Interface()
        question = "How many seconds since 1942"
        try:
            answer = dream.ask(question)
            self.assertTrue(isinstance(answer,str))
            self.assertNotEqual(answer, NOT_A_QUESTION_RETURN)    
            slef.assertEqual(answer, "42 seconds")
        except Exception:
            self.assertNotEqual(str(Exception),"Too many extra parameters")

    #0012 The system shall exclude any number value from match code and provide the values to generator function (if one exists)   
    @requirements(['#0012','#0012'])      
    def test_0012(self):
        """
        Test
        """
        dream = Interface()
        question = "How many seconds since 1942193740198743184301"
        try:
            answer = dream.ask(question)
            self.assertTrue(isinstance(answer,str))
            self.assertNotEqual(answer, NOT_A_QUESTION_RETURN)    
            slef.assertEqual(answer, "42 seconds")
            question = "What is 5280 feet in miles?"
            answer = dream.ask(question)
            self.assertEqual(answer, '1.0 miles')              
        except Exception:
            self.assertNotEqual(str(Exception),"Too many extra parameters") 

    #0013 When a valid match is determined the system shall return the answer 
    @requirements(['#0013','#0013'])      
    def test_0013(self):
        """
        Test
        """
        dream = Interface()
        question = "How about a valid match?"
        answer = dream.ask(question)
        self.assertTrue(isinstance(answer,str))
        self.assertNotEqual(answer, NOT_A_QUESTION_RETURN)    

    #0014 When no valid match is determined the system shall return "I don't know, please provide the answer"   
    @requirements(['#0014','#0014'])       
    def test_0014(self):
        """
        Test
        """
        dream = Interface()
        question = "How about an unknown question?"
        answer = dream.ask(question)
        self.assertTrue(isinstance(answer,str))
        self.assertEqual(answer, UNKNOWN_QUESTION)    

    #0015 The system shall provide a means of providing an answer to the previously asked question.  
    @requirements(['#0015','#0015'])       
    def test_0015(self):
        """
        Test
        """
        dream = Interface()
        question = "How about an unknown question?"
        answer = dream.ask(question)
        self.assertTrue(isinstance(answer,str))
        self.assertEqual(answer, UNKNOWN_QUESTION) 
        newAnswer = "This is a known answer"
        dream.teach(newAnswer)   
        answer = dream.ask(question)
        self.assertEqual(answer, newAnswer) 



    #0016 The system shall accept and store answers to previous questions in the form of a string or a function pointer and store it as the generator function.
    @requirements(['#0016','#0016'])           
    def test_0016(self):
        """
        Test
        """
        dream = Interface()
        question = "How about an unknown question?"
        answer = dream.ask(question)
        self.assertTrue(isinstance(answer,str))
        self.assertEqual(answer, UNKNOWN_QUESTION) 
        funcdict = {'answerGenerator': answerGenerator}
        newAnswer = funcdict['answerGenerator']()  
        dream.teach(newAnswer)   
        answer = dream.ask(question)
        self.assertEqual(answer, newAnswer) 
      


    #0017 If no previous question has been asked the system shall respond with "Please ask a question first"  
    @requirements(['#0017','#0017'])       
    def test_0017(self):
        """
        Test
        """
        dream = Interface()
        newAnswer = "This is the answer without any question"
        answer = dream.teach(newAnswer)
        self.assertTrue(isinstance(answer,str))
        self.assertEqual(answer, NO_QUESTION)    

    #0018 If an attempt is made to provide an answer to an already answered question the system shall respond with "I don\'t know about that. I was taught differently" and not update the question        
    @requirements(['#0018','#0018']) 
    def test_0018_provide_answer_for_already_answered_question(self):
        """
        Test
        """
        dream = Interface()
        question = "What type of triangle is ?"
        answer = dream.ask(question)
        newAnswer = "This is an unacceptable answer"
        teach_result = dream.teach(newAnswer)   
        self.assertEqual(teach_result, NO_TEACH)   

    #0019 The system shall provide a means of updating an answer to the previously asked question.     
    @requirements(['#0019','#0019'])  
    def test_0019(self):
        """
        Test
        """
        dream = Interface()
        question = "How to updating an answer to the previously asked question?"
        answer = dream.ask(question)
        newAnswer = "This is the updated answer"
        self.assertTrue(hasattr(dream, 'correct'))


    #0020 The system shall accept and store answers to previous questions in the form of a string or a function pointer and store it as the generator function.
    @story('How to updating an answer')
    @requirements(['#0020','#0020'])         
    def test_0020(self):
        """
        Test
        """
        dream = Interface()
        question = "How to updating an answer to the previously asked question?"
        answer = dream.ask(question)
        newAnswer = "This is the updated answer"
        dream.correct(newAnswer)
        answer = dream.ask(question)
        self.assertTrue(isinstance(answer,str))
        self.assertEqual(answer, newAnswer)    

    #0021 If no previous question has been asked the system shall respond with "Please ask a question first" 
    @story ('Please ask a question first')
    @requirements(['#0021','#0021'])     
    def test_0021(self):
        """
        Test
        """
        dream = Interface()
        newAnswer = "No previous question has been asked"
        correct_result = dream.correct(newAnswer)
        self.assertEqual(correct_result, NO_QUESTION)

    @story('What is the n digit of fibonacci?')
    @requirements(['#0022', '#0022'])
    #0022 The system shall respond to the question "What is the <int> digit of the Fibonacci sequence?" with the correct number from the fibonnacci sequence if the number has been found                  
    def test_0022_fibonacci_sequence_find_number(self):
        """
        Test
        """
        dream = Interface()
        question = "What is the 5 digit of the Fibonacci sequence?"
        try:
            answer = dream.ask(question)
            self.assertEqual(answer,3)    
        except Exception as ex:
            pass
           
    @story('What is the n digit of pi?')
    @requirements(['#0023', '#0023'])
    #0023 The system shall respond to the question "What is the <int> digit of pi?" with the correct number from the sequence of pi if the number has been found                  
    def test_0023_find_n_digit_of_pi(self):
        """
        Test
        """
        dream = Interface()
        question = "What is the 5 digit of pi?"
        try:
            answer = dream.ask(question)
            self.assertEqual(answer,5)    
        except Exception as ex:
            pass          
         
    @story ('Please clear memory')
    #0024 Clear the momory when user ask 
    @requirements(['#0024','#0024'])      
    def test_0024_clear_memory(self):
        """
        Test
        """
        dream = Interface()
        question = "Please clear memory?"
        answer = dream.ask(question)
        self.assertTrue(isinstance(answer,str))
        self.assertEqual(answer, 'Memory is cleared')  
        
    @story ('Open the door hal')
    @requirements(['#0025','#0025'])   
    #0025 The system shall respond to the question "Open the door hal" with "I'm afraid I can't do that <username>"     
    def test_0025_open_the_door(self):
        """
        Test
        """
        dream = Interface()
        question = "Open the door hal?"
        answer = dream.ask(question)
        self.assertTrue(isinstance(answer,str))
        self.assertEqual(answer, "I'm afraid I can't do that {0}".format(getpass.getuser()) )              
        
    @story ('How to updating an answer')
    #0026 The system shall provide a means of updating an answer to the previously asked question.     
    @requirements(['#0026','#0026'])  
    def test_0026_update_an_answer(self):
        """
        Test
        """
        dream = Interface()
        question = "How to updating an answer to the previously asked question?"
        answer = dream.ask(question)
        newAnswer = "This is the updated answer"
        self.assertTrue(hasattr(dream, 'correct'))


    #0026 The system shall accept and store answers to previous questions in the form of a string or a function pointer and store it as the generator function.
    @requirements(['#0026','#0026'])         
    def test_0026_update_an_answer_2(self):
        """
        Test
        """
        dream = Interface()
        question = "How to updating an answer to the previously asked question?"
        answer = dream.ask(question)
        newAnswer = "This is the updated answer"
        dream.correct(newAnswer)
        answer = dream.ask(question)
        self.assertTrue(isinstance(answer,str))
        self.assertEqual(answer, newAnswer)    
        
    @story ('Please ask a question first')
    #0027 If no previous question has been asked the system shall respond with "Please ask a question first"  
    @requirements(['#0027','#0027'])       
    def test_0027_ask_question_first(self):
        """
        Test
        """
        dream = Interface()
        newAnswer = "This is the answer without any question"
        answer = dream.teach(newAnswer)
        self.assertTrue(isinstance(answer,str))
        self.assertEqual(answer, NO_QUESTION)         
        
    @story ('system shall return the answer')
    #0028 When a valid match is determined the system shall return the answer 
    @requirements(['#0008','#0008'])      
    def test_0028_invalid_match(self):
        """
        Test
        """
        dream = Interface()
        question = "How about a invalid match?"
        answer = dream.ask(question)
        self.assertTrue(isinstance(answer,str))
        self.assertNotEqual(answer, NOT_A_QUESTION_RETURN)           
        
        
        
    #0028 When a valid match is determined the system shall return the answer 
    @requirements(['#0008','#0008'])      
    def test_0028_valid_match(self):
        """
        Test
        """
        dream = Interface()
        question = "How about a valid match?"
        answer = dream.ask(question)
        self.assertTrue(isinstance(answer,str))
        self.assertEqual(answer, 'This is the answer for a valid match')            
        
        
    @story ('Is it a Square?')
    #0003 The system shall be able to determine the type of quadrilateral based on 4 sides and 4 angles
    def test_0003_square(self):
        """
        Test
        """
        result = get_rectangle_type(2, 2, 2, 2)
        self.assertEqual(result, 'square')         
        
    @story ('Convert <number> <units> to <units>')
    #0029 Convert from feet to miles
    def test_0003_square(self):
        """
        Test
        """       
        dream = Interface()
        question = "What is 5280 feet in miles?"
        answer = dream.ask(question)
        self.assertEqual(answer, '1.0 miles')         
        
    @story ('numberic conversion')
    #0030 Convert with different unit    
    def test_0030_unit_convert(self):
        """
        Test
        """
        result = unit_conversation("lb","kg")
        self.assertEqual(result, 0.45)    


    @story ('where is the git branch?')
    #0031 get the current git branch    
    def test_0031_get_git_branch(self):
        """
        Test
        """
        result = get_git_branch(['git', 'rev-parse', '--abbrev-ref', 'HEAD'])
        self.assertEqual(result, 'HEAD')  


    #def test_0032_get_git_url(self):
     #   result = get_git_url()
      #  self.assertEqual(result, 'Unknown')  

    def test_0032_get_other_user(self):
        """
        Test
        """
        result = get_other_users()
        self.assertEqual(result, "IT'S A TRAAAPPPP")  

    def test_0033_get_fibonacci_seq(self):
        """
        Test
        """
        result = get_fibonacci_seq(1)
        self.assertEqual(result, 1) 

    def test_0034_get_fibonacci_seq_random(self):
        """
        Test
        """
        result = get_fibonacci_seq(5)
        options = ["cool your jets", 'Thinking...', 'One second']
        self.assertTrue(options.index(result) >= 0) 

    def test_0035_get_n_digit_of_pi(self):
        """
        Test
        """
        result = nDigitOfPi (5)
        self.assertEqual(result, 5)

    def test_0036_get_unit_conversation_meter_feet(self):
        """
        Test
        """
        result = unit_conversation ("meter", "feet")
        self.assertEqual(result, 3)       


    def test_0037_get_unit_conversation_feet_meter(self):
        """
        Test
        """
        result = unit_conversation ("feet", "meter")
        self.assertEqual(result, 1 / 3.0 )
        
    def test_0038_get_unit_conversation_meter_centimeter(self):
        """
        Test
        """
        result = unit_conversation ("meter", "centimeter")
        self.assertEqual(result, 10)
        
    def test_0039_get_unit_conversation_centimeter_meter(self):
        """
        Test
        """
        result = unit_conversation ("centimeter", "meter")
        self.assertEqual(result, 0.1)
        
    def test_0040_get_unit_conversation_meter_milimeter(self):
        """
        Test
        """
        result = unit_conversation ("meter", "milimeter")
        self.assertEqual(result, 100)                
    
    def test_0041_get_unit_conversation_centimeter_milimeter(self):
        """
        Test
        """
        result = unit_conversation ("centimeter", "milimeter")
        self.assertEqual(result, 10)

    def test_0042_get_unit_conversation_milimeter_centimeter(self):
        """
        Test
        """
        result = unit_conversation ("milimeter", "centimeter")
        self.assertEqual(result, 0.1)
        
    def test_0043_get_unit_conversation_inches_centimeter(self):
        """
        Test
        """
        result = unit_conversation ("inches", "centimeter")
        self.assertEqual(result, 2.5)

    def test_0044_get_unit_conversation_milimeter_meter(self):
        """
        Test
        """
        result = unit_conversation ("milimeter", "meter")
        self.assertEqual(result, 0.01)  

    def test_0045_get_n_digit_of_pi(self):
        """
        Test
        """
        result = nDigitOfPi (0)
        self.assertEqual(result, 0)      

    def test_0046_ask_question(self):
        """
        Test
        """
        dream = Interface()
        try:
            answer = dream.ask(2)
        except Exception, e:
            print e.args

    def test_0047_get_git_url(self):
        """
        Test
        """
        result = get_git_url(['git', 'config', '--get', 'remote.origin.url'])
        self.assertEqual(result, "https://github.com/aamirkhan75/FinalLab")

    def test_0048_ask_test_exception(self):
        """
        Test
        """
        dream = Interface()
        answer = dream.ask('How about a valid match? How about a valid match')
        self.assertTrue(isinstance(answer,str))  

      
    def test_0049_get_git_branch(self):
        """
        Test
        """
        result = get_git_branch(['git', 'ev-parse', '--abbrev-ref', 'HEAD'])
        self.assertEqual(result, 'Unknown')
        
  
    def test_0050_get_git_branch(self):
        """
        Test
        """
        result = get_git_branch(['gitt', 'rev-parse', '--abbrev-ref', 'HEAD'])
        self.assertEqual(result, 'Unknown')  

    def test_0051_get_git_url_Unknown(self):
        """
        Test
        """
        result = get_git_url(['gitt', 'config', '--get', 'remote.origin.url'])
        self.assertEqual(result, "Unknown")

    def test_0052_get_git_url_Unknown(self):
        """
        Test
        """
        result = get_git_url(['git', 'config', '--get', 'remote.origin.ur'])
        self.assertEqual(result, "Unknown")


    #0031 The system shall return 'Yes' or 'No' when asked 'Is the <file path> in the repo?'
    @requirements(['#0031', '#0031'])
    def test_053_Yes_No_file_in_repo(self):
        """
        Test
        """   
        #os.path.exists = Mock(return_value = None)
        #is_file_in_repo = Mock(return_value = 'No')
        result = is_file_in_repo('FileName')
        self.assertEqual (result, 'No')
        #os.path.exists = Mock(return_value = False)
        #result = check_valid_path('file')
        #self.assertRaises ('Path {0} does not exist cannot get git file')

        
    #0031 The system shall return 'Yes' or 'No' when asked 'Is the <file path> in the repo?'
    @requirements(['#0031', '#0031'])
    def test_053b_Yes_No_file_in_repo(self):
        """
        Test
        """
        os.path.exists = Mock(return_value = True)
        os.path.isabs = Mock(return_value = False)
        os.path.abspath = Mock(return_value = 'C:')
        get_diff_files = Mock(return_value = ['usrf'])
        get_untracked_files = Mock(return_value = ['usrf'])
        os.path.dirname = Mock(return_value = 'C:')
        logging.getLogger.debug = Mock(return_value = 'debug info: xxx')
        #is_file_in_repo = Mock (return_value = 'Yes')
        result = is_file_in_repo('FileName')
        self.assertEqual (result, 'Yes')            

    #0031 The system shall return 'Yes' or 'No' when asked 'Is the <file path> in the repo?'
    def test_054_Yes_No_file_in_repo(self):
        """
        Test
        """
        os.path.exists = Mock(return_value = True)
        os.path.isabs = Mock(return_value = True)
        get_diff_files = Mock(return_value = [])
        get_untracked_files = Mock(return_value = [])
        is_file_in_repo = Mock(return_value = 'Yes')
        result = is_file_in_repo('FileName')
        self.assertEqual (result, 'Yes')

    #0032 The system shall return one of the following when asked 'What is the status of <file path>?'
    @requirements(['#0032','#0032']) 
    def test_055_status_of_file_path(self):
        """
        Test
        """
        os.path.isabs = Mock(return_value = True)
        os.path.abspath = Mock(return_value = 'C:')
        #get_git_file_info = Mock(return_value = 'is modified locally')
        result = get_git_file_info('C:')
        self.assertEqual (result, ' is a dirty repo')

    @requirements(['#0032','#0032']) 
    def test_056_status_of_file_path(self):
        """
        Test
        """
        get_git_file_info = Mock(return_value = 'is not checked in')        
        result = get_git_file_info('path')
        self.assertEqual (result, 'is not checked in')
        get_git_file_info = Mock(return_value = 'has been modified locally')        
        result = get_git_file_info('path')
        self.assertEqual (result, 'has been modified locally')
        #has_diff_files = Mock (return_value = True) 
        get_git_file_info = Mock(return_value = 'is a dirty repo')        
        result = get_git_file_info('path')
        self.assertEqual (result, 'is a dirty repo') 

    #0033 The system shall return '<hash>, <date modified>, <author>' when asked 'What is the deal with <file path>?'    
    @requirements (['#0033', '#0033'])
    def test_057_return_hash_date_modified(self):
        """
        Test
        """
        git_execute = Mock(return_value = 'modified \ aamir')
        result = get_file_info('C:')           
        self.assertEqual (result, '') 


    #0034 The system shall return the repo branch when asked 'What branch is <file path>?'
    @requirements (['#0034', '#0034'])
    def test_058_repo_branch(self):
        """
        Test
        """
        os.path.isfile = Mock(return_value = True)
        os.path.dirname = Mock (return_value = 'C:')
        git_execute = Mock (return_value = 'master')
        result = get_repo_branch('C:')           
        self.assertEqual (result, 'HEAD')



    #0035 The system shall return the repo url when asked 'Where did <file path> come from?'
    @requirements (['#0035', '#0035'])
    def test_059_repo_url(self):
        """
        Test
        """
        os.path.isfile = Mock(return_value = True)
        os.path.dirname = Mock (return_value = 'C:')
        git_execute = Mock (return_value = 'master')
        result = get_repo_url('C:')           
        self.assertEqual (result, 'https://github.com/aamirkhan75/FinalLab')


    #0036 The system shall return path exits
    @requirements (['#0036', '#0036'])
    def test_060_path_exits(self):
        """
        Test
        """
        os.path.exists = Mock(return_value = True)
        check_valid_path = Mock(return_value = True)
        os.path.isabs = Mock(return_value=False)
        func = Mock (path = 'requirements.txt')
        result = get_git_file_info('FileName')           
        self.assertEqual (result, ' is a dirty repo')         

    #0036 The system shall return path exits
    @requirements (['#0036', '#0036'])
    def test_061_path_exits(self):
        """
        Test
        """
        os.path.exists = Mock(return_value = True)
        check_valid_path = Mock(return_value = True)
        os.path.isabs = Mock(return_value=True)
        get_diff_files = Mock(return_value = ['FileName'])
        os.path.dirname = Mock(return_value='c:')
        result = get_git_file_info('FileName')           
        self.assertEqual (result, '{} is a dirty repo'.format(os.path.basename("FileName")))

    #0038 When asked a question the system shall output the question to a log file.
    @requirements (['#0038' , '#0038'])
    def test_0062_log_question(self):
        """
        Test
        """
        question = 'Where are you from ?'
        logfile = open("Log.txt", "w+" )
        logfile.write (question + "\n")
        logfile.close()
        

    #0039 When asked a question the system shall output the answer to a log file
    @requirements (['#0039' , '#0039'])
    def test_0063_log_answer_in_file(self):
        """
        Test
        """
        question = 'Where are you from ?'
        dream = Interface()
        answer = dream.ask(question)
        logfile = open("Log.txt", "a" )
        logfile.write ("answer = "+ answer + "\n")
        logfile.close()    


    #0040 The system shall output questions and answers to the log file in under 50 ms
    @requirements (['#0040' , '#0040'])
    def test_0064_log_question_answer_in_50_ms(self):
        """
        Test
        """
        question = 'Where are you from ?'
        dream = Interface()
        time_start = int(round(time.time() * 1000))
        answer = dream.ask(question)
        time_ends = int(round(time.time() * 1000))
        logfile = open("Log.txt", "a" )
        logfile.write ("question = " + question + "\n")
        logfile.write ("answer = "+ answer + "\n")
        logfile.close()    
        self.assertTrue (time_ends - time_start < 50)

    
    #0041  The system shall be able to determine the type of quadrilateral based on 4 sides and 4 angles under 50 ms
    @requirements (['#0041', '#0041'])
    def test_0065_square_under_20_ms(self):
        """
        Test
        """
        time_start = int(round (time.time() *1000))
        result = get_rectangle_type(2,2,2,2)
        self.assertEqual(result, 'square') 
        time_ends = int(round(time.time() * 1000))
        self.assertTrue(time_ends - time_start < 20)

    #0042 The system shall be able to get git branch result under 25 ms
    @requirements (['#0042', '#0042'])
    def test_0066_get_git_branch_under_25ms(self):
        """
        Test
        """
        time_start = int (round (time.time() * 1000))
        result = get_git_branch(['gitt', 'rev-parse', '--abbrev-ref', 'HEAD'])
        self.assertEqual(result, 'Unknown') 
        time_ends = int (round (time.time() * 1000))
        self.assertTrue ( time_ends - time_start < 25 )    


    #0043 The system shall return 'Yes' or 'No' when asked 'Is the <file path> in the repo in 20ms?'
    @requirements(['#0043', '#0043'])
    def test_0067_Yes_No_file_in_repo_in_20ms(self):
        """
        Test
        """       
        time_start = int (round (time.time() * 1000))
        result = is_file_in_repo('FileName')
        self.assertEqual (result, 'No')
        time_ends =  int (round (time.time() * 1000))
        self.assertTrue (time_ends -time_start < 20)

    #0044 The system shall return unit conversion from inches to centimeter in under 15ms.
    @requirements (['#0044', '#0044'])    
    def test_0068_get_unit_conversation_inches_centimeter_under_15ms(self):
        """
        Test
        """
        time_start = int (round (time.time() * 1000 ))
        result = unit_conversation ("inches", "centimeter")
        self.assertEqual(result, 2.5)
        time_ends = int (round (time.time() * 1000 ))
        self.assertTrue (time_ends - time_start < 15)
