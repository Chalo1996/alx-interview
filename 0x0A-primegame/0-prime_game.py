#!/usr/bin/python3
"""The Game Module."""


def isWinner(x, nums):
    """
    isWinner: A function that determines if a player is the winner.

    Args:
        x (int): The number of rounds.
        nums (list): A list of n.

    Returns:
        str: The name of the player that won the most rounds.
            If the winner cannot be determined, return None.
    """
    def filterNums(n):
        """filterNums: A function that filters the list of n."""
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False

        return [i for i in range(2, n + 1) if primes[i]]

    def game(n):
        """
        game: A function that determines if a player is the winner.
        """
        primes = filterNums(n)
        nums = set(range(1, n + 1))
        while nums and primes:
            for p in primes:
                multiples = set(range(p, n + 1, p))
                nums -= multiples
                if not nums:
                    return "Ben"
                primes = [q for q in primes if q not in multiples]
                if not primes:
                    return "Maria"

    winners = [game(n) for n in nums]
    maria_wins = winners.count("Maria")
    ben_wins = winners.count("Ben")
    if maria_wins > ben_wins:
        return "Ben"
    elif ben_wins > maria_wins:
        return "Maria"
    else:
        return None
