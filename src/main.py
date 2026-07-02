from plant import TemperaturePlant
from simulator import Simulator
import matplotlib.pyplot as plt
from plotter import Plotter
from pid import PIDController

kp = 2.0
ki = 0
kd = 0
simulator = Simulator(kp=kp, ki=ki, kd=kd)

results= simulator.run()
plotter = Plotter()
plotter.plot(results)


# plt.plot(times, temperatures, label="Temperature (°C)")
# plt.plot(times, heater_powers, label="Heater Power (%)")

# plt.title("Temperature Vs Time Simulation")
# plt.xlabel("Time (s)")  
# plt.ylabel("Temperature (°C)")
# plt.grid()
# plt.legend()
# plt.show()

# plant = TemperaturePlant()

# print(f"Initial temperature: {plant.temperature} °C")
# print(f"Room temperature: {plant.room_temperature} °C")
# print(f"Heating constant: {plant.heating_constant}")
# print(f"Cooling constant: {plant.cooling_constant}")

# heating_power = 100
# dt = 0.1

# sim_time = 10

# for step in range(20):
#     plant.update(heating_power, dt)
#     print(f"Time: {(step +1) * dt:.1f} s, Temperature: {plant.temperature:.2f} °C")