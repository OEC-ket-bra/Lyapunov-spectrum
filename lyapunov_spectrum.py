import numpy as np

class Lyapunov_spectrum:
    def __init__(self, jacobian, N_x):
        """初期設定

        Args:
            jacobian (callable): ヤコビアンを求める関数
            N_x (int): 相空間の次元
        """
        
        self.jacobian = jacobian
        self.N_x = N_x


    def __call__(self, time_series, ls_range):
        """リアプノフスペクトルを求める

        Args:
            time_series (array): 時系列データ（N_x * データ長）
            ls_range (int): 何番目までのリアプノフスペクトルを求めるか

        Returns:
            array: リアプノフスペクトル
        """

        Q = np.eye(self.N_x)
        le_bank = np.zeros(ls_range) #零配列 

        data_length = len(time_series)

        for x in time_series:
            Q, R =  np.linalg.qr(self.jacobian(x) @ Q)
            R_diag = np.diag(R)
            le_bank = le_bank + np.log(np.abs(R_diag[:ls_range]))
            
        return le_bank / data_length
