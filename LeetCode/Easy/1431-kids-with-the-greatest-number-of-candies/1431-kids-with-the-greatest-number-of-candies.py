class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        sum_candy = []
        result = []

        for candy in candies:
            sum_candy.append(candy + extraCandies)

        max_candy = max(candies)

        for i in range(len(sum_candy)):
            if sum_candy[i] >= max_candy:
                result.append(True)
            else:
                result.append(False)

        return result