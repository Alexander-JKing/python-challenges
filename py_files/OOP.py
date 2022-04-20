###############################
# 1
###############################

"""class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.employed = True


person_1 = Person('Alex', 25)
person_1.employed = False
print(person_1.employed)"""

###############################
# 2
###############################


"""class MobilePhone:
    def __init__(self, display_size, ram, os):
        self.display_size = display_size
        self.ram = ram
        self.os = os


pearphone = MobilePhone(5.5, "3GB", "yOS 11.2")
simsun = MobilePhone(5.4, "4GB", "Cyborg 8.1")

print(f"The new Pear phone has a {pearphone.display_size} display size"
      f"{pearphone.ram} of RAM and runs on"
      f"the latest version of {pearphone.os}"
      f"Its biggest competitor is the Simsun phone "
      f"which sports a similar AMOLED {simsun.display_size}")"""

###############################
# 3
###############################
"""import math


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def circumference_calculate(self):
        circumference = 2 * math.pi * self.radius
        return circumference

    def circle_area(self, ):
        area = math.pi * self.radius * self.radius
        return area

# Before calling class methods, you must first makes sure that whatever you are calling the class method on, such as
# the below radius_ variable which we get from the user, is a Class object itself first. Here we instantiate the user-
# input into a radius_ Class object, then call the method on it.

x = False
while x is False:
    radius_ = Circle(float(input("Please enter a radius: ")))
    print("Circumference = ", Circle.circumference_calculate(radius_))
    print("Area = ", Circle.circle_area(radius_))
    opt_out = input("Would you like to opt out? (yes/no): ")
    if opt_out.lower() == 'yes':
        x = True
    elif opt_out.lower() == 'no':
        pass
    else:
        pass"""

###############################
# 4
###############################

"""
class WebBrowser:

    connected = True
    number_of_browsers = 0

    def __init__(self, page):
        self.current_page = page
        self.history = [page]
        self.is_incognito = False
        WebBrowser.number_of_browsers += 1
        
        # We have added a method to the initialiser, which determines the attributes of all instances/objects.
        # Here the method will update by one every time a new instance is created.
        # Therefore the Class attribute 'number_of_browsers' will get updates each time.


print(WebBrowser.number_of_browsers)

firefox = WebBrowser("google.com")
chrome = WebBrowser("facebook.com")
print(WebBrowser.number_of_browsers)"""

###############################
# 5
###############################
'''Safety mechanism in elevator for when past capacity
maximum occupancy = 8
elevator should be initailised with the number of occupants.
if limit exceeded, print error warning'''


"""class Elevator:

    occupancy_limit = 8

    def __init__(self, occupants):
        self.occupants = occupants
        if self.occupants > self.occupancy_limit:
            self.overhaul = self.occupants - self.occupancy_limit
            print("ERROR -- Please number: {} step of:".format(self.overhaul))
        else:
            print("Appropriate number of passengers")


elevator1 = Elevator(6)
print(elevator1.occupants)

print()

elevator2 = Elevator(5)
print(elevator2.occupants)

print()

elevator3 = Elevator(23)
print(elevator3.occupants)"""


###############################
# 6
###############################


"""class WebBrowser:

    connected = True
    number_of_browsers = 0
    geo_coordinates = {"lat": -4.764813, "lng": 16.131331}

    def __init__(self, page):
        self.current_page = page
        self.history = [page]
        self.is_incognito = False
        WebBrowser.number_of_browsers += 1

    def navigate(self, new_page):
        self.current_page = new_page
        if self.is_incognito is False:
            self.history.append(new_page)

    def clear_history(self, page_history):
        self.history.clear()
        self.history.append(self.current_page)

    @classmethod
    def change_coordinates(cls, new_coordinates):
        if new_coordinates["lat"] > 90 or new_coordinates["lat"] < -90:
            print("Invalid values for latitude. Should be within the range from -90 to 90 degrees")
            return None
        if new_coordinates['lng'] > 180 or new_coordinates['lng'] < -180:
            print("Invalid value for longitude. Should be within range of -180 to 180 degrees")
            return None
        cls.geo_coordinates = new_coordinates

    @classmethod
    def with_incognito(cls, page):
        instance = cls(page)
        instance.is_incognito = True
        instance.history = []
        return instance


firefox = WebBrowser("google.com")
chrome = WebBrowser("facebook.com")

vivaldi = WebBrowser("gocampaign.org")
print(vivaldi.current_page)

vivaldi.navigate("reddit.com")
print(vivaldi.current_page)
print(vivaldi.history)

vivaldi.clear_history(vivaldi.history)
print("Vivaldi history: ", vivaldi.history)
print("Firefox history: ", firefox.history)

print("Class orginal coordinates: ", WebBrowser.geo_coordinates)
print("Firefox original Coordinates: ", firefox.geo_coordinates)
print()
firefox.geo_coordinates = {"lat": -45.34234, "lng": 23.85948}
print("Firefox changed Coordinates: ", firefox.geo_coordinates)
WebBrowser.geo_coordinates = {"lat": 23.81293, "lng": 86.38493}
print("Class changed coordinates: ", WebBrowser.geo_coordinates)
print("Firefox original Coordinates: ", firefox.geo_coordinates)"""


