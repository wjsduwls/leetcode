from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = []
        num_dict = Counter(nums).most_common(k)
        for i in range(len(num_dict)):
            answer.append(num_dict[i][0])
        return answer
        #numbers = sorted(num_dict.items(), key = lambda x:x[1], reverse = True)
        #for i in range(len(numbers)):
            #if numbers[i][1] >= k:
                #answer.append(numbers[i][0])
        