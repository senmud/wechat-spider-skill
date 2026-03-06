# WeChat Spider Skill 🕷️

针对微信公众号文章的专用抓取技能。当普通的 `web_fetch` 或 `browser` 被反爬验证码拦截时使用。

## 🛠️ 核心能力
- 模拟 iPhone 微信客户端常用 User-Agent。
- 精确提取 `#js_content` 容器中的正文，过滤干扰脚本。
- 支持处理编码问题，确保中文不乱码。

## 📖 使用指南

使用 `exec` 工具运行脚本（推荐使用绝对路径）：

```bash
python3 /root/.nanobot/workspace/skills/wechat-spider/scripts/fetch_wechat.py "URL"
# 或者
python3 /root/.nanobot/workspace/skills/wechat-spider/scripts/fetch_wechat.py --url "URL"
```

## ⚠️ 注意事项
- 本工具仅限获取公开文章内容。
- 若提示“环境异常”，说明 UA 已被微信标记，需更新 `headers` 中的 `User-Agent`。
- 该工具不处理图片抓取，仅限提取文字。
