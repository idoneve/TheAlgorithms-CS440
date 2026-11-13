"""For more information about the Binomial Distribution -
https://en.wikipedia.org/wiki/Binomial_distribution"""

from decimal import MAX_EMAX, MIN_EMIN, Context, Decimal, localcontext
from math import factorial


def binomial_distribution(successes: int, trials: int, prob: float) -> float:
    """
    Return probability of k successes out of n tries, with p probability for one
    success

    The function uses the factorial function in order to calculate the binomial
    coefficient

    >>> binomial_distribution(3, 5, 0.7)
    0.30870000000000003
    >>> binomial_distribution (2, 4, 0.5)
    0.375
    """
    if successes > trials:
        raise ValueError("""successes must be lower or equal to trials""")
    if trials < 0 or successes < 0:
        raise ValueError("the function is defined for non-negative integers")
    if not isinstance(successes, int) or not isinstance(trials, int):
        raise ValueError("the function is defined for non-negative integers")
    if not 0 < prob < 1:
        raise ValueError("prob has to be in range of 1 - 0")
    # Calculate the binomial coefficient: n! / k!(n-k)!
    coefficient = factorial(trials) // (
        factorial(successes) * factorial(trials - successes)
    )
    with localcontext(Context(prec=50, Emin=MIN_EMIN, Emax=MAX_EMAX)):
        probability = Decimal(prob)
        return float(
            coefficient
            * probability**successes
            * (1 - probability) ** (trials - successes)
        )


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    print("Probability of 2 successes out of 4 trials")
    print("with probability of 0.75 is:", end=" ")
    print(binomial_distribution(2, 4, 0.75))
