# Cursor通过GitHub做版本控制完整指南

## 目录
1. [前提条件](#前提条件)
2. [Git安装和配置](#git安装和配置)
3. [GitHub账户设置](#github账户设置)
4. [Cursor中Git集成](#cursor中git集成)
5. [项目版本控制流程](#项目版本控制流程)
6. [常用Git操作](#常用git操作)
7. [分支管理](#分支管理)
8. [协作开发](#协作开发)
9. [常见问题解决](#常见问题解决)
10. [最佳实践](#最佳实践)

## 前提条件

### 系统要求
- Windows 10/11（64位）
- 稳定的网络连接
- 至少2GB可用磁盘空间

### 必需软件
- Git（最新版本）
- Cursor编辑器
- GitHub账户

## Git安装和配置

### 1. 安装Git
1. 访问 [Git官网](https://git-scm.com/)
2. 下载Windows版本
3. 运行安装程序，使用默认设置即可

### 2. 验证Git安装
打开命令提示符（CMD）或PowerShell，执行：

```bash
# 检查Git版本
git --version

# 检查Git配置
git config --list
```

### 3. 配置Git用户信息
```bash
# 设置用户名和邮箱
git config --global user.name "您的用户名"
git config --global user.email "您的邮箱@example.com"

# 验证配置
git config user.name
git config user.email
```

### 4. 配置SSH密钥（推荐）
```bash
# 生成SSH密钥
ssh-keygen -t ed25519 -C "您的邮箱@example.com"

# 启动ssh-agent
eval "$(ssh-agent -s)"

# 添加SSH密钥到ssh-agent
ssh-add ~/.ssh/id_ed25519

# 复制公钥到剪贴板
clip < ~/.ssh/id_ed25519.pub
```

## GitHub账户设置

### 1. 创建GitHub账户
1. 访问 [GitHub官网](https://github.com/)
2. 点击"Sign up"注册账户
3. 验证邮箱地址

### 2. 添加SSH密钥到GitHub
1. 登录GitHub
2. 点击右上角头像 → Settings
3. 左侧菜单选择"SSH and GPG keys"
4. 点击"New SSH key"
5. 粘贴之前复制的公钥内容
6. 点击"Add SSH key"

### 3. 测试SSH连接
```bash
ssh -T git@github.com
```

## Cursor中Git集成

### 1. 打开源代码管理面板
- 按 `Ctrl+Shift+G` 打开Git面板
- 或点击左侧活动栏的源代码管理图标

### 2. 初始化Git仓库
1. 在Cursor中打开项目文件夹
2. 按 `Ctrl+Shift+P` 打开命令面板
3. 输入 "Git: Initialize Repository"
4. 选择项目根目录

### 3. 配置Git设置
在项目根目录创建 `.gitignore` 文件：

```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
venv/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Logs
*.log

# Data files
*.csv
*.xlsx
*.json
```

## 项目版本控制流程

### 1. 创建GitHub仓库
1. 登录GitHub
2. 点击右上角"+" → "New repository"
3. 填写仓库名称和描述
4. 选择公开或私有
5. 不要初始化README（我们将在本地创建）

### 2. 连接本地仓库到GitHub
```bash
# 在项目根目录执行
git remote add origin git@github.com:用户名/仓库名.git

# 验证远程仓库
git remote -v
```

### 3. 首次提交
```bash
# 添加所有文件到暂存区
git add .

# 创建首次提交
git commit -m "Initial commit: 项目初始化"

# 推送到GitHub
git push -u origin main
```

## 常用Git操作

### 1. 基本工作流程
```bash
# 查看状态
git status

# 添加文件到暂存区
git add 文件名
git add .  # 添加所有文件

# 提交更改
git commit -m "提交信息"

# 推送到远程仓库
git push

# 从远程仓库拉取更新
git pull
```

### 2. 查看历史记录
```bash
# 查看提交历史
git log --oneline

# 查看特定文件的修改历史
git log --follow 文件名

# 查看最近n次提交
git log -n 5
```

### 3. 撤销操作
```bash
# 撤销工作区的修改
git checkout -- 文件名

# 撤销暂存区的修改
git reset HEAD 文件名

# 撤销最后一次提交
git reset --soft HEAD~1

# 撤销提交并保留修改
git reset --mixed HEAD~1
```

## 分支管理

### 1. 创建和切换分支
```bash
# 创建新分支
git branch 分支名

# 切换到分支
git checkout 分支名

# 创建并切换到新分支
git checkout -b 新分支名

# 查看所有分支
git branch -a
```

### 2. 合并分支
```bash
# 切换到目标分支（通常是main）
git checkout main

# 合并分支
git merge 分支名

# 删除已合并的分支
git branch -d 分支名
```

### 3. 解决冲突
当合并出现冲突时：
1. 打开冲突文件
2. 查找冲突标记 `<<<<<<<`, `=======`, `>>>>>>>`
3. 手动编辑解决冲突
4. 保存文件
5. 添加解决后的文件：`git add 文件名`
6. 完成合并：`git commit`

## 协作开发

### 1. Fork和Pull Request
1. 在GitHub上Fork目标仓库
2. 克隆Fork的仓库到本地
3. 创建功能分支
4. 进行修改并提交
5. 推送到Fork的仓库
6. 创建Pull Request

### 2. 代码审查
- 在GitHub上查看Pull Request
- 添加评论和反馈
- 请求更改或批准合并

### 3. 同步上游仓库
```bash
# 添加上游仓库
git remote add upstream 原仓库URL

# 获取上游更新
git fetch upstream

# 合并上游更改
git merge upstream/main
```

## 项目配置

### 1. 项目结构
```
my_project/
├── .git/                   # Git仓库文件
├── .gitignore             # Git忽略文件
├── README.md              # 项目说明
├── src/                   # 源代码
│   ├── __init__.py
│   └── main.py
├── tests/                 # 测试文件
├── docs/                  # 文档
├── requirements.txt       # Python依赖
└── .github/              # GitHub配置
    └── workflows/        # GitHub Actions
```

### 2. README.md模板
```markdown
# 项目名称

## 项目描述
简要描述项目的目的和功能。

## 安装说明
```bash
git clone https://github.com/用户名/仓库名.git
cd 仓库名
pip install -r requirements.txt
```

## 使用方法
描述如何使用项目。

## 贡献指南
说明如何贡献代码。

## 许可证
项目许可证信息。
```

### 3. GitHub Actions配置
创建 `.github/workflows/ci.yml`：

```yaml
name: CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.11'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    
    - name: Run tests
      run: |
        python -m pytest tests/
```

## 常见问题解决

### 1. 推送被拒绝
```bash
# 先拉取远程更改
git pull origin main

# 解决冲突后再次推送
git push origin main
```

### 2. 忘记提交文件
```bash
# 添加遗漏的文件
git add 遗漏的文件

# 修改最后一次提交
git commit --amend --no-edit
```

### 3. 撤销错误的提交
```bash
# 撤销最后一次提交
git revert HEAD

# 或者重置到指定提交
git reset --hard 提交哈希
```

### 4. 恢复删除的文件
```bash
# 查看删除的文件
git log --diff-filter=D --summary

# 恢复文件
git checkout 提交哈希 -- 文件路径
```

## 最佳实践

### 1. 提交信息规范
- 使用清晰的提交信息
- 遵循约定式提交格式：
  - `feat:` 新功能
  - `fix:` 修复bug
  - `docs:` 文档更新
  - `style:` 代码格式调整
  - `refactor:` 代码重构
  - `test:` 测试相关
  - `chore:` 构建过程或辅助工具的变动

### 2. 分支命名规范
- `main` - 主分支
- `develop` - 开发分支
- `feature/功能名` - 功能分支
- `bugfix/问题描述` - 修复分支
- `hotfix/紧急修复` - 紧急修复分支

### 3. 工作流程建议
1. 始终从最新代码开始工作
2. 经常提交，小步快跑
3. 及时推送代码到远程仓库
4. 使用有意义的提交信息
5. 定期清理已合并的分支

### 4. 安全注意事项
- 不要在代码中提交敏感信息
- 使用环境变量管理配置
- 定期更新依赖包
- 启用GitHub的安全功能

## 总结

通过本指南，您应该能够：

1. ✅ 正确安装和配置Git
2. ✅ 设置GitHub账户和SSH密钥
3. ✅ 在Cursor中使用Git进行版本控制
4. ✅ 管理项目分支和合并
5. ✅ 参与协作开发
6. ✅ 解决常见问题
7. ✅ 遵循最佳实践

### 验证清单
- [ ] Git安装并配置
- [ ] GitHub账户设置完成
- [ ] SSH密钥配置成功
- [ ] 本地仓库初始化
- [ ] 远程仓库连接
- [ ] 首次提交和推送
- [ ] 分支管理测试
- [ ] 协作流程了解

祝您开发愉快！

---

**注意**：本指南基于Windows系统编写，其他操作系统可能需要调整命令和路径。 