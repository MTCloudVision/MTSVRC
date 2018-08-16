FROM mxnet/python:gpu_0.11.0
LABEL maintainer "xxx@meitu.com"

# install python
RUN rm -rf /var/lib/apt/lists/*
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
            aptitude git vim make wget zip zsh pkg-config \
            build-essential checkinstall p7zip-full python-pip \
            python3-pip tmux ffmpeg i7z unrar htop cmake g++  \
            curl libopenblas-dev python-numpy python3-numpy \
            python python-tk idle python-pmw python-imaging \
            libjpeg8-dev libtiff5-dev libjasper-dev libpng12-dev \
            libtbb2 libtbb-dev  libdc1394-22-dev libavcodec-dev  \
            libavformat-dev libswscale-dev libv4l-dev libatlas-base-dev \
            gfortran && \
    apt-get autoremove && \
    apt-get clean && \
    aptitude install -y python-dev && \
    # update pip and setuptools
    pip install --upgrade pip setuptools

# install opencv
RUN mkdir -p /software && cd /software && \
    git clone https://github.com/opencv/opencv.git && \
    git clone https://github.com/opencv/opencv_contrib.git && \

RUN cd /software && \
    mkdir -p /software/opencv/build && cd /software/opencv/build && \
    cmake -DCMAKE_BUILD_TYPE=RELEASE -DCMAKE_INSTALL_PREFIX=/usr/local \
    -DOPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules \
    -DWITH_CUDA=OFF -DWITH_OPENCL=OFF -DWITH_TBB=ON -DWITH_DNN=OFF \
    -DBUILD_opencv_python2=ON -DBUILD_opencv_python3=ON .. && \
    make -j4 && \
    make install && \
    ldconfig && rm -rf /software

RUN rm -rf /var/lib/apt/lists/*

# 安装依赖包
RUN pip install -r requirements.txt -i http://pypi.douban.com/simple  --trusted-host pypi.douban.com

###############################################
# 以上部分用户可定制，以下部分不可删除
###############################################
# 项目构建
WORKDIR /MTSVRC
COPY . .
# 指定启动路径
ENTRYPOINT cd test && python run.py
