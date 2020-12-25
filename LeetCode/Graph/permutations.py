class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        prev_elements = []

        def dfs(elements):
            # 자식 노드의 개수가 0일 때, 즉 단말 노드일 때 이전 레벨 노드 추가
            if len(elements) == 0:
                results.append(prev_elements[:])

            # 순열 생성 재귀 호출
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()

        dfs(nums)
        return results


# 반복자 생성에 최적화된 효율적인 기능을 제공하는 모듈
# 구현의 효율성, 성능을 위해 사용
import itertools


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutation(nums))
        # return list(map(list, itertools.permutations(nums))) 로 튜플 아닌 리스트 리턴
