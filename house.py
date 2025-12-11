class HousePark:
    lastname = "박"

    def __init__(self, name):
        self.fullnanme = self.lastname + name

    def travel(self, where):
        print("%s, %s 여행을 가다." % (self.fullnanme, where))

    def love(self, other):
        print("%s, %s 사랑에 빠졌네." % (self.fullnanme, other.fullnanme))

    def fight(self, other):
        print("%s, %s 싸우네" % (self.fullnanme, other.fullnanme))
    def __add__(self, other):
        print("%s, %s 결혼했네" % (self.fullnanme, other.fullnanme))

    def __sub__(self, other):
        print("%s, %s 이혼했네" % (self.fullnanme, other.fullnanme))

class HouseKim(HousePark):
    lastname = "김"

    def travel(self, where, day):
        print("%s, %s 여행 %d일 가네" % (self.fullnanme, where, day))

pey = HousePark("응용")
juliet = HouseKim("줄리엣")
pey.travel("부산")
juliet.travel("부산", 3)
pey.love(juliet)
pey + juliet
pey.fight(juliet)
pey - juliet