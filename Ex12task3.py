import random


class Pet:
    boredom_decrement = 4
    hunger_decrement = 6
    boredom_threshold = 5
    hunger_threshold = 10
    sounds = ["auf"]
    
    def __init__(self, name="Max", speed=1):
        self.name = name
        self.speed = speed
        self.hunger = random.randrange(self.hunger_threshold)
        self.boredom = random.randrange(self.boredom_threshold)
        self.sounds = self.sounds[:]

    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "happy"
        elif self.hunger > self.hunger_threshold:
            return "hungry"
        else:
            return "bored"

    def __str__(self):
        state = "     I'm " + self.name + ". "
        state += " I feel " + self.mood() + ". "
        return state

    def hi(self):
        print(self.sounds[random.randrange(len(self.sounds))])


class Dog(Pet):
    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "happy, arf! Happy"
        elif self.hunger > self.hunger_threshold:
            return "hungry already, arrrf"
        else:
            return "bored, so you should play with me"


class Poodle(Dog):
    def dance(self):
        return "Dancin' in circles like poodles do."

    def hi(self):
        print(self.dance())
        Dog.hi(self)


class Bird(Pet):
    sounds = ["chirp"]

    def __init__(self, chirp_number=2):
        super().__init__(speed=3)
        self.chirp_number = chirp_number

    def hi(self):
        for i in range(self.chirp_number):
            print(self.sounds[random.randrange(len(self.sounds))])


class Hybrid(Bird, Poodle):
    def something_interests(self):
        greetings = self.hi and self.dance
        return greetings


dogebird = Hybrid()
print(dogebird.something_interests())
