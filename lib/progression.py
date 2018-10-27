import threading
import time

import lib.html as html

my_obj = None
method = None

def monitor(object, call, operator):
    global my_obj
    global method

    my_obj = object
    method = call

    class Compute_Thread(threading.Thread):
        def __init__(self, name):
            threading.Thread.__init__(self)
            self.name = name

        def run(self):
            global method

            method()


    class Display_Thread(threading.Thread):
        def __init__(self, name):
            threading.Thread.__init__(self)
            self.name = name

        def run(self):
            global my_obj

            current_progress = None

            while my_obj.progress:
                if my_obj.progress != current_progress:
                    current_progress = my_obj.progress
                    if not current_progress:
                        break
                    o.handle(current_progress, operator)
                time.sleep(0.5)

    compute = Compute_Thread("compute_thread")
    display = Display_Thread("display_thread")

    compute.start()
    display.start()

    compute.join()
    display.join()

    return my_obj

def progression_print(p):
    print(p)

#progress operators - dictionary of functions to call on progress str

class Progression_Operator:
    def __init__(self):
        self.p_ops = {
        'print': progression_print
        }

    def handle(self, progress, operator):
        self.p_ops[operator](progress)

    def extend(self, dictionary):
        self.p_ops.update(dictionary)

o = Progression_Operator()