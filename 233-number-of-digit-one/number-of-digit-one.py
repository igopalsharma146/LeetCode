class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        p = 1 
        while p <= n:
            higher = n // (p * 10)
            current = (n // p) % 10
            lower = n % p
            # print(higher,current,lower)
            if current == 0:
                count += higher * p
            elif current == 1:
                count += higher * p + lower + 1
            else:
                count += (higher + 1) * p

            p *= 10
            # print(count)
        return count


        # TLE ERROR
        # if n<1:
        #     return 0

        # def count(num):
        #     c=0
        #     while num > 0:
        #         r=num%10
        #         if r==1:
        #             c+=1
        #         num=num//10
        #     return c
        
        # res=0
        # for i in range(1,n+1):
        #     res+=count(i)
        # return res