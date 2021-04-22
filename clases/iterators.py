class MiIterable:
    def __iter__(self):
        self.indice = 1
        return self

    def __next__(self):
        if self.indice <= 20:
            x = self.indice
            self.indice += 1
            return x  # el valor a retornar del iterable
        else:
            raise StopIteration


mi_iterable = MiIterable()

for i in mi_iterable:
    print(i)
