## MTSVRC相关文档

### Baseline
* 时间基准值 Time Baseline：100ms/Video
* 准确率基准值 ACC Baseline：0.78
* 说明：
    - 运行时间计算的是从读入视频路径到输出预测标签的所有时间
    - 最终计算排名使用的是误差Baseline，其值为1 - acc

### 测试机器配置
* GPU：TITAN Xp
* CPU：48 Intel(R) Xeon(R) CPU E5-2650 v4 @ 2.20GHz
* 内存：128G

### 竞赛须知
#### Docker工程
* 参赛选手需自行创建和参赛英文队名一致的项目和工程名称。
    - 项目名需去掉空格和标点符号，只包含小写字母、数字、下划线
    - eg:参赛队伍名称为 meitu’ 2018，则需创建meitu2018项目
* 项目权限需设置为私有，默认只有参赛者和组织方有权访问。
    
#### Docker标签
* 为避免镜像上传覆盖，上传时需更新tag，tag中需记录上传时间和当天的上传次数。
    - eg：meitu2018:v0815-01；meitu2018:v0815-02
* 除算法运行必要的环境、模型、代码等数据，不要将其他视频、图像数据一起打包上传。
* 命令：
    - docker pull 仓库地址/项目名/工程名:标签
    - docker pull registry.meitu-int.com/meitu2018/meitu2018:v0815-01
 
#### 验证策略
* 组织方每周只会对参赛者**前两次**提交的镜像进行测试。
* 时间测评：
    - 时间测评阶段组织方将运行部分视频来测评参赛队伍的算法平均运行时间。
    - 若运行时间达不到基准值，则不进入准确率测评，竞赛组织方将直接通知参赛队伍。
    - 组织方会测试处理500个视频的时间。测试程序运行10次，取平均结果。
* 准确率测评：
    - 准确率测评阶段组织方将运行全部测试视频来评测参赛队伍的算法准确率。
    - 测试集相对验证集各类别数量更均衡一些，故验证集准确率可能与测试集准确率有一定差异。

#### 标签映射
* 模型的输出标签ID需要和标准ID一致，具体参考[MTSVRC标签](doc/Tag.md)


#### 标准格式
##### 代码格式
* 参赛者需参考**infer.py**标准格式写好接口，不得改变**ServerApi**类名和**handle**函数名。
    - 其中**handle**函数的输入需为单视频路径，输出需为该视频识别标签。
    - 参赛者需将模型加载等初始化操作并入**__init__**，并指定运行环境gpu_id。
    - 若参赛选手使用非python的其他语言，也需要使用python中转，实现infer.py的相关功能。
##### Dockerfile格式
* 不强制要求基础镜像的环境、框架和版本
* 但必须启动执行：ENTRYPOINT cd test && python run.py
* 具体参考：[Dockerfile](mxnet/Dockerfile)
    
#### 代码结构
* mxnet：mxnet版本demo
    - infer：算法代码
    - Dockerfile：构建文档
    - requirements.txt：pip安装文件
  - infer.py：算法接口代码
* caffe：caffe版本demo
* test：测试文件夹
    - run.py：启动文件
	- video：测试数据集
    - input.txt：输入文件
    - output.txt：输出文件
    - tag.txt：标签文件
    - result.txt：结果文件
* <font color="red">注：test目录只做参考，后期会被组织方真实验证目录覆盖，故不能存放任何与算法相关的数据</font>

```
.
├── README.md
├── caffe
│   ├── Dockerfile
│   ├── README.md
│   ├── infer
│   │   └── infer.py
│   └── requirements.txt
├── doc
├── mxnet
│   ├── Dockerfile
│   ├── README.md
│   ├── infer
│   │   └── infer.py
│   └── requirements.txt
└── test
    ├── input.txt
    ├── output.txt
    ├── result.txt
    ├── run.py
    ├── tag.txt
    └── video
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
nvidia-docker build -t meitu2018 .
# 运行服务
nvidia-docker run -it meitu2018
# 查看服务输出
nvidia-docker ps
```

#### 推送命令(push)
```
# 登录Harbor平台
docker login http://registry.xxx.com/ 
# 镜像打标记    				
docker tag meitu2018 registry.xxx.com/meitu2018/meitu2018:v0815-01
# 镜像推送   	
docker push registry.xxx.com/meitu2018/meitu2018:v0815-01		
```

### 示例程序
* [caffe版本构建样例](caffe/README.md)
* [mxnet版本构建样例](mxnet/README.md)


### 常见问题
* 组织方将定期整理参数选手遇到的[常见问题](doc/FAQ.md)，新问题欢迎提交Issue.