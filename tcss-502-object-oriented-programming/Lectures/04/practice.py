# Exceptions

# Iterator

# List Comprehension

# Observable
class Observer:
    def __init__(self, observable, id):
        self.observable = observable
        self.id = id

    def update(self, data):
        print(F"{self.id} received message: {data}")
    
    def notify(self, message):
        self.observable.notify(message)

    def change_data(self, data):
        self.data = data
        self.observable.notify(data)

class Observable:
    def __init__(self):
        self.observers = []
        self.data = None

    def register(self, observer):
        self.observers.append(observer)

    def unregister(self, observer):
        self.observers.remove(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)
    
    def attach(self, observer):
        self.observers.append(observer)
        
station = Observable()
worker1 = Observer(station, "worker1")
worker2 = Observer(station, "worker2")
station.attach(worker1)
station.attach(worker2)

worker1.change_data("Hello")