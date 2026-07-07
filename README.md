# PID Controller Simulator

An interactive PID (Proportional–Integral–Derivative) controller simulator built in Python with a desktop GUI. This project demonstrates the fundamentals of closed-loop control systems through real-time simulation and visualization.

The simulator models a first-order temperature control system and allows users to tune PID gains interactively while observing the system response.

---

## Features

- Interactive GUI built using **CustomTkinter**
- Adjustable PID gains
  - Proportional (Kp)
  - Integral (Ki)
  - Derivative (Kd)
- Adjustable temperature setpoint
- First-order temperature plant simulation
- Step response simulation
- Real-time visualization of:
  - Temperature response
  - Controller output
  - Error
  - P, I and D contributions
- Modular project architecture
- Git version control throughout development

---

## Demo

### PID Controller GUI

> *(Add a screenshot here)*

```
docs/images/gui.png
```

---

## System Architecture

```
            +------------------+
            |      GUI         |
            | (CustomTkinter)  |
            +--------+---------+
                     |
                     v
            +------------------+
            |    Simulator     |
            +--------+---------+
                     |
         +-----------+------------+
         |                        |
         v                        v
+------------------+      +----------------+
| PID Controller   | ---> | Temperature    |
|                  | <--- | Plant Model    |
+------------------+      +----------------+
                     |
                     v
             Simulation Results
                     |
                     v
               Matplotlib Plots
```

---

## Project Structure

```
PID-Simulator/
│
├── src/
│   ├── app.py             # GUI
│   ├── main.py            # Application entry point
│   ├── simulator.py       # Simulation loop
│   ├── pid.py             # PID controller
│   ├── plant.py           # Temperature plant model
│   ├── plotter.py         # Plot generation
│   └── config.py          # Configuration constants
│
├── docs/
├── requirements.txt
├── README.md
└── LICENSE
```

---

## Simulation Model

The simulator models a simple first-order thermal system.

The plant temperature is updated every simulation step using:

```
Heating - Cooling
```

where

- Heating is proportional to heater power.
- Cooling is proportional to the difference between the current temperature and room temperature.

---

## PID Controller

The controller computes

```
Output = P + I + D
```

where

### Proportional

```
P = Kp × Error
```

### Integral

```
I = Ki × ∫Error dt
```

### Derivative

```
D = Kd × d(Error)/dt
```

The controller output is limited between **0%** and **100%** heater power.

---

## GUI Controls

The simulator provides sliders for:

- Kp
- Ki
- Kd
- Temperature Setpoint

After selecting the desired gains, press **Run Simulation** to generate the response.

---

## Generated Plots

The simulator displays four plots:

### Temperature Response

Shows the measured temperature together with the desired setpoint.

### Controller Output

Displays the heater power commanded by the PID controller.

### Error

Shows the difference between the setpoint and measured temperature.

### PID Contributions

Visualizes the contribution of the

- Proportional term
- Integral term
- Derivative term

during the simulation.

---

## Installation

Clone the repository

```bash
git clone https://github.com/gauravbhole18/PID-Simulator.git
```

Go into the project

```bash
cd PID-Simulator
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python src/main.py
```

---

## Technologies Used

- Python
- CustomTkinter
- Matplotlib
- Object-Oriented Programming
- Git
- GitHub

---

## Learning Objectives

This project was built to gain practical experience with

- PID control
- Closed-loop systems
- Control system visualization
- Desktop GUI development
- Simulation architecture
- Software engineering best practices

---

## Future Improvements

- Derivative on measurement
- Integral anti-windup
- Sensor noise simulation
- Derivative filtering
- Controller comparison mode (P / PI / PID)
- Live tuning without pressing Run
- Export simulation data to CSV
- Automatic PID tuning
- Support for additional plant models
- Performance metrics
  - Rise time
  - Overshoot
  - Settling time
  - Steady-state error

---

## License

This project is licensed under the MIT License.

---

## Author

**Gaurav Bhole**

GitHub: https://github.com/gauravbhole18