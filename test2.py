"""
 * Project name(项目名称)：Python_traceback模块
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/29 
 * Time(创建时间)： 11:01
 * Version(版本): 1.0
 * Description(描述)： 
 """

import traceback


class SelfException(Exception):
    pass


def main():
    firstMethod()


def firstMethod():
    secondMethod()


def secondMethod():
    thirdMethod()


def thirdMethod():
    raise SelfException("自定义异常信息")


if __name__ == '__main__':
    try:
        main()
    except:
        # 捕捉异常，并将异常传播信息输出控制台
        traceback.print_exc()
        # 捕捉异常，并将异常传播信息输出指定文件中
        traceback.print_exc(file=open('error.log', 'a', encoding="UTF-8"))
