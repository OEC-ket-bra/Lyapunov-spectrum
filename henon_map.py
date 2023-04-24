import numpy as np


class Henon_Map:
    def __init__(self, a=1.4, b=0.3):
        self.a, self.b = a, b

    def henon_map(self, x, y):
        return [self.a - x ** 2 + self.b * y, x]

    def save(self, init_xy: list, data_num: int, save_name: str) -> None :
        """
        データ列を作成して保存

        Parameters
        ----------
        init_xy : list
            初期値
        data_num : int
            データ数
        save_name : str
            保存名
        """

        x, y = init_xy

        xy_list = []
        xy_list.append([x, y])

        for i in range(data_num):
            x, y = self.henon_map(x, y)
            xy_list.append([x, y])

        data = np.array(xy_list)
        np.save('./{}'.format(save_name), data)