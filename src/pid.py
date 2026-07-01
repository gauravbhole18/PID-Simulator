class PController:
    def __init__(self, kp):
        self.kp = kp
    
    def compute(self, setpoint, measured_value):
        error = setpoint - measured_value
        output_signal = self.kp * error
        output_signal = max(0, min(100,output_signal))  # Clamp output to [0, 100]
        
        return output_signal