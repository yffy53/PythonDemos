import json


txt = 'mmb.txt'  #储存数据
password_max = '13708'  #管理员密码
#当前用户
username_now = ''
password_now = ''


class User:
    def __init__(self, username, password):
        self.username = username  #用户名
        self.password = password  #密码
        self.num = 0  #对战次数
        self.win_num = 0  #胜利次数
        self.defeat_num = 0  #失败次数

    def login_list(self):  #用户数据写入字典
        data_list = [self.password, self.num, self.win_num, self.defeat_num]
        data_dict = {self.username: data_list}
        return data_dict

    def record(self, num=0, win_num=0, defeat_num=0):  #战绩更新
        self.num += num
        self.win_num += win_num
        self.defeat_num += defeat_num
        return self.login_list()


def write_dict_a(name, password):  #字典格式追加写入
    data_dict = User(name, password).login_list()
    with open(txt, 'a', encoding='utf-8') as f:
        json.dump(data_dict, f, ensure_ascii=False)
        f.write('\n')


def json_dict(path):  #字典格式读取，返回包含多部字典的列表
    dicts = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                dict_data = json.loads(line.strip())  # 去除行尾的换行符并解析JSON
                dicts.append(dict_data)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON on line: {line.strip()}\nError: {e}")
    return dicts


def fetch_contrast(username, password):  #验证用户名是否存在，密码是否正确
    data_list = json_dict(txt)
    for i in data_list:
        for key, value in i.items():
            if key == username:
                if password == value[0]:
                    return 1
                else:
                    return 2
    return 3


def write_dict_w(username, password, num=0, win_num=0, defeat_num=0):  #覆盖写入
    user = User(username, password)
    data_dict_list = json_dict(txt)
    back = 0
    with open(txt, 'w', encoding='utf-8') as f:
        for i in data_dict_list:
            for key, value in i.items():
                if key == username:
                    i[key] = user.record(num=num, win_num=win_num, defeat_num=defeat_num)[user.username]
                    back = 1
            json.dump(i, f, ensure_ascii=False)
            f.write('\n')
    return back
