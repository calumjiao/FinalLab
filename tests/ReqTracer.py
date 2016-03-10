#pylint: disable=trailing-whitespace
#white spce should be alright
#pylint: disable=invalid-name
#using this name is not huriting anything.

"""
this is reqtracerfile
"""

from nose2.events import Plugin

class RequirementTrace(Plugin):
    """
    this is class
    """
    req_text = ""
    def __init__(self, text):
        """group = self.session.pluginargs
        group.add_argument("Hello", "World")"""
        self.req_text = text
        self.func_name = []
        

        
class JobStory(Plugin):
    """
    job story
    """
    desc = ""
    def __init__(self, text):
        """group = self.session.pluginargs
        group.add_argument("Hello", "World")"""
        self.desc = text
        self.func_name = []     

        

    

Requirements = {}
Stories = {}

def requirements(req_list):
    """
    another function
    """
    def wrapper(func):
        """
        another function
        """
        def add_req_and_call(*args, **kwargs):
            """
            another function
            """
            for req in req_list:
                if req not in Requirements.keys():
                    raise Exception('Requirement {0} not defined'.format(req))
                Requirements[req].func_name.append(func.__name__)
            return func(*args, **kwargs)

        return add_req_and_call

    return wrapper

with open('Requirements.txt') as f:
    for line in f.readlines():
        if '#00' in line:
            req_id, desc = line.split(' ', 1)
            Requirements[req_id] = RequirementTrace(desc)

def story(title1):
    """
    story function
    """
    def wrapper(func):
        """
        some function
        """
        def add_req_and_call(*args, **kwargs):
            """
            add request funtion
            """
            if title1 not in Stories.keys():
                raise Exception('Job Story {0} not defined'.format(title))
            Stories[title1].func_name.append(func.__name__)
            return func(*args, **kwargs)
        return add_req_and_call
        
    return wrapper

with open('Requirements.txt') as f:
    for line in f.readlines():
        if '*"' in line:
            title, desc = line.split('"*', 1)
            title = title[2:]
            Stories[title] = JobStory(desc)
