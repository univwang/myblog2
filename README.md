# myblog

## 生成静态文件

```shell
hexo generate
```

## 静态文件public上传

```shell
scp -r .\public\* root@139.9.116.24:/root/myweb/blog
```

## git

```shell
git add .
git commit -m "hexo"
git push
```


### all

```shell
git add .
git commit -m "hexo"
git push
hexo generate
scp -r .\public\* root@139.9.116.24:/root/myweb/blog
echo "hello"
```

