from plant import TemperaturePlant
from pid import PIDController
from config import ( KP,
                     KI,
                    KD,
                    SIMULATION_TIME,
                    DT
                    )




class Simulator:
    def __init__(self, kp, ki, kd):
        self.controller = PIDController(kp=kp, ki=ki, kd=kd)  # PID gains
        self.setpoint = 100.0  # Desired temperature
        self.plant = TemperaturePlant()
        self.dt = DT  # Time step for simulation
        self.simulation_time = SIMULATION_TIME  # Total simulation time
        # self.heater_power = 100  # Power of the heater
        

    def run(self):
        times = [0.0]
        temperatures = [self.plant.temperature]
        heater_powers = [0.0]
        p_values = [0.0]
        i_values = [0.0]
        d_values = [0.0]
        errors = [self.setpoint - self.plant.temperature]
        for step in range(int(self.simulation_time/self.dt)):
            current_time = (step + 1) * self.dt
            heater_power, p, i,d = self.controller.compute(self.setpoint, self.plant.temperature, self.dt)
            self.plant.update(heater_power, self.dt)
            times.append(current_time)
            temperatures.append(self.plant.temperature)
            heater_powers.append(heater_power)
            errors.append(self.setpoint - self.plant.temperature)   
            p_values.append(p)
            i_values.append(i)
            d_values.append(d)

        return {
           "times": times,
           "temperatures": temperatures,
           "heater_powers": heater_powers,
           "p_values": p_values,
           "i_values": i_values,
           "d_values": d_values,
           "errors": errors,
           "setpoint": self.setpoint
        }