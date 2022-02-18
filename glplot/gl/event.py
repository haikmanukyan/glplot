class Event:
    def __init__(self):
        self.listeners = []
    def __add__(self, callback):
        self.listeners.append(callback)
        return self
    def __call__(self, *argv):
        for callback in self.listeners:
            callback(*argv)