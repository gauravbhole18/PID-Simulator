from config import ( ROOM_TEMPERATURE, 
                    HEATING_CONSTANT, 
                    COOLING_CONSTANT, 
                    INITIAL_TEMPERATURE,
                    )

class TemperaturePlant:
    def __init__(self):
        self.room_temperature = ROOM_TEMPERATURE
        self.heating_constant = HEATING_CONSTANT
        self.cooling_constant = COOLING_CONSTANT

        self.temperature = INITIAL_TEMPERATURE  # Initial temperature of the plant

       

      

    def update(self, heater_power, dt):
        heating = heater_power * self.heating_constant 
        cooling = (self.temperature - self.room_temperature) * self.cooling_constant
        temperature_change = heating - cooling
        self.temperature += temperature_change * dt

    
        