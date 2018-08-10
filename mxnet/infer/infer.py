# -*- coding: utf-8 -*-

import os
import random

from defines import IMAGE_DIR


class ServerApi(object):
    """
    统一算法预测接口类：
    注：
        1.handle为举办方验证接口，该接口必须返回预测分类值，参赛队伍需具体实现该接口
        2.模型装载操作必须在初始化方法中进行
        3.其他接口都为参考，可以选择实现或删除
    """
    def __init__(self):
        self.model = self.load_model()

    def video_frames(self, file_dir):
        """
        视频截帧
        :param file_dir: 视频路径
        :return:
        """
        return None

    def load_model(self):
        """
        模型装载
        """
        return ''

    def predict(self, file_dir):
        """
        模型预测
        :param file_dir: 预测文件路径
        :return:
        """
        return None

    def handle(self, video_dir):
        """
        算法处理
        :param video_dir: 待处理视频路径
        :return: 返回预测分类
        """
        return random.randint(0, 50)
