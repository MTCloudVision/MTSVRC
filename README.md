### 文件格式
#### 目录格式
* run.py 启动文件
* data：存放数据
	- image：图片数据
	- video: 视频数据
    - input.txt：输入文件
    - output.txt：输出文件
* infer: 存放代码
  - infer.py 算法服务代码
  - defines.py 常量参数
* model：存放模型

```
.
├── Dockerfile
├── README.md
├── data
│   ├── image
│   │   └── 1001717770
│   │       └── 01.jpg
│   ├── input.txt
│   ├── output.txt
│   └── video
│       └── 1001717770.mp4
├── infer
│   ├── defines.py
│   └── infer.py
├── model
└── run.py
```


#### 输入文件格式
```
963193352.mp4
970453214.mp4
...
```

#### 输出文件格式
```
963193352.mp4,13
970453214.mp4,39
...
```

### 基本命令
#### 拉取命令(pull)
```
docker pull mxnet/python:gpu_0.11.0
```

#### 构建命令(build)
* 由于此处为GPU镜像，故需要nvidia-docker进行构建

```
# 服务构建
nvidia-docker build -t demo_mxnet .
# 运行服务
nvidia-docker run -it demo_mxnet
# 查看服务输出
nvidia-docker ps
```

#### 推送命令(push)
```
# 登录Harbor平台
docker login http://registry.xxx.com/ 
# 镜像打标记    				
docker tag demo_mxnet registry.xxx.com/prcv/demo_mxnet
# 镜像推送   	
docker push registry.xxx.com/prcv/demo_mxnet		
```

### 示例程序
* [caffe版本构建样例](caffe/README.md)
* [mxnet版本构建样例](mxnet/README.md)


