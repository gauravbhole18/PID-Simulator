# config.py

# ==========================
# Simulation
# ==========================

SIMULATION_TIME = 20.0      # seconds
DT = 0.1                    # simulation time step

# ==========================
# Plant
# ==========================

ROOM_TEMPERATURE = 20.0      # °C
INITIAL_TEMPERATURE = 20.0   # °C

HEATING_CONSTANT = 0.8
COOLING_CONSTANT = 0.03

# ==========================
# Controller
# ==========================

KP = 2.0
KI = 0.5
KD = 0.1

# ==========================
# Setpoint
# ==========================

INITIAL_SETPOINT = 20.0      # °C
FINAL_SETPOINT = 100.0       # °C
STEP_TIME = 5.0              # seconds

# ==========================
# Actuator
# ==========================

MIN_HEATER_POWER = 0.0
MAX_HEATER_POWER = 100.0