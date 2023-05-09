# 412. Fizz Buzz
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return ['FizzBuzz' if el%15==0 else 'Fizz' if el%3==0 else 'Buzz' if el%5==0 else str(el) for el in range(1, n+1)]
