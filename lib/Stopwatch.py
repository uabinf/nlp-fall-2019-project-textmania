#Stopwatch.py

import time

class Stopwatch:
    """ Simple class for timing tasks. Not meant for measuring performance. """

    def __init__(self, name):
        """
        :param name: string name of the stopwatch.
        """
    
        self.name = name
        self._start_time = None
        self._stop_time = None
        self._laps = None
        
    def start(self):
        """ Starts the watch """
        self._start_time = time.time()
        self._stop_time = None
        self._laps = []
        
    def stop(self):
        self._stop_time = time.time()
        
        
    def elapsed(self, round_to=2):
        """ 
        
        If Stopwatch is running returns the current amount of time since it started in seconds. 
        If stopped returns the time elapsed between starting and stopping the watch in seconds.
        
        :param round_to: The number of decimals to round the time to.
        
        """
        if self._start_time == None:
            return 0
        
        end_time = self._stop_time if self._stop_time != None else time.time()
        
        elapsed = end_time - self._start_time
        return elapsed if round_to == None else round(elapsed, round_to)
    
    def __str__(self):
        """ String representation - 'My stopwatch name 18.32s'  """
        return f"{self.name} {self.elapsed()}s"    



def stopwatch_sample():
    import sys
        
    stopwatch = Stopwatch("Sample Watch")
    
    stopwatch.start()

    time.sleep(1.5)
    
    print(stopwatch)
    
    time.sleep(1.2)
    
    print(stopwatch)
    
    stopwatch.stop()
    
    print(f"Elapsed: {stopwatch.elapsed(round_to=4)}")


# stopwatch_sample()
    