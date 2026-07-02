import matplotlib.pyplot as plt

class Plotter:
    def plot(self,results):
        times = results["times"]
        temperatures = results["temperatures"]
        heater_powers = results["heater_powers"]
        p_values = results["p_values"]
        i_values = results["i_values"]  
        d_values = results["d_values"]
        setpoints = results["setpoint"]
        errors = results["errors"]
      
      
        plt.figure(figsize=(12, 10))
        plt.subplot(4, 1, 1)

        plt.plot(times, temperatures, label="Temperature")

        # plt.axhline(
        #     setpoint,
        #     linestyle="--",
        #     label="Setpoint"
        # )

        plt.plot(
            times,
            setpoints,
            "--",
            label="Setpoint"
        )

        plt.title("Temperature Response")

        plt.ylabel("Temperature (°C)")

        plt.grid(True)

        plt.legend()
        plt.subplot(4, 1, 2)

        plt.plot(times, heater_powers)

        plt.title("Controller Output")

        plt.ylabel("Heater (%)")

        plt.grid(True)
        plt.subplot(4, 1, 3)

        plt.plot(times, errors)

        plt.title("Error")

        plt.ylabel("°C")

        plt.grid(True)

        plt.subplot(4, 1, 4)

        plt.plot(times, p_values, label="P")

        plt.plot(times, i_values, label="I")

        plt.plot(times, d_values, label="D")

        plt.title("PID Contributions")

        plt.xlabel("Time (s)")

        plt.ylabel("Output")

        plt.grid(True)

        plt.legend()

        plt.tight_layout()

        plt.show()