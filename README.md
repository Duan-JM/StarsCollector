## Install
安装到 python 库中，并会自动生成可执行文件 `sc`。

```bash
make install
```
## Usage

```bash
sc -id <github-id>
```

结合 grep 使用

```bash
sc -d Duan-JM 2>&1 | grep -C 4 luyuhao
```

## NeedFix

Make install 完成之后，可执行文件 `sc` 的输出路径需要进行手动的调整。

如下为我的安装的 log 输出：

```bash
Installing sc script to /usr/local/Cellar/python@3.8/3.8.5/Frameworks/Python.framework/Versions/3.8/bin

Installed /usr/local/lib/python3.8/site-packages/stars_collecter-0.1.dev0-py3.8.egg
Processing dependencies for stars-collecter==0.1.dev0
Searching for requests==2.24.0
Best match: requests 2.24.0
Adding requests 2.24.0 to easy-install.pth file

Using /usr/local/lib/python3.8/site-packages
Searching for urllib3==1.25.10
Best match: urllib3 1.25.10
Adding urllib3 1.25.10 to easy-install.pth file

Using /usr/local/lib/python3.8/site-packages
Searching for idna==2.10
Best match: idna 2.10
Adding idna 2.10 to easy-install.pth file

Using /usr/local/lib/python3.8/site-packages
Searching for chardet==3.0.4
Best match: chardet 3.0.4
Adding chardet 3.0.4 to easy-install.pth file
Installing chardetect script to /usr/local/Cellar/python@3.8/3.8.5/Frameworks/Python.framework/Versions/3.8/bin

Using /usr/local/lib/python3.8/site-packages
Searching for certifi==2020.6.20
Best match: certifi 2020.6.20
Adding certifi 2020.6.20 to easy-install.pth file

Using /usr/local/lib/python3.8/site-packages
Finished processing dependencies for stars-collecter==0.1.dev0
```

可以看到我的本地测试环境中可执行文件生成到
`/usr/local/Cellar/python@3.8/3.8.5/Frameworks/Python.framework/Versions/3.8/bin`
中，需要手动的把这个路径添加到 PATH 中，或者手动的把这个文件拷贝到 PATH
的目录下也行。 目前还没有找到合适的解决方案。
