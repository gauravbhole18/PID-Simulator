import matplotlib.pyplot as plt


class Plotter:

    def plot(self, results):

        times = results["times"]
        temperatures = results["temperatures"]
        heater_powers = results["heater_powers"]
        p_values = results["p_values"]
        i_values = results["i_values"]
        d_values = results["d_values"]
        setpoints = results["setpoints"]
        errors = results["errors"]

        # Create Figure
        fig = plt.Figure(figsize=(12, 10))

        # -----------------------------
        # Temperature Plot
        # -----------------------------
        ax1 = fig.add_subplot(4, 1, 1)

        ax1.plot(times, temperatures, label="Temperature")
        ax1.plot(times, setpoints, "--", label="Setpoint")

        ax1.set_title("Temperature Response")
        ax1.set_ylabel("Temperature (°C)")
        ax1.grid(True)
        ax1.legend()

        # -----------------------------
        # Heater Output
        # -----------------------------
        ax2 = fig.add_subplot(4, 1, 2)

        ax2.plot(times, heater_powers)

        ax2.set_title("Controller Output")
        ax2.set_ylabel("Heater (%)")
        ax2.grid(True)

        # -----------------------------
        # Error
        # -----------------------------
        ax3 = fig.add_subplot(4, 1, 3)

        ax3.plot(times, errors)

        ax3.set_title("Error")
        ax3.set_ylabel("°C")
        ax3.grid(True)

        # -----------------------------
        # PID Contributions
        # -----------------------------
        ax4 = fig.add_subplot(4, 1, 4)

        ax4.plot(times, p_values, label="P")
        ax4.plot(times, i_values, label="I")
        ax4.plot(times, d_values, label="D")

        ax4.set_title("PID Contributions")
        ax4.set_xlabel("Time (s)")
        ax4.set_ylabel("Output")
        ax4.grid(True)
        ax4.legend()

        fig.tight_layout()

        return fig