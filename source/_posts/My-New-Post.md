---
title: My New Post
date: 2020-10-04 06:06:48
tags:
---
SSR安卓客户端
https://github.com/shadowsocksrr/shadowsocksr-android/releases

“email”: “gongyaoman015@163.com“,
“password”: “a1234560”

```
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
python -m pip install –upgrade pip
```

`npm config set registry https://registry.npm.taobao.org`

pyinstaller -F –noconsole test_9_25.py

hexo
`npm install -g hexo-cli`

`hexo init my-blog`

```
git config --global user.name "iplai"
git config --global user.email "365141210@qq.com"
```

在git bash 中执行,或将( C:\Program Files\Git\usr\bin)添加进环境变量
`ssh-keygen -t rsa -C "365141210@qq.com"`
`cat ~/.ssh/id_rsa.pub`
https://github.com/settings/ssh/new

验证
```
ssh -T git@github.com
```
Hi iplai! You’ve successfully authenticated, but GitHub does not provide shell access.

_config.yml最后一行
```
deploy:
  type: git
  repository: https://github.com/iplai/iplai.github.io
  branch: main
```
新建文章
`hexo new post "article title"`

部署到 GitHub Pages
```
npm install hexo-deployer-git --save
hexo g
hexo d
```