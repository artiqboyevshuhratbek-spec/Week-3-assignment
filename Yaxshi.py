class Thermostat:
    min_temp = 15.0
    max_temp = 30.0
    device_count = 0
    def __init__(self, location, initial_temp):
        self.location = location
        self.readings = []
        Thermostat.device_count += 1
        if initial_temp < Thermostat.min_temp:
            print("Initial temperature out of range. Set to minimum.")
            self.current_temp = Thermostat.min_temp
        elif initial_temp > Thermostat.max_temp:
            print("Initial temperature out of range. Set to maximum.")
            self.current_temp = Thermostat.max_temp
        else:
            self.current_temp = initial_temp
            print(f"Temperature set to {self.current_temp}°C")
        self.readings.append(self.current_temp)
    def set_temperature(self, new_temp):
        if new_temp < Thermostat.min_temp or new_temp > Thermostat.max_temp:
            print(f"Temperature {new_temp}°C is out of allowed range ({Thermostat.min_temp}-{Thermostat.max_temp})")
        else:
            self.current_temp = new_temp
            self.readings.append(new_temp)
            print(f"Temperature set to {new_temp}°C")
    def get_average_temp(self):
        if not self.readings:
            return 0.0
        return sum(self.readings) / len(self.readings)
    def display_status(self):
        print(f"Thermostat in {self.location}: {self.current_temp}°C")
        print(f"Reading count: {len(self.readings)}")
        print(f"Average temperature: {self.get_average_temp()}°C")
    def is_comfortable(self):
        return 20.0 <= self.current_temp <= 25.0
t1 = Thermostat("Living Room", 22.0)
t2 = Thermostat("Garage", 10.0)
t1.set_temperature(26.5)
t1.set_temperature(35.0)
t1.display_status()
t2.display_status()
print(t1.is_comfortable())
print(Thermostat.device_count)