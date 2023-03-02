# 2Take1-AdBots-BlackList
严禁商用化
此版本没有白名单系统，请不要尝试以此谋利
运行环境 - python 3.8.10


服务端安装运行库: flask ratelimit pymongo

# 如何运行服务端
1. 第一次运行，打开 run me before start server [Once].bat
2. 安装 MongoDB [win10+](https://fastdl.mongodb.org/windows/mongodb-windows-x86_64-6.0.4-signed.msi)     [Linux](https://www.mongodb.com/download-center/community/releases)
3. 打开server_no_white.py，
4. 正常运行如下
* Serving Flask app 'server_no_white'
* Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:6471
 * Running on http://xxx.xxx.x.xxx:6471
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 123-427-945

# 如何分发客户端
1. 使用你喜欢的编辑器打开user.py
2. 找到第14行 url = "http://Server Ip:6471"
3. 将 Server Ip修改为你的服务器地址即可
4. 使用你喜欢的的方式打包成EXE即可

# 如何打包后台
1. 使用你喜欢的编辑器打开admin.py
2. 找到第4行 url = "http://Server Ip:6471"
3. 将 Server Ip修改为你的服务器地址即可
4. 使用你喜欢的的方式打包成EXE即可(可不打包)

