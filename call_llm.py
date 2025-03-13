import os

import dashscope
from dashscope import MultiModalConversation

dashscope.api_key="sk-5c29358f33fd44b9bbea59b2cf6c131c"


def query_llm_qw(model_name):
    messages = [
                    {
                        "role": "system",
                        "content": [
                            {"text": "你是一位秋招笔试专家，我将给你提供一系列题目，题目包含行测和计算机专业知识两类,题目内容通过图片形式提供。"
                                     "题目类型包括但不限于单选题、多选题（不定项选择）、判断题以及代码书写题。"
                                     "由于题目内容在图片中，所以你需要先把题目内容进行输出然后再根据下面的要求进行作答"
                                     "0.对于选择题和判断题，请提供正确的答案并解释每个选项的理由。对于代码书写题，请使用Python编写并详细解释代码逻辑。\
                                        请遵循以下步骤：\
                                        选择题：\
                                        单选题：选择一个最优答案。并解释原因\
                                        多选题（不定项选择）：选择所有正确的答案。并解释原因\
                                        判断题：\
                                        给出判断结果是“正确”还是“错误”。并解释原因\
                                        代码书写题：\
                                        使用Python编写解决方案，并对代码逻辑进行详细解释。"}
                            # {"text": "你是一位行测专家，我将给你提供一系列题目,题目内容在所提供的图片当中，题目类型包括但不限于单选题、多选题（不定项选择）、判断题。"
                            #          "0.对于选择题和判断题，请提供正确的答案不需要解释每个选项的理由\
                            #             请遵循以下步骤：\
                            #             选择题：\
                            #             单选题：选择一个最优答案。\
                            #             多选题（不定项选择）：选择所有正确的答案。\
                            #             判断题：\
                            #             给出判断结果是“正确”还是“错误”。"}
                        ]
                    },
                    {
                        "role": "user",
                        "content": [
                            {"image":  os.getcwd() + '\\filesfolder\\screenshot.png'},
                            {"text": '根据图片内容给出答案'},
                        ]
                    }
                ]
    responses = MultiModalConversation.call(model=model_name,
                                            messages=messages,
                                            stream=False)
    return responses.output.choices[0].message.content[0]['text']


if __name__ == '__main__':
    root_path = os.getcwd()

    key = ""
    result = query_llm_qw("qwen-vl-max-0809", "冒泡排序")
    print(result)
