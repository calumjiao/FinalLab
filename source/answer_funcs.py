# pylint: disable= trailing-whitespace
# White space is not important and wont affect the program.
# pylint: disable=invalid-name
# these name are invalid due to not giving meaning ful name but it is not hurting the program.
# pylint: disable=too-many-return-statements
# using number of if statment which required return statment for each if statment.
# pylint: diable= global-statement
# I dont want to change anythign that is already provided by instructor.
# pylint: disable= broad-except
# I already catch the specific exception before the generic one.
#pylint: disable = global-statement
# does not effecting anything in the program
"""
Well this is a skapke checker class
"""
import getpass
import random
import socket
import subprocess
import threading
import time

seq_finder = None

def feet_to_miles(feet):
    """
    This is function
    """
    return "{0} miles".format(float(feet) / 5280)

def hal_20():
    """
    This is function
    """
    return "I'm afraid I can't do that {0}".format(getpass.getuser())

def get_git_branch(args):
    """
    This is function
    """
    try:
        process = subprocess.Popen(args, stdout=subprocess.PIPE)
        output = process.communicate()[0]
    except ValueError:
        return "Unknown"
    except Exception:
        return "Unknown"    

    if not output:
        return "Unknown"
    return output.strip()

def get_git_url(args):
    """
    This is function
    """
    try:
        process = subprocess.Popen(args, stdout=subprocess.PIPE)
        output = process.communicate()[0]
    except ValueError:
        return "Unknown"
    except Exception:
        return "Unknown"    

    if not output:
        return "Unknown"
    return output.strip()

def get_other_users():
    """
    This is function
    """
    try:
        host = '192.168.3.64'
        port = '1337'

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.send('Who?')
        data = s.recv(255)
        s.close()
        return data.split('$')


    except IOError, e:
        print e
        return "IT'S A TRAAAPPPP"
    except Exception: 
        return "IT'S A TRAAAPPPP"


class FibSeqFinder(threading.Thread):
    """
    This is function
    """
    def __init__(self, *args, **kwargs):
        """
        """
        super(FibSeqFinder, self).__init__(*args, **kwargs)
        self.sequence = [0, 1]
        self._stop = threading.Event()

    def stop(self):
        """
        This is function
        """
        self._stop.set()

    def run(self):
        """
        This is function
        """
        while not self._stop.isSet():
            self.sequence.append(self.sequence[-1] + self.sequence[-2])
            time.sleep(1.00)

def get_fibonacci_seq(index):
    """
    Fibonacci methods
    """
    index = int(index)
    global seq_finder
    if seq_finder is None:   
        seq_finder = FibSeqFinder()
        seq_finder.start()
    seq_finder.stop()

    if index > len(seq_finder.sequence):
        value = random.randint(0, 10)
        if value > 6:
            return "Thinking..."
        elif value > 3:
            return "One second"
        else:
            return "cool your jets"
    else:
        return seq_finder.sequence[index]      

def nDigitOfPi(limit):  # Generator function
    """
    Prints out the digits of PI
    until it reaches the given limit
    """

    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3

    counter = 0
    if limit < 1:
        return 0        
    while counter != limit:
        if 4 * q + r - t < n * t:
            if (limit-1) == counter:
                return n
            counter += 1
            nr = 10 * (r - n * t)
            n = ((10 * (3 * q + r)) // t) - 10 * n
            q *= 10
            r = nr
        else:
            nr = (2 * q + r) * l
            nn = (q * (7 * k) + 2 + (r * l)) // (t * l)
            q *= k
            t *= l
            l += 2
            k += 1
            n = nn
            r = nr   

def unit_conversation(current_unit, target_unit):
    """
    convert unit methods into meter
    feet, centimeter and melimeter
    """
    if current_unit == "meter" and target_unit == "feet":
        return 3
    if current_unit == "feet" and target_unit == "meter":
        return 1 / 3.0  
    if current_unit == "meter" and target_unit == "centimeter":
        return 10
    if current_unit == "centimeter" and target_unit == "meter":
        return 0.1
    if current_unit == "meter" and target_unit == "milimeter":
        return 100  
    if current_unit == "milimeter" and target_unit == "meter":
        return 0.01 
    if current_unit == "milimeter" and target_unit == "centimeter":
        return 0.1
    if current_unit == "centimeter" and target_unit == "milimeter":
        return 10
    if current_unit == "lb" and target_unit == "kg":
        return 0.45
    if current_unit == "inches" and target_unit == "centimeter":
        return 2.5
