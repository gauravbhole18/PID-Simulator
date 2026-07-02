class TemperaturePlant:
    def __init__(self):
        self.room_temperature = 0

        self.temperature = 20.0  # Initial temperature of the plant

        self.heating_constant = 0.8

        self.cooling_constant = 0.6

    def update(self, heater_power, dt):
        heating = heater_power * self.heating_constant 
        cooling = (self.temperature - self.room_temperature) * self.cooling_constant
        temperature_change = heating - cooling
        self.temperature += temperature_change * dt

    
        