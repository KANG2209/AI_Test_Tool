# AI测试用例生成工具

一个基于AI模型的自动化测试用例生成工具，支持使用本地Ollama模型和在线API模型。

## 功能特点

- 支持本地Ollama模型（deepseekr1:1.5和qwen1.8）
- 支持在线API模型（如OpenAI）
- 自动从需求文档生成测试用例
- 可视化界面操作
- 支持测试用例导出

## 安装要求

1. Python 3.7+
2. 本地Ollama服务（可选，用于使用本地模型）
3. 相关依赖包

## 配置说明

### 1. 配置文件 (`config.ini`)

配置文件包含模型相关的设置：

```ini
[model]
api_key = # 在线模型API密钥
model_name = gpt-3.5-turbo
max_tokens = 2048
temperature = 0.7

[ollama]
enable = true
model_name = deepseekr1:1.5
api_base = http://localhost:11434/v1
```

- `api_key`：在线模型的API密钥（如OpenAI API密钥）
- `model_name`：使用的模型名称
- `ollama.enable`：是否启用本地Ollama模型
- `ollama.model_name`：本地Ollama模型名称
- `ollama.api_base`：Ollama服务地址

### 2. 系统提示文件

- `TESTCASE_READER_SYSTEM_MESSAGE.txt`：测试用例读取器系统提示
- `TESTCASE_WRITER_SYSTEM_MESSAGE.txt`：测试用例生成器系统提示

## 使用方法

### 1. 启动应用

直接运行 `page.py` 文件：

```bash
python page.py
```

或使用编译好的可执行文件：

```bash
run.exe
```

**run.exe 文件位置**：

- 可通过 GitHub Releases 页面下载：<https://github.com/KANG2209/AI_Test_Tool/releases>
- 下载后直接运行即可，无需安装Python环境

### 2. 生成测试用例

1. 在界面中输入需求描述或上传需求文档
2. 选择使用的模型（本地Ollama或在线API）
3. 点击「生成测试用例」按钮
4. 查看生成的测试用例结果

### 3. 导出测试用例

生成测试用例后，可以将结果导出为文本文件。

## 本地Ollama模型配置

1. 安装Ollama：<https://ollama.com/download>
2. 下载模型：
   ```bash
   ollama pull deepseekr1:1.5
   ollama pull qwen1.8
   ```
3. 启动Ollama服务（默认地址：<http://localhost:11434）>
4. 在配置文件中设置 `ollama.enable = true` 并选择对应的模型

## 项目结构

```
AITestTool/
├── img/              # 图片资源
├── config.ini        # 配置文件
├── llms.py           # 模型管理
├── ollama_client.py  # Ollama客户端
├── page.py           # 主界面
├── TESTCASE_READER_SYSTEM_MESSAGE.txt  # 读取器系统提示
├── TESTCASE_WRITER_SYSTEM_MESSAGE.txt  # 生成器系统提示
├── 需求文档示例.txt    # 需求文档示例
└── README.md         # 项目说明
```

## 运行示例

1. 启动应用
2. 输入需求描述，例如：
   ```
   用户注册功能：
   1. 支持手机号注册
   2. 支持邮箱注册
   3. 密码长度至少8位
   4. 需要验证码验证
   ```
3. 选择使用本地Ollama模型
4. 点击「生成测试用例」
5. 查看生成的测试用例

## 注意事项

1. 使用在线API模型需要配置有效的API密钥
2. 使用本地Ollama模型需要确保Ollama服务正在运行
3. 生成测试用例的质量取决于模型的能力和需求描述的清晰度

## 常见问题

### Q: 本地Ollama模型无法连接

A: 请检查Ollama服务是否正在运行，默认地址为 <http://localhost:11434>

### Q: 在线API模型报错

A: 请检查API密钥是否正确，以及网络连接是否正常

### Q: 生成的测试用例质量不高

A: 尝试提供更详细的需求描述，或切换到更高级的模型


