## 第一次写ReadMe文件出现的问题
  ```
  The current branch master has no upstream branch. To push the current branch
  ```
出现这个问题后经过百度，有人提出了两种解决办法：
 - 法一:
	1. 在创建远程仓库的时候，就创建一个ReadMe文件。因为这是标志远程仓库主分支的文件
 - 法二:
	1. git remote add origin https://github.com/CandyJar/Python-exercises.git
	2. git push -u origin master

## 待续...