# kuso_omikuji_streamlit.py
import streamlit as st
import random
import time
from datetime import datetime

st.set_page_config(page_title="🔮 おみくじ (Web)", layout="centered")

FORTUNES = [
    "超不運大吉：宝くじ買うな（買っても当たらない）",
    "微妙な中吉：メールの既読をつけ忘れる運",
    "普通の小吉：冷蔵庫に何かある気がするが無い",
    "不運凶：鍵を失くす可能性高め（予備の鍵を持たないで）",
    "謎の半吉：明日の予定が何故か消える",
    "無限ループ吉：その問題は永遠に終わらない",
    "運命はあなた次第（という名の丸投げ）",
    "爆笑大凶：今日の笑いはあなたが原因かも",
    "やる気微増：コーヒーを飲めば 0.2% 効果あり",
    "不可思議吉：猫に好かれる確率アップ（ただし猫次第）"
]

TIPS = [
    "靴下の左右を逆に履いてみると世界が変わる…かも",
    "メールの最後に『よろしくお草』と書くと縁起が良い（？）",
    "3回深呼吸してから冷蔵庫を開けると幸せが見つかる確率上昇",
    "今日の運勢はあなたの靴紐の結び方で決まる"
]

st.title("🔮 おみくじジェネレータ")
st.caption("ジョークアプリです。実用性は期待しないでね。")

name = st.text_input("お名前（任意）", value="名無し")
col1, col2 = st.columns([2,1])

with col1:
    if st.button("おみくじを引く（超真剣）"):
        with st.spinner("シャッフルしてます..."):
            time.sleep(0.8)
            fortune = random.choice(FORTUNES)
            tip = random.choice(TIPS) if random.random() < 0.6 else ""
            score = random.randint(-100, 100)
            ts = datetime.now().isoformat(sep=" ", timespec="seconds")
            display = f"**{fortune}**\n\n{tip}\n\n**幸福度:** {score}\n\n（{ts}）"
            st.markdown(display)
            st.session_state["last_result"] = {
                "name": name,
                "fortune": fortune,
                "tip": tip,
                "score": score,
                "timestamp": ts
            }

with col2:
    st.write("SNS用テキスト")
    if "last_result" in st.session_state:
        lr = st.session_state["last_result"]
        sns_text = f"【おみくじ】 {lr['fortune']} / {lr['tip'] or 'アドバイスなし'} （幸福度 {lr['score']})"
        st.text_area("コピーして貼るだけ", value=sns_text, height=120)
    else:
        st.info("まずは『おみくじを引く』を押してね。")

st.markdown("---")
st.caption("Tip: このWeb版はブラウザで動きます。簡単に共有できるよ！")