###############################
# 7
###############################

'''Create a MusicPlayer Class,
Create a play() method, which sets the first track from the list of tracks as currently playing
THe list of tracks should be a private attribute
Additionally, it should have a firmware attribute and a firmware method to update the firmware'''


"""class MusicPlayer:

    def __init__(self):
        self.track = ""
        self.__track_list = ["Moonage Daydream", "Starman", "Life on Mars"]
        self.firmware = 1.0

    def play(self):
        current_track = self.__track_list[0]
        return current_track

    def list_tracks(self):
        return self.__track_list

    def update_firmware(self, new_firmware):
        if new_firmware > self.firmware:
            new_firmware = self.firmware
        else:
            return self.firmware
        return new_firmware


player1 = MusicPlayer()
for i in player1.list_tracks():
    print(i)"""


###############################
# 8
###############################
''' Define a Cat Class, from which we'll derive other big cats,
the class will have the methods vocalise and print_facts
and the attributes lifespan, mass, and speed.'''


"""class Cat:

    def __init__(self, mass, lifespan, speed):
        self.mass_in_kg = mass
        self.lifespan_in_years = lifespan
        self.speed_in_km = speed

    def vocalise(self):
        print("Chuff")

    def __str__(self):
        print(f"The {type(self).__name__.lower()} "
              f"weighs {self.mass_in_kg} kg, "
              f"has a lifespan of {self.lifespan_in_years} years and "
              f"can run at a maximum speed of {self.speed_in_km} kph"
              f"")


cat = Cat(34, 8, 23)
# cat.vocalise()
# cat.print_facts()


class Cheetah(Cat):

    def __init__(self, mass, lifespan, speed):
        super().__init__(mass, lifespan, speed)
        self.spotted_coat = True

    def vocalise(self):
        print("Chirrup")


class Lion(Cat):

    def __init__(self, mass=190, lifespan=14, speed=14):
        super().__init__(mass, lifespan, speed)
        self.is_social = True

    def vocalise(self):
        print("Roar")


class Leopard(Cat):
    def vocalise(self):
        print("Roar")


cheetah = Cheetah(12, 67, 45)
print(cheetah.mass_in_kg)
lion = Lion()
leopard = Leopard(34, 67, 89)
leopard.vocalise()


class Tiger(Cat):

    def __init__(self, mass=310, lifespan=26, speed=65):
        super().__init__(mass, lifespan, speed)
        self.coat_pattern = 'striped'

    def __str__(self):
        facts = super().__str__()
        facts = "{}, it also has a {} coat pattern ".format(facts, self.coat_pattern)
        return facts

    def vocalise(self):
        print("ROAR")

    def swim(self):
        print("Splash, splash")


tiger = Tiger()
print()
print("---------------")
print(tiger)


class Liger(Lion, Tiger):
    pass


liger = Liger()
print("Is it social:", liger.is_social, "...and what coat does it have: ", liger.coat_pattern)"""


###############################
# 9
###############################


''' Create a Class called Camera,
Create a Class called MobilePhone
These will be the Base/Super classes of a Class called CameraPhone
The CameraPhone Class should be initialised with the memory attribute and should have a take_picture() method,
which prints out the message say cheese!'''


class Camera:

    def take_picture(self):
        print("SAY CHEESE!")


class MobilePhone:

    def __init__(self, memory="32GB"):
        self.memory = memory


class CameraPhone(Camera, MobilePhone):
    pass


camera_phone = CameraPhone()
print(camera_phone.memory)
camera_phone.take_picture()




