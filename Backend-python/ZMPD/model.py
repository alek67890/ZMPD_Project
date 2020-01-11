import threading
import time

class ExportingThread(threading.Thread):
    def __init__(self, name=''):
        self.progress = 0
        self.output = {}
        self.status = 'created'
        self.task_name = name
        super().__init__()

    def run(self):

        self.status = 'running'
        # Your exporting stuff goes here ...
        for _ in range(100):
            time.sleep(1)
            self.progress += 1

        self.output['final'] = "dsadasd"
        self.status = 'finished'

    def delay_start(self, sleep_time):
        time.sleep(sleep_time)
        self.run()

