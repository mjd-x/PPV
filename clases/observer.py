class Subscriber:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print('{} got the message "{}"'.format(self.name, message))


class Publisher:
    def __init__(self):
        self.subscribers = set()  # para que no me deje suscribirlo mas de una vez

    def register(self, who):
        self.subscribers.add(who)

    def unregister(self, who):
        self.subscribers.discard(who)

    def dispatch(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message)


pub = Publisher()

bob = Subscriber("Bob")
alice = Subscriber("Alice")
john = Subscriber("John")

pub.register(bob)
pub.register(bob)
pub.register(bob)
pub.register(alice)
pub.register(john)

pub.dispatch("It's lunchtime!")

pub.unregister(john)

pub.dispatch("It's time for dinner!")