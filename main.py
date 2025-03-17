import subprocess


path = r'C:\"Program Files (x86)\Tencent\WeChat\WeChat.exe"'
command = f'start {path}'


def run_cmd(run_time):
    try:
        run_time = int(run_time)
        run_command = command
        for i in range(1, run_time):
            run_command += f' && {command}'
        result = subprocess.run(run_command, shell=True,
                                capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print(f'[Error] 发生了一个错误: ', str(e), '!')


if __name__ == "__main__":
    while True:
        try:
            number = int(input('[In] 请输入多开数量 > '))
            if 0 < number < 11:
                run_cmd(number)
                break
            else:
                print('[Out] 请输入大于0且小于11的整数!')
        except:
            print('[Error] 请输入有效的整数!')
