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

# Example function: f(x) = x^2
def f(x):
    return x ** 2

if __name__ == "__main__":
    calc_tool = CalcTool(f)

    # Get user input for differentiation
    try:
        x_diff = float(input("Enter the point at which to differentiate (e.g., 2): "))
        print("Derivative at x =", x_diff, ":", calc_tool.differentiate(x_diff))

        # Get user input for integration
        a = float(input("Enter the lower bound of integration (e.g., 0): "))
        b = float(input("Enter the upper bound of integration (e.g., 3): "))
        print("Integral from", a, "to", b, ":", calc_tool.integrate(a, b))

    except ValueError:
        print("Please enter valid numerical values.")
