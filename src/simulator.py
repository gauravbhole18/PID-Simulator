from plant import TemperaturePlant
from pid import PController




class Simulator:
    def __init__(self):
        self.controller = PController(kp=2.0)  # Proportional gain
        self.setpoint = 100.0  # Desired temperature
        self.plant = TemperaturePlant()
        self.dt = 0.1  # Time step for simulation
        self.simulation_time = 10  # Total simulation time
        # self.heater_power = 100  # Power of the heater
        

    def run(self):
        times = [0]
        temperatures = [self.plant.temperature]
        heater_powers = [0]
        for step in range(int(self.simulation_time/self.dt)):
            current_time = (step + 1) * self.dt
            heater_power = self.controller.compute(self.setpoint, self.plant.temperature)
            self.plant.update(heater_power, self.dt)
            times.append(current_time)
            temperatures.append(self.plant.temperature)
            heater_powers.append(heater_power)

        return times, temperatures, heater_powers