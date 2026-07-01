from plant import TemperaturePlant
from simulator import Simulator
import matplotlib.pyplot as plt

from pid import PController


simulator = Simulator()

times, temperatures, heater_powers = simulator.run()

plt.plot(times, temperatures, label="Temperature (°C)")
plt.plot(times, heater_powers, label="Heater Power (%)")

plt.title("Temperature Vs Time Simulation")
plt.xlabel("Time (s)")  
plt.ylabel("Temperature (°C)")
plt.grid()
plt.legend()
plt.show()

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