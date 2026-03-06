import requests
from bs4 import BeautifulSoup
import sys
import argparse

def fetch_wechat_article(url):
    """
    专门针对微信公众号文章的抓取脚本，使用伪装UA绕过反爬。
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1',
    }

    try:
        r = requests.get(url, headers=headers, timeout=15)
        r.raise_for_status()
        r.encoding = 'utf-8'
        
        soup = BeautifulSoup(r.text, 'html.parser')
        article = soup.find('div', {'id': 'js_content'})
        
        if not article:
            # 兼容性处理：如果 js_content 抓不到，返回提示
            if "环境异常" in r.text:
                return "ERROR: Detected Anti-Crawler Verification (环境异常). UA might need rotation."
            return "ERROR: Could not find js_content container."
            
        return article.get_text(separator='\n').strip()

    except Exception as e:
        return f"ERROR: {str(e)}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="WeChat Article Spider")
    parser.add_argument("url", nargs="?", help="The URL of the WeChat article")
    parser.add_argument("--url", dest="url_opt", help="The URL of the WeChat article (optional flag)")
    args = parser.parse_args()
    
    target_url = args.url or args.url_opt
    if not target_url:
        print("ERROR: No URL provided.")
        sys.exit(1)
    
    print(fetch_wechat_article(target_url))
