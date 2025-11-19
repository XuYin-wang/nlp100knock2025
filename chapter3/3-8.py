# 28. MediaWikiマークアップの除去
# 27の処理に加えて、テンプレートの値からMediaWikiマークアップを可能な限り除去し、国の基本情報を整形せよ。

import requests
import re
def remove_mediawiki_markup(text):
    # 強調マークアップの除去
    text = re.sub(r"''+", "", text)
    # 内部リンクの除去
    text = re.sub(r"\[\[([^|\]]+\|)?([^\]]+)\]\]", r"\2", text)
    # 外部リンクの除去
    text = re.sub(r"\[([^ ]+ )?([^\]]+)\]", r"\2", text)
    # HTMLタグの除去
    text = re.sub(r"<[^>]+>", "", text)
    return text
# 国の基本情報を取得する関数
def get_country_info(country_name):
    url = f"https://ja.wikipedia.org/w/api.php"
    # APIパラメータ
    params = {
        "action": "query",
        "titles": country_name,
        "prop": "revisions",
        "rvprop": "content",
        "format": "json"
    }
    # ユーザーエージェントを設定
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15"
    }
    # APIリクエスト
    r = requests.get(url, params=params, headers=headers, timeout=10)
    data = r.json()
    pages = data["query"]["pages"]
    page = next(iter(pages.values()))
    content = page["revisions"][0]["*"]
    # 基本情報テンプレートの抽出
    match = re.search(r"\{\{基礎情報 国(.*?)\n\}\}", content, re.DOTALL)
    if not match:
        return None
    info_template = match.group(1)
    info_dict = {}
    for line in info_template.split("\n|"):
        if "=" in line:
            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip()
            value = remove_mediawiki_markup(value)
            info_dict[key] = value
    return info_dict
# テスト：日本の基本情報
if __name__ == "__main__":
    country = "イギリス"
    info = get_country_info(country)
    for key, value in info.items():
        print(f"{key}: {value}")
