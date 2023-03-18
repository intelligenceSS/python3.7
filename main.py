# 按间距中的绿色按钮以运行脚本。
import torch.cuda

if __name__ == '__main__':
    print(torch.cuda.is_available())
    print(torch.cuda.device_count())
# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
