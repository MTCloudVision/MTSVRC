# -*- coding: utf-8 -*-

import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(ROOT_DIR, 'data')
VIDEO_DIR = os.path.join(DATA_DIR, 'video')
IMAGE_DIR = os.path.join(DATA_DIR, 'image')
MODEL_DIR = os.path.join(ROOT_DIR, 'model')

if __name__ == '__main__':
    print ROOT_DIR
    print DATA_DIR
    print VIDEO_DIR
    print IMAGE_DIR
    print MODEL_DIR
