class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0
        prime = [True]*n
        prime[0]=prime[1]=False
        i=2
        for i in range(2,math.isqrt(n)+1):
            if prime[i]:
                for j in range(i*i,n,i):
                    prime[j]=False
        return sum(prime)
        
        # if n <= 2:
        #     return 0
        # primes = [True] * n
        # primes[0] = primes[1] = False 
        
        # for number in range(2, n):
        #     if primes[number]:
        #         for multiple in range(2 * number, n, number):
        #             primes[multiple] = False
        # return sum(primes)