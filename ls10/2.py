class Car:
    def __init__(self, mark):
        self.mark = mark

    def start(self):
        print("Заводим двигатель")
    def stop(self):
        print("Отключить двигатель")
    class Move:
        def front(self): print("Вперед")
        def back(self): print("Назад")

    move = Move()

bmw = Car("BMW")
nissan = Car("NISSAN")
print(bmw.mark)
print(nissan.mark)
bmw.start()
bmw.stop()
bmw.move.front()
bmw.move.back()