class PIDController:
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd


        self.prev_error = 0
        self.integral = 0

    def compute(self, setpoint, measured_value, dt):
        error = setpoint - measured_value
        p = self.kp * error
        self.integral+= error * dt
        i = self.ki * self.integral

        d = self.kd * ((
            error - self.prev_error )/ dt)
        self.prev_error = error
        output_signal = p + i + d
        output_signal = max(0, min(100, output_signal))  # Clamp output to [0, 100]

        return output_signal, p, i, d