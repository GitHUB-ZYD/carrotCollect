# carrotCollect
面向个人的科研成果管理系统

# 关于代码格式化

```bash
不要eslint，太严格了

使用 vscode的插件，快捷键迅速格式化代码，能看就行

在 settings.json 文件中，添加 "editor.formatOnSave": true  即可
# https://blog.csdn.net/qq_45796592/article/details/137904808
```

# 关于git commit 不要提交module

`.gitignore` 文件在 Git 项目中是用来指定哪些文件或目录应该被 Git 忽略，不跟踪其更改。`.gitignore` 文件的规则是递归地应用于整个仓库的，包括子目录。

如果你在项目的根目录下创建了 `.gitignore` 文件，并在其中指定了某些规则，这些规则会对整个项目生效，包括所有子目录。但是，如果你在子目录中也创建了 `.gitignore` 文件，那么这个子目录下的 `.gitignore` 只会对该子目录及其更深层次的子目录有效，而不会覆盖根目录下的 `.gitignore` 规则。

例如，如果你在项目的根目录下有一个 `.gitignore` 文件，里面包含了规则 `*.log`，这将忽略整个项目中的所有 `.log` 文件。但是，如果你在某个子目录下也创建了一个 `.gitignore` 文件，并在其中指定了 `!important.log`（排除规则），这将只对那个子目录及其子目录有效，不会影响其他目录中的 `.log` 文件。

总结来说，`.gitignore` 文件在 Git 项目的子目录下是有效的，但是它只影响该子目录及其更深层次的子目录，而不会影响其他目录。

```
在 src/vue3/carrotCollect 中，就有 .gitignore 文件，只作用于 src/vue3/carrotCollect 目录，日后直接 git commit ./* 即可
```



# 实现功能

## 注册

```
1. 点击注册按钮，进入注册页面
2. 输入 用户名、邮箱和密码
3. 输入邮箱后，点击获取验证码按钮，获取验证码
4. 填写验证码后，验证是否正确，然后才可以注册
5. 注册成功或者失败的状态信息
```



# 
