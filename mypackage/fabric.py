class Tesla:
    # WRITE YOUR CODE HERE
    def __init__(self, model: str, color: str, autopilot: bool = False, seats_count: int = 5, is_locked: bool = True, battery_charge: float = 99.9, efficiency: float = 0.3):
        self.__model = model
        self.__color = color
        self.__autopilot = autopilot
        self.__battery_charge = battery_charge
        self.__is_locked = is_locked
        self.__seats_count = seats_count
        self.__efficiency = efficiency

    @property
    def color(self) -> str:
      return self.__color

    @property
    def autopilot(self) -> str:
      return self.__autopilot

    @property
    def seats_count(self) -> int:
      return self.__seats_count
  
    @property
    def is_locked(self) -> bool:
      return self.__is_locked

    @property
    def battery_charge(self) -> int:
      return self.__battery_charge

    @color.setter
    def color(self, new_color: str) -> None:
      self.__color = new_color

    @autopilot.setter
    def autopilot(self, autopilot: bool) -> None:
      self.__autopilot = autopilot

    @seats_count.setter
    def seats_count(self, seats: int) -> None:
      if(seats < 2):
        return "Seats count cannot be lower than 2!"
      self.__seats_count = seats

    @is_locked.setter
    def is_locked(self) -> None:
      self.is_locked = True

    def autopilot(self, obsticle: str) -> str:
      '''
      Takes in an obsticle object as string, returns string information about successfully avoiding the object or string information about availability of autopilot.

          Parameters:
                  obsticle (str): An real world object that needs to be manuverd
                    
          Returns:
                  success (str): String informing about avoided obsticle
                  fail (str): String warning that the car does not have autopilot
      '''
      if self.__autopilot:
        return f"Tesla model {self.__model} avoids {obsticle}"
      return "Autopilot is not available"
    
    #unlocking car
    def unlock(self) -> None:
      self.__is_locked = False

    # opening doors
    def open_doors(self) -> str:
      '''
      Returns string information about opening the doors of the car.

          Parameters:
                  None
          Returns:
                  success (str): String informing that the doors are opening
                  fail (str): String warning that the car is locked
      '''
      if(self.__is_locked):
        return "Car is locked!"
      return "Doors opens sideways"
    
    # checking battery
    def check_battery_level(self) -> str:
      return f"Battery charge level is {self.__battery_charge}%"

    # charging battery
    def charge_battery(self) -> None:
      self.__battery_charge = 100

    # driving the car
    def drive(self, travel_range: float):
      '''
      Takes in the travel distance number, returns remaining battery life or not enough battery warning.

          Parameters:
                  travel_range (float): A float number
                    
          Returns:
                  battery_charge_level (str): String informing about remaining battery life
                  String warning (str): String warning that there is not enough battery to complete the travel distance
      '''
      battery_discharge_percent = travel_range * self.__efficiency
      # COMPLETE THE FUNCTION
      if self.__battery_charge - battery_discharge_percent >= 0:
        self.__battery_charge = self.__battery_charge - battery_discharge_percent
        return self.check_battery_level()
      else:
        return "Battery charge level is too low!"

    def welcome(self) -> str:
        raise NotImplementedError
