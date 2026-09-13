import streamlit as st
import feedparser

# ======== 1. ページ設定とUI ========
st.set_page_config(page_title="最新IT・AIニュース", page_icon="📰", layout="centered")

st.title("📰 サクサク読める IT・AIニュース")
st.write("最新のニュース一覧です。気になった記事はリンクから確認できます。")

# ======== 2. ニュース取得処理 (10分キャッシュ) ========
# ttl=600で10分間（600秒）結果を保持し、アプリをサクサク動かします
@st.cache_data(ttl=600)
def fetch_news(feed_url):
    parsed = feedparser.parse(feed_url)
    return parsed.entries[:15]  # 最新の15件を取得

# IT系のRSSフィード（例としてYahoo!ニュースのIT・科学カテゴリ）
RSS_URL = "https://news.yahoo.co.jp/rss/topics/it.xml"
entries = fetch_news(RSS_URL)

# ======== 3. ニュース一覧の表示 ========
for entry in entries:
    # カード風のレイアウトを作成
    with st.container(border=True):
        st.subheader(entry.title)
        st.caption(f"配信日時: {entry.published}")
        
        # もしRSSに概要文が含まれていれば表示する（おまけ機能）
        if hasattr(entry, 'summary') and entry.summary:
            st.write(entry.summary)
            
        # 右寄せでリンクを配置
        col1, col2 = st.columns([3, 1])
        with col2:
            st.write(f"🔗 [元記事を読む]({entry.link})")