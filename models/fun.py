nums = [5]
k=1
def findMaxAverage( nums, k) -> float:
        k_sum = sum(nums[:k])
        sum_max = k_sum
        n = len(nums)
        for i in range(k,n):
            k_sum += nums[i]-nums[i-k]
            print(k_sum)
            sum_max = max(k_sum, sum_max)
        print(sum_max/k)
findMaxAverage(nums,k)
