from plant import TemperaturePlant

plant = TemperaturePlant()

print(f"Initial temperature: {plant.temperature} °C")
print(f"Room temperature: {plant.room_temperature} °C")
print(f"Heating constant: {plant.heating_constant}")
print(f"Cooling constant: {plant.cooling_constant}")

heating_power = 100
dt = 0.1

sim_time = 10

for step in range(20):
    plant.update(heating_power, dt)
    print(f"Time: {(step +1) * dt:.1f} s, Temperature: {plant.temperature:.2f} °C")