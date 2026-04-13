---
name: wechat-spider
version: 0.1.1
description: "小雪安全 (Xiaoxue Security) 专用微信公众号文章抓取工具。模拟移动端 UA，精准提取正文，绕过基础反爬。"
author: "Xiaoxue Security"
repository: "https://github.com/senmud/wechat-spider-skill"
metadata: {"nanobot":{"emoji":"🕷️"}}
---

# WeChat Spider (小雪微信情报官) 🕷️

针对微信公众号文章的专用抓取技能。当普通的 `web_fetch` 或 `browser` 被反爬验证码拦截时使用。

## 🛠️ 核心能力
- **UA 伪装**: 模拟 iPhone 微信客户端常用 User-Agent。
- **精准提取**: 精确提取 `#js_content` 容器中的正文，过滤干扰脚本。
- **编码优化**: 自动处理微信特有的编码问题，确保中文不乱码。

## 📖 使用指南

### 抓取文章正文
```bash
python3 scripts/fetch_wechat.py "https://mp.weixin.qq.com/s/..."
```

## 🛡️ 安全声明
本工具由 **小雪安全 (Xiaoxue Security)** 提供，仅限用于公开情报获取。严禁用于非法抓取或侵犯隐私。
