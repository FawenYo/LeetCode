import copy
import re
from typing import Any, List

import rich.progress
from rich import console
from rich.console import Console

from model import *

console = Console()


def call_function_by_name(solution, function_name, args=[], kwargs={}) -> Any:
    return getattr(solution, function_name)(*args, **kwargs)


class Check:
    def __init__(self) -> None:
        self.test_cases: list = []
        self.function_name: str = ""
        self.inputs_args_type: List[str] = []
        self.output_args_type: str = ""

    def run_code(self, solution, test_data_path: str):
        self.load_test_data(test_data_path=test_data_path)
        self.check_answer(solution=solution)

    def load_test_data(self, test_data_path: str) -> None:
        console.print(":link: Loading testing data...")
        template = ""
        with open(test_data_path) as f:
            template = f.read()
        infos = template.split("\n")
        self.function_name = infos[0]
        args = infos[1].split("|")
        self.inputs_args_type = args[:-1]
        self.output_args_type = args[-1]
        for line_index, line_content in enumerate(infos[2::3]):
            input_values = eval(infos[2 + 3 * line_index])
            self.translate_input_type(input_values=input_values)
            output_values = infos[2 + 3 * line_index + 1]
            output_values = self.translate_output_type(output_values=output_values)

            self.test_cases.append((input_values, output_values))

        console.print(":page_with_curl: Testing data loaded.")

    def check_answer(self, solution) -> None:
        success = True
        for question_input, expected_output in rich.progress.track(
            self.test_cases, description=":rocket: Checking your code..."
        ):
            try:
                origin_question_input = copy.deepcopy(question_input)
                return_output = call_function_by_name(
                    solution=solution,
                    function_name=self.function_name,
                    args=question_input,
                )

                # ListNode
                if self.output_args_type == "ListNode":
                    return_output = listnode_to_list(listnode=return_output)
                    expected_output = listnode_to_list(listnode=expected_output)
                    if return_output == expected_output:
                        pass
                    else:
                        success = False
                        input_text = ""
                        for i in question_input:
                            input_text += f"{i}, "
                        input_text = input_text.strip(", ")
                        console.print(":x: Wrong Answer")
                        console.print(f"Input: {input_text}")
                        console.print(f"Output: {return_output}")
                        console.print(f"Expected: {expected_output}")
                        break
                # TreeNode
                elif self.output_args_type == "TreeNode":
                    return_output = treenode_to_list(treenode=return_output)
                    expected_output = treenode_to_list(treenode=expected_output)
                    if return_output == expected_output:
                        pass
                    else:
                        success = False
                        input_text = ""
                        for i in question_input:
                            input_text += f"{i}, "
                        input_text = input_text.strip(", ")
                        console.print(":x: Wrong Answer")
                        console.print(f"Input: {input_text}")
                        console.print(f"Output: {return_output}")
                        console.print(f"Expected: {expected_output}")
                        break
                # None
                elif self.output_args_type == "None":
                    return_output = question_input
                    clone_return = copy.deepcopy(return_output)
                    clone_expected = copy.deepcopy(expected_output)
                    if clone_return.sort() == clone_expected.sort():
                        pass
                    else:
                        success = False
                        input_text = ""
                        for i in origin_question_input:
                            input_text += f"{i}, "
                        input_text = input_text.strip(", ")

                        output_text = ""
                        for i in question_input:
                            output_text += f"{i}, "
                        output_text = output_text.strip(", ")

                        console.print(":x: Wrong Answer")
                        console.print(f"Input: {input_text}")
                        console.print(f"Output: {output_text}")
                        console.print(f"Expected: {expected_output}")
                        break
                # List[Any]
                elif re.findall("List\[(.*)\]", string=self.output_args_type):
                    clone_return = copy.deepcopy(return_output)
                    clone_expected = copy.deepcopy(expected_output)
                    if clone_return.sort() == clone_expected.sort():
                        pass
                    else:
                        success = False
                        input_text = ""
                        for i in question_input:
                            input_text += f"{i}, "
                        input_text = input_text.strip(", ")
                        console.print(":x: Wrong Answer")
                        console.print(f"Input: {input_text}")
                        console.print(f"Output: {return_output[0]}")
                        console.print(f"Expected: {expected_output}")
                        break
                # Others
                else:
                    if return_output == expected_output:
                        pass
                    else:
                        success = False
                        input_text = ""
                        for i in question_input:
                            input_text += f"{i}, "
                        input_text = input_text.strip(", ")
                        console.print(":x: Wrong Answer")
                        console.print(f"Input: {input_text}")
                        console.print(f"Output: {return_output[0]}")
                        console.print(f"Expected: {expected_output}")
                        break
            except:
                success = False
                console.print(":heavy_exclamation_mark: Runtime Error")
                rich.console.Console().print_exception()
                break
        if success:
            console.print(":o: All testing data accepted!")

    def translate_input_type(self, input_values: List[str]) -> None:
        for index, args_type in enumerate(self.inputs_args_type):
            temp = input_values[index]

            # Int
            if args_type == "int":
                input_values[index] = int(temp)

            # List[Any]
            list_args = re.findall("List\[(.*)\]", string=args_type)
            if list_args:
                input_values[index] = eval(temp)
                each_arg = list_args[0]
                for each_index, each_value in enumerate(eval(temp)):
                    # List[str]
                    if each_arg == "str":
                        input_values[index][each_index] = str(each_value)
                    # List[int]
                    if each_arg == "int":
                        input_values[index][each_index] = int(each_value)

            # ListNode
            if args_type == "ListNode":
                temp = eval(temp)
                input_values[index] = list_to_listnode(target=temp)

            # TreeNode
            if args_type == "TreeNode":
                temp = eval(temp)
                input_values[index] = list_to_treenode(data=temp)

    def translate_output_type(self, output_values: str) -> Any:
        # Str
        if self.output_args_type == "str":
            return str(output_values)

        # Int
        if self.output_args_type == "int":
            return int(output_values)

        # List[Any]
        output_arg = re.findall("List\[(.*)\]", string=self.output_args_type)
        if output_arg:
            temp = eval(output_values)
            each_arg = output_arg[0]
            for each_index, each_value in enumerate(temp):
                # List[str]
                if each_arg == "str":
                    temp[each_index] = str(each_value)
                # List[int]
                if each_arg == "int":
                    temp[each_index] = int(each_value)
            return temp

        # ListNode
        if self.output_args_type == "ListNode":
            return list_to_listnode(target=eval(output_values))

        # TreeNode
        if self.output_args_type == "TreeNode":
            return list_to_treenode(data=eval(output_values))

        # None
        if self.output_args_type == "None":
            return eval(output_values)
