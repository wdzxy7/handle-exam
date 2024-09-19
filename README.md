# handle-exam
this code is base on https://github.com/lxygoodjob/Hit-leetcode. 

I rewrite these codes: computer1.py, computer2.py call_llm.py.

These changes makes this project more suitable for multiple-choice question.

The screenshot is from your mouse position to the bottom right corner of the screen, and the screenshot results will store in the savefolder name as screenshot.png.

If you change the savefolder and the file name, please make sure this configuration is the same in computer1.py, computer2.py, call_llm.py(line 55).

Different from the original code, you must fix the dashscope.api_key in call_llm.py which can be get from https://help.aliyun.com/zh/dashscope/developer-reference/compatibility-of-openai-with-dashscope?spm=a2c4g.11186623.0.0.3a5446c1Be7jxC. 

The prompt I have designed, you can modify it according to your needs.

Do not change llm_type in computer2.py(line 31).

The following guidance is copy from Hit-leetcode：

电脑2，获取答案用电脑
pip install -r requirements_computer2.txt

运行 python computer2.py
获取当前的请求url， 一般是192.168.x.x:9210, 这里我设的端口是9210

电脑1，面试用电脑
pip install -r requirements_computer1.txt

填入 电脑2运行后的url = "http://xxxx:9210/get_code"

运行 python computer1.py

快捷键 'Shift+Z'
截图并请求答案, 这边需要先把鼠标移到要截取的区域右下角，会从屏幕左上角（0，0）截到该位置

快捷键 'Shift+X'
重新识别上一次的图片，重新请求大模型获取答案, 如果要再次截图识别获取答案，请再次按快捷键 'Shift+Z' ， 注意鼠标位置！！！！！
