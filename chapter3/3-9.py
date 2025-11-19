# 29. 国旗画像のURLを取得する
# テンプレートの内容を利用し、国旗画像のURLを取得せよ。（ヒント: MediaWiki APIのimageinfoを呼び出して、ファイル参照をURLに変換すればよい）
import requests
import urllib.parse

def get_image_url(image_title):
    # 画像タイトル → "File:" を付ける
    title = "File:" + image_title

    # MediaWiki API endpoint
    url = "https://ja.wikipedia.org/w/api.php"

    params = {
        "action": "query",
        "titles": title,
        "prop": "imageinfo",
        "iiprop": "url",
        "format": "json"
    }
    # ユーザーエージェントを設定
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15"
    }
    # APIリクエスト
    r = requests.get(url, params=params, headers=headers, timeout=10)
    # JSONレスポンスを解析
    data = r.json()
    pages = data["query"]["pages"]
    page = next(iter(pages.values()))
    # 画像URLを取得
    return page["imageinfo"][0]["url"]


# テスト：英語の国旗
if __name__ == "__main__":
    image_name = "Flag_of_the_United_Kingdom.svg"
    url = get_image_url(image_name)
    print("国旗URL:", url)
