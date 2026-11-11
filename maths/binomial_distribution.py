"""For more information about the Binomial Distribution -
https://en.wikipedia.org/wiki/Binomial_distribution"""

from decimal import Decimal, getcontext
from math import factorial

getcontext().prec = 20  # Using decimal library for float precision


def binomial_distribution(successes: int, trials: int, prob: float) -> float:
    """
    Return probability of k successes out of n tries, with p probability for one
    success

    The function uses the factorial function in order to calculate the binomial
    coefficient

    >>> binomial_distribution(3, 5, 0.7)
    0.3087
    >>> binomial_distribution (2, 4, 0.5)
    0.375
    >>> binomial_distribution(85, 171, 0.5)
    0.06075
    """
    if successes > trials:
        raise ValueError("""successes must be lower or equal to trials""")
    if trials < 0 or successes < 0:
        raise ValueError("the function is defined for non-negative integers")
    if not isinstance(successes, int) or not isinstance(trials, int):
        raise ValueError("the function is defined for non-negative integers")
    if not 0 < prob < 1:
        raise ValueError("prob has to be in range of 1 - 0")
    probability = Decimal((prob**successes) * ((1 - prob) ** (trials - successes)))
    # Calculate the binomial coefficient: n! / k!(n-k)!
    coefficient = Decimal(factorial(trials))
    coefficient /= Decimal(factorial(successes) * factorial(trials - successes))
    # Round to 5 decimal places and cast back into float
    return float((probability * coefficient).quantize(Decimal("0.00001")))


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    print("Probability of 2 successes out of 4 trials")
    print("with probability of 0.75 is:", end=" ")
    print(binomial_distribution(2, 4, 0.75))
