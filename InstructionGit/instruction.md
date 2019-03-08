# Some operation of git

#### Synchronization 同步一个之前fork的项目

 - 先从自己的github里添加一个远程仓库到本地

```
  git remote add tmp https://github.com/XIANQw/ProjetGLA.git
```
 - 再从原作者那里添加一个远程仓库到本地

```
  git remote add upstream https://github.com/originalAuthor/original.git
```
 - 再用fetch获取上游分支的内容

```
  git fetch upstream
```
 - 切换到master分支

```
 git checkout master
```
 - 将upstream分支合并到本地master分支

```
  git merge upstream/master
```
 - 更新到 GitHub 的 fork 上

```
git push origin master
```

#### conflict -> merge项目出现冲突
 - 提交自己的代码到本地仓库　或者　stash
 ```
   git add .
   git commit -m "details"
 ```
 - 查看本地库名称并拉取代码
```
  git remote -v
  git fetch [主机名]
```
 - 将origin的代码合并到本地master分支
```
  git merge origin/master
```
 - 出现冲突，打开冲突的文件再决定Use哪一段代码并保存

 - 然后再提交到本地仓库并再次merge
```
Already up to date
```
- 若无法解决冲突，先把自己的代码移出当前文件夹，然后
```
git pull origin master
```
- 把远程仓库的代码拉取下来，再把自己的代码复制粘贴回此文件夹
```
git add.
git commit -m "something"
git push origin master
```
- ok
