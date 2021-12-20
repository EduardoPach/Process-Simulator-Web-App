import numpy as np
from scipy.integrate import odeint 
from scipy.optimize import fsolve

class CSTR:
    def __init__(self) -> None:
        pass

    def _model(self, y: float, t: np.array, *args, **kwargs) -> list[float, float]:
        C, T = y

        dCdt = False
        dTdt = False
        
        return dCdt, dTdt

    def _simulation(self) -> list[float, float]:
        pass 

    def plot_nullclines(self) -> None:
        pass



