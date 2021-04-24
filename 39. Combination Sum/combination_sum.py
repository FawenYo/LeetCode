import pathlib
import sys

folder_path = str(pathlib.Path(__file__).parent.absolute())

sys.path.append(".")
from check import Check
from model import *


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = self.dfs(candidates=candidates, path=[], result=[], target=target)
        return result

    def dfs(
        self,
        candidates: List[int],
        path: List[int],
        result: List[List[int]],
        target: int,
    ):
        if target < 0:
            return None
        if target == 0:
            result.append(path)

        for i in range(len(candidates)):
            new_candidates = candidates[i:]
            new_path = path + [candidates[i]]
            new_target = target - candidates[i]
            # No more result
            if new_target < 0:
                break
            self.dfs(
                candidates=new_candidates,
                path=new_path,
                result=result,
                target=new_target,
            )
        return result


if __name__ == "__main__":
    Check().run_code(solution=Solution(), test_data_path=f"{folder_path}/test_data.txt")
