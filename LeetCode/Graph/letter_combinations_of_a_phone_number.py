class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index, path):
            # 입력한 숫자의 길이와 만들어진 문자열의 길이가 같으면
            if len(path) == len(digits):
                result.append(path)
                return

            # 인덱스부터 입력한 숫자의 길이만큼 반복하면서
            # 입력한 숫자의 i번째 자리에 해당하는 번호의 문자를 경로에 추가하며 DFS 탐색
            for i in range(index, len(digits)):
                for j in dic[digits[i]]:
                    dfs(i + 1, path + j)

        # 입력한 숫자가 없는 경우 예외처리
        if not digits:
            return []

        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
               "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = []
        dfs(0, "")

        return result
