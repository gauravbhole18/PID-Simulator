from simulator import Simulator
from plotter import Plotter
from config import ( KP,
                     KI,
                     KD,
                     )


simulator = Simulator(kp=KP, ki=KI, kd=KD)

results= simulator.run()
plotter = Plotter()
plotter.plot(results)
