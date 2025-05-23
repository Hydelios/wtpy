import time
from wtpy import WtEngine, EngineType

import sys
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 如果需要，可以将上级目录加入sys.path，避免导入失败
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")))
import path  # 你的路径模块

print("Current working directory:", os.getcwd())
print("Common path:", path.common_path)

from Strategies.HftStraDemo import HftStraDemo

if __name__ == "__main__":
    #创建一个运行环境，并加入策略
    engine = WtEngine(EngineType.ET_HFT)

    #初始化执行环境，传入
    engine.init(folder = path.common_path, cfgfile = path.cfg_path)

    #设置数据存储目录
    # engine.configStorage(module="", path="D:\\WTP_Data\\")

    #注册CTA策略工厂，即C++的CTA策略工厂模块所在的目录
    # engine.regCtaStraFactories(factFolder = ".\\cta\\")
    
    #添加外部CTA策略，即C++版本的CTA策略
    '''
    engine.addExternalHftStrategy(id = "cppxpa_rb", params = {
        "name":"WtCtaStraFact.DualThrust",  #工厂名.策略名
        "params":{  #这是策略所需要的参数
            "code":"SHFE.rb.HOT",
            "period":"m3",
            "count": 50,
            "days": 30,
            "k1": 0.2,
            "k2": 0.2
        }
    })
    '''

    engine.commitConfig()
    
    #添加Python版本的策略
    straInfo = HftStraDemo(name='pyhft_IF', code="CFFEX.IF.HOT", expsecs=15, offset=0, freq=30)
    engine.add_hft_strategy(straInfo, trader="simnow")
    
    #开始运行
    engine.run()

    print('press ctrl-c to exit')
    try:
    	while True:
            time.sleep(1)
    except KeyboardInterrupt as e:
    	exit(0)