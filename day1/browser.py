import webbrowser

url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query="
keywords = ["아이유","수지","설현"]
for name in keywords:
  webbrowser.open(url + name)
