import numpy as np

class CalcTool:
    def __init__(self, func, delta=1e-5):
        """
        func : function
            The function to be differentiated or integrated.
        delta : float
            Step size for numerical differentiation.
        """
        self.func = func
        self.delta = delta

    def differentiate(self, x):
        """
        Calculate the numerical derivative of the function at a given point x.
        
        Parameters:
        x : float
            The point at which to differentiate.
        
        Returns:
        float : The derivative at point x.
        """
        return (self.func(x + self.delta) - self.func(x - self.delta)) / (2 * self.delta)

    def integrate(self, a, b, n=1000):
        """
        Calculate the numerical integral of the function from a to b using the trapezoidal rule.
        
        Parameters:
        a : float
            Lower bound of integration.
        b : float
            Upper bound of integration.
        n : int
            Number of divisions (more divisions increases accuracy).
        
        Returns:
        float : The integral from a to b.
        """
        x = np.linspace(a, b, n+1)
        y = self.func(x)
        return np.trapz(y, x)

# Example usage
if __name__ == "__main__":
    # Example function: f(x) = x^2
    def f(x):
        return x ** 2

    calc_tool = CalcTool(f)

    # Differentiate at x = 2
    print("Derivative at x=2:", calc_tool.differentiate(2))

    # Integrate from 0 to 3
    print("Integral from 0 to 3:", calc_tool.integrate(0, 3))
