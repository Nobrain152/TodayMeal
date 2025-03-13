import os
from openai import OpenAI
import base64


def doubao_img():
    # 请确保您已将 API Key 存储在环境变量 ARK_API_KEY 中
    # 初始化Ark客户端，从环境变量中读取您的API Key
    client = OpenAI(
        # 此为默认路径，您可根据业务所在地域进行配置
        base_url="https://ark.cn-beijing.volces.com/api/v3",
        # 从环境变量中获取您的 API Key。此为默认方式，您可根据需要进行修改
        api_key="61bfc492-1121-4db8-a22f-e56e60e2f043",
    )

    # 定义方法将指定路径图片转为Base64编码
    def encode_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    # 需要传给大模型的图片
    image_path = "C:\\Users\\DELL\\Desktop\\今天的饭\\企业微信截图_17411567072582.png"

    # 将图片转为Base64编码
    base64_image = encode_image(image_path)
    response = client.chat.completions.create(
        # 指定您创建的方舟推理接入点 ID，此处已帮您修改为您的推理接入点 ID
        model="ep-20250305143354-9fqlk",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "总结出一套文档的模板，只需要模板，不需要任何额外信息。"},
                    {
                        "type": "image_url",
                        "image_url": {
                            # 需要注意：传入Base64编码前需要增加前缀 data:image/{图片格式};base64,{Base64编码}：
                            # PNG图片："url":  f"data:image/png;base64,{base64_image}"
                            # JEPG图片："url":  f"data:image/jpeg;base64,{base64_image}"
                            # WEBP图片："url":  f"data:image/webp;base64,{base64_image}"
                            "url":  f"data:image/png;base64,{base64_image}"
                        },
                    },
                ],
            }
        ],
    )

    # response = client.chat.completions.create(
    #     # 指定您创建的方舟推理接入点 ID，此处已帮您修改为您的推理接入点 ID
    #     model="ep-20250305143354-9fqlk",
    #     messages=[
    #         {
    #             "role": "user",
    #             "content": [
    #                 {"type": "text", "text": "总结出一套文档的模板，只需要模板，不需要任何额外信息。"},
    #                 {
    #                     "type": "image_url",
    #                     "image_url": {
    #                         "url": "https://ark-project.tos-cn-beijing.ivolces.com/images/view.jpeg"
    #                     },
    #                 },
    #             ],
    #         }
    #     ],
    # )

    print(response.choices[0])

# 联网工具
# 抓取菜谱有联网实时性的需求，因此需要联网工具
def scrape_recipes():
    # 请确保您已将 API Key 存储在环境变量 ARK_API_KEY 中
    # 初始化Openai客户端，从环境变量中读取您的API Key
    client = OpenAI(
        # 此为默认路径，您可根据业务所在地域进行配置
        base_url="https://ark.cn-beijing.volces.com/api/v3/bots",
        # 从环境变量中获取您的 API Key
        api_key="0db98a0f-5cc0-46b3-9b8b-6646316133cf"
    )

    content='# [菜品名称]\n## 基本信息\n分类：[菜品所属分类]\n制作量：[X人份]\n制作需要时间：[X分钟]\n|准备食材需要时间|腌制需要时间|烹饪需要时间|\n|----|----|----|\n|[X分钟]|[X分钟]|[X分钟]|\n需要厨具：[所需厨具]\n\n## 原材料\n|制作部分|原材料名称|用量|\n|----|----|----|\n|原材料|[原材料 1]|[用量 1]|\n|原材料|[原材料 2]|[用量 2]|\n|...|...|...|\n|腌料|[腌料 1]|[用量 3]|\n|腌料|[腌料 2]|[用量 4]|\n|...|...|...|\n\n## 制作流程\n1. [步骤 1：原材料前期处理]\n2. [步骤 2：腌制操作]\n3. [步骤 3：烹饪前期准备及初始烹饪操作]\n4. [步骤 4：持续烹饪 及过程中的关键操作]\n5. [步骤 5：装盘等收尾操作] '

    # Non-streaming:
    print("----- standard request -----")
    completion = client.chat.completions.create(
        model="bot-20250304142343-b7fx6",  # bot-20250304142343-b7fx6 为您当前的智能体的ID，注意此处与Chat API存在差异。差异对比详见 SDK使用指南
        messages=[
            {"role": "system", "content": "规整菜谱请按照以下格式进行规整。\n" + content},
            {"role": "user", "content": "从下厨房规整一份鱼香肉丝菜谱。"},
        ],
    )
    print(completion)
    print(completion.choices[0].message.content)
    if hasattr(completion, "references"):
        print(completion.references)


    


# 非联网工具
# 按输入食材生成菜谱
# 只是说规划做多少菜的话，不联网的工具其实就可以
def generate_recipe_based_on_ingredients():
    # 请确保您已将 API Key 存储在环境变量 ARK_API_KEY 中
    # 初始化Openai客户端，从环境变量中读取您的API Key
    client = OpenAI(
        # 此为默认路径，您可根据业务所在地域进行配置
        base_url="https://ark.cn-beijing.volces.com/api/v3/bots",
        # 从环境变量中获取您的 API Key
        api_key="0db98a0f-5cc0-46b3-9b8b-6646316133cf"
    )

    # Non-streaming:
    print("----- standard request -----")
    completion = client.chat.completions.create(
        model="bot-20250313170347-db6x7",  # bot-20250313170347-db6x7 为您当前的智能体的ID，注意此处与Chat API存在差异。差异对比详见 SDK使用指南
        messages=[
            {"role": "system", "content": "你是一个家庭主妇。"},
            {"role": "user", "content": "家里有500g的鸡腿，400g的藕，请帮我规划一下明天两人份的便当要做什么菜"},
        ],
    )
    print(completion)
    print(completion.choices[0].message.content)
    if hasattr(completion, "references"):
        print(completion.references)

    
    # # Multi-round：
    # print("----- multiple rounds request -----")
    # completion = client.chat.completions.create(
    #     model="bot-20250305143505-pkczk",  # bot-20250305143505-pkczk 为您当前的智能体的ID，注意此处与Chat API存在差异。差异对比详见 SDK使用指南
    #     messages=[  # 通过会话传递历史信息，模型会参考上下文消息
    #         {"role": "system", "content": "你是豆包，是由字节跳动开发的 AI 人工智能助手"},
    #         {"role": "user", "content": "花椰菜是什么？"},
    #         {"role": "assistant", "content": "花椰菜又称菜花、花菜，是一种常见的蔬菜。"},
    #         {"role": "user", "content": "再详细点"},
    #     ],
    # )
    # print(completion.choices[0].message.content)
    # if hasattr(completion, "references"):
    #     print(completion.references)

    # # Streaming:
    # print("----- streaming request -----")
    # stream = client.chat.completions.create(
    #     model="bot-20250305143505-pkczk",  # bot-20250305143505-pkczk 为您当前的智能体的ID，注意此处与Chat API存在差异。差异对比详见 SDK使用指南
    #     messages=[
    #         {"role": "system", "content": "你是豆包，是由字节跳动开发的 AI 人工智能助手"},
    #         {"role": "user", "content": "常见的十字花科植物有哪些？"},
    #     ],
    #     stream=True,
    # )
    # for chunk in stream:
    #     if hasattr(chunk, "references"):
    #         print(chunk.references)
    #     if not chunk.choices:
    #         continue
    #     if chunk.choices[0].delta.content:
    #         print(chunk.choices[0].delta.content, end="")
    # print()

if __name__ == "__main__":
    # doubao_img()
    scrape_recipes()
    # generate_recipe_based_on_ingredients()