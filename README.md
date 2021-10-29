## [python development in cinema 4d](https://github.com/iplai/ic4d)

### 一行命令查看**python**版本
`import sys;print(sys.version)`
```
'3.9.1+ (pipelines/8936:778d593, Jan 25 2021, 20:35:13) [MSC v.1900 64 bit (AMD64)]'
```

### 一行命令查看**python**所有依赖路径
`import sys;print("\n".join(sys.path))`
```
C:\Program Files\Maxon Cinema 4D R25\resource\modules\python\libs\python39
C:\Users\iplai\AppData\Roaming\Maxon\Maxon Cinema 4D R25_1FE0824E\python39
C:\Program Files\Maxon Cinema 4D R25\resource\modules\python\libs\python39.win64.framework\lib
C:\Program Files\Maxon Cinema 4D R25\resource\modules\python\libs\python39.win64.framework\dlls
C:\Program Files\Maxon Cinema 4D R25
C:\Users\iplai\AppData\Roaming\Maxon\python\python39\libs
C:\Users\iplai\AppData\Roaming\Maxon\Maxon Cinema 4D R25_1FE0824E\python39\libs
C:\Program Files\Maxon Cinema 4D R25\resource\modules\python\libs\python39.win64.framework\lib\site-packages
```

### 存放第三方包的路径 [官方链接](https://developers.maxon.net/docs/Cinema4DPythonSDK/html/manuals/introduction/python_libraries.html)
`%APPDATA%/MAXON/python/python39/libs`

### 给开发时的python解释器添加 c4d fake package 以支持代码提示和自动补全 [官方链接](https://developers.maxon.net/docs/Cinema4DPythonSDK/html/manuals/introduction/autocompletion_dummy_package.html)
在site-packages目录下执行
```
mklink /d /h /j c4d "C:\Program Files\Maxon Cinema 4D R25\resource\modules\python\libs\python39\c4d"
```

### 将开发目录链接到C4D插件目录
```
cd "C:\Program Files\Maxon Cinema 4D R25\plugins"
mklink /d /h /j {目录名} "{开发目录的绝对路径}"
example:
mklink /d /h /j TorusKnot "C:\Users\iplai\Desktop\C4D-HOME\c4d-torusknot\TorusKnot"
```
