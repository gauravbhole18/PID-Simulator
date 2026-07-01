from plant import TemperaturePlant


class Simulator:
    def __init__(self):
        self.plant = TemperaturePlant()
        self.dt = 0.1  # Time step for simulation
        self.simulation_time = 10  # Total simulation time
        self.heater_power = 100  # Power of the heater

    def run(self):
        times = [0]
        temperatures = [self.plant.temperature]
        for step in range(int(self.simulation_time/self.dt)):
            current_time = (step + 1) * self.dt
            self.plant.update(self.heater_power, self.dt)
            times.append(current_time)
            temperatures.append(self.plant.temperature)

        return times, temperatures