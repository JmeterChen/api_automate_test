
##  线上机器人2期项目结构及使用说明

#### <span id="jump2">项目结构</span>
![项目接口](https://img-blog.csdnimg.cn/20190909165400556.jpeg)  
  #### conf
 - [ ] 大家不需要管，这个已经通用化了！

 #### data
`两个方案，自己随意挑选`
    
 - [ ] 方案一：

    - excleFiles
        - 按项目划分，一个项目一个excle表格 ，示例表格：==ddsf.xlsx==
        - 存放测试excle用例，接口请求详情数据 
        
    |  字段名称| 是否必填 |填写规则  |
    |--|--|--|
    | 环境 | 是 | test/pre/prod|
    | 模块名 | 是 | 需要与json中模块名和类名前缀部分保持一致 |
    | 接口名称 | 是 | 需要与json中接口名和函数后缀名保持一致 |
    | 请求方法 | 是 | http常见请求方法 |
    | 用例描述 | 是| 自定义描述即可 |
    | 是否跳过该用例 | 否 | 是/否，其他内容默认为是 |
    | 请求头 | 是 | dict格式 |
    | 接口关联参数 | 否 | dict格式,relateOut/relateIn/all |
    | 请求参数 | 是 | dict格式 |
    | 请求体 | 是 | 无 |
    | 预期结果 | 是 | dict格式 |
    - jsonFiles

    |  结构层级 |是否拥有限制 |填写规则  |
    |--|--|--|
    | 项目名称 | 是| 与excle表文件名一致|
    | 模块名称 | 是| 与脚本中类名保持一致 |
    | 接口名 | 是| 与用例脚本中函数名称保持一致 |

 - [ ] 方案二：

    - FDD接口测试用例.xlsx
         -  按项目划分，一个项目一个sheet页签，名称与项目名（json中项目名称以及用例脚本的文件夹后缀名保持一致）
            示例：
            ![excle页签名称](https://img-blog.csdnimg.cn/20190909191725712.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTM4NjE0NQ==,size_16,color_FFFFFF,t_70)
   
    - config.json
        -  按项目划分，一个项目json模块；
            ![json文件](https://img-blog.csdnimg.cn/20190909192057718.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTM4NjE0NQ==,size_16,color_FFFFFF,t_70)
   #### output
    - logs (可扩展)  
        <span color='yellow'>日志来源于日志配置文件，大家可以不用管，直接套用即可</span>
         -  run.log ：默认不传入日志参数时自动生成的用例运行日志记录；
         -  runTest.log ：根据传入的日志参数生成对应的操作日志记录；
         -  getData.log ：用做获取数据时操作步骤日志记录；   
    - report
        - 根据修改过的BeautifulReport库生成的测试报告；

#### src

1. common

	`该目录下文件夹均为自定义组件模块，大家直接套用即可，每个函数/类均有解释说明`
	
    模块/包名 | 作用 | 备注
    ---|--- | ---
    |  BeautifulReport| 生成新版测试报告 | （源码被修改了）直接使用即可
	|  read_data.py| 读取excle/json文件中的测试用例数据 |  注意上述data方案
	|  readaLogger.py| 读取日志配置文件并按配置生成日志 |  直接使用即可
	|  runMethod.py| 根据测试数据重新定义http常见请求 |  直接使用即可
	|  runTest.py | 用例基础信息写入日志  | 直接使用即可 |


 2. mainProgram
      - run.py  项目启动函数，需要补充根据不同项目启动需要设置
 
 
#### 项目用例

 3. 文件夹以test_xxx命名；
 4. 分项目存放用例脚本；
 5. 单个项目中以模块创建py文件脚本（名称不做要去）；
 6. 上述脚本中以模块创建类，格式如XXXTest；
 7. 上述类中以接口名创建用例，格式为test_xxx；

 ![在这里插入图片描述](https://img-blog.csdnimg.cn/20190909201251465.jpeg)
 
 #### 待补充
    1.接入钉钉系统函数
    2.分项目启动脚本
    3.接入RabbitMQ
    4.接口用例报错统计
    5.请求参数化做判断
    6.签名加密
