# -*- coding:utf-8 -*-


import os
import time

from caffe.infer.log import LOG
from infer.defines import DATA_DIR, VIDEO_DIR
from infer.infer import ServerApi

os.environ['GLOG_minloglevel'] = '3'
server = ServerApi()


def verify_method(type):
    start_time = time.time()
    # 视频读取
    video_list = []
    with open(os.path.join(DATA_DIR, 'input_%s.txt' % type), 'r+') as f:
        line = f.readline()
        while line:
            video_path = line.replace('\n', '')
            video_list.append(os.path.join(VIDEO_DIR, video_path))
            line = f.readline()
    # 视频处理
    result_list = []
    for video in video_list:
        video_name = video.split('/')[-1]
        try:
            cla = server.handle(video)
        except Exception:
            cla = -1        # -1代表预测异常
        result_list.append([video_name, cla])
    # 结果输出
    with open(os.path.join(DATA_DIR, 'output_%s.txt' % type), 'w+') as f:
        for result in result_list:
            out_info = str(result[0]) + ',' + str(result[1]) + '\n'
            f.write(out_info)
    end_time = time.time()
    return len(video_list), end_time - start_time


if __name__ == '__main__':
    # 速度验证
    count, total_time = verify_method('time')
    LOG.info('verify time: count=%s, total_time=%s' % (count, total_time))
    # 准确率验证
    count, total_time = verify_method('acc')
    LOG.info('verify acc: count=%s, total_time=%s' % (count, total_time))
