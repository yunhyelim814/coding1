import streamlit as st

# --- PAGE SETUP ---
# https://fonts.google.com/icons
about_page = st.Page(
    page="views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)
project_1_page = st.Page(
    page="views/sales_dashboard.py",
    title="Sales Dashboard",
    icon=":material/bar_chart:",
)
project_2_page = st.Page(
    page="views/chatbot.py",
    title="Chat Bot",
    icon=":material/smart_toy:",
)

test1_page = st.Page(
    page="views/test1.py",
    title="텍스트",
    icon=":material/sentiment_satisfied:",
)
test2_page = st.Page(
    page="views/test2.py",
    title="위젯",
    icon=":material/sentiment_satisfied:",
)
test3_page = st.Page(
    page="views/coin_game.py",
    title="동전 던지기 게임",
    icon=":material/sentiment_satisfied:",
)
test4_page = st.Page(
    page="views/bmi_calc.py",
    title="체질량지수 BMI 계산",
    icon=":material/sentiment_satisfied:",
)
test5_page = st.Page(
    page="views/bibimbap.py",
    title="비빔밥 주문",
    icon=":material/sentiment_satisfied:",
)

graph1_page = st.Page(
    page="views/graph_matplotlib_1.py",
    title="맷플롯립 그래프 연습",
    icon=":material/sentiment_satisfied:",
)
graph2_page = st.Page(
    page="views/graph_pizza_chicken.py",
    title="피자 vs 치킨",
    icon=":material/sentiment_satisfied:",
)
graph3_page = st.Page(
    page="views/graph_price.py",
    title="간식의 가격 변화",
    icon=":material/sentiment_satisfied:",
)


# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS] ---
pg = st.navigation({
    "Info": [about_page],
    "Projects": [project_1_page, project_2_page],
    "스트림릿 연습": [test1_page, test2_page, test3_page, test4_page, test5_page],
    "데이터 시각화": [graph1_page, graph2_page, graph3_page],
})

# --- SHARED ON ALL PAGES ---
st.logo("assets/myLogo.png")
st.sidebar.text("Made with ❤ by SW")

# --- RUN NAVIGATION ---
pg.run()
