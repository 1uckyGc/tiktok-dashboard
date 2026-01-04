import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime, timedelta

# ==========================================
# 1. 页面配置 (模拟出海酱的暗色风格)
# ==========================================
st.set_page_config(page_title="TikTok Growth Engine", layout="wide", page_icon="📊")

# 模拟 CSS 样式，还原暗黑极简风
st.markdown("""
<style>
    .stApp { background-color: #0e1117; color: white; }
    div[data-testid="metric-container"] {
        background-color: #1e1e1e;
        border: 1px solid #333;
        padding: 15px;
        border-radius: 5px;
        color: white;
    }
    h1, h2, h3 { color: white !important; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. 模拟 TikTok API 数据 (后端接口层)
# ==========================================
def get_tiktok_data(days=14):
    """
    这里未来替换为真实的 request.get(TIKTOK_API_URL)
    目前使用 Mock 数据模拟 API 返回的 JSON 结构
    """
    dates = pd.date_range(end=datetime.today(), periods=days)
    
    # 模拟每日数据
    data = pd.DataFrame({
        "Date": dates,
        "Views": np.random.randint(1000, 50000, size=days), # 播放量
        "Likes": np.random.randint(100, 5000, size=days),   # 点赞
        "Comments": np.random.randint(10, 500, size=days)   # 评论
    })
    
    # 模拟 Top 视频数据
    top_videos = [
        {"title": "三防枕套防水测试", "views": "1.2M", "ctr": "5.4%", "score": 98},
        {"title": "厨房去油污神器", "views": "850K", "ctr": "4.2%", "score": 92},
        {"title": "车内清洁沉浸式", "views": "420K", "ctr": "3.8%", "score": 85},
    ]
    
    return data, top_videos

# ==========================================
# 3. 前端 UI 构建 (复刻截图)
# ==========================================

# --- 顶部导航与筛选 ---
col1, col2 = st.columns([3, 1])
with col1:
    st.title("📊 TikTok 账号数据看板")
    st.caption("连接你的 TikTok 账号，即可查看播放、互动和热门内容。")
with col2:
    st.button("➕ 连接新账号", type="primary")

# 筛选栏
st.selectbox("平台", ["TikTok", "Instagram", "YouTube"], index=0)
time_range = st.selectbox("时间范围", ["最近 7 天", "最近 14 天", "最近 30 天"], index=1)

# 获取数据
df, top_videos = get_tiktok_data(days=14)

# --- 核心指标卡 (Key Metrics) ---
st.markdown("### 数据总览")
m1, m2, m3, m4 = st.columns(4)
m1.metric("已发布视频", "12", "+2")
m2.metric("活跃账号", "3", "0")
m3.metric("总播放量", f"{df['Views'].sum():,}", "+15%")
m4.metric("总互动 (点赞+评论)", f"{df['Likes'].sum() + df['Comments'].sum():,}", "+8%")

# --- 趋势图表区 ---
st.markdown("---")
c1, c2 = st.columns(2)

with c1:
    st.subheader("📈 播放量趋势 (Views)")
    fig_views = px.line(df, x='Date', y='Views', markers=True, template="plotly_dark")
    fig_views.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig_views, use_container_width=True)

with c2:
    st.subheader("❤️ 互动趋势 (Engagement)")
    fig_eng = px.line(df, x='Date', y=['Likes', 'Comments'], markers=True, template="plotly_dark")
    fig_eng.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig_eng, use_container_width=True)

# --- Top 视频与 AI 诊断 (核心差异化功能) ---
st.markdown("---")
t1, t2 = st.columns([2, 1])

with t1:
    st.subheader("🔥 Top 热门视频")
    # 渲染成表格
    st.dataframe(
        pd.DataFrame(top_videos),
        column_config={
            "score": st.column_config.ProgressColumn("AI 推荐分", format="%d", min_value=0, max_value=100)
        },
        use_container_width=True
    )

with t2:
    st.subheader("🤖 Agent 实时诊断")
    st.info("AI 正在分析 API 数据...")
    
    # 这里模拟 Agent 的输出
    latest_trend = "播放量上升" if df['Views'].iloc[-1] > df['Views'].iloc[-2] else "播放量下降"
    st.write(f"**数据洞察**：过去 14 天账号{latest_trend}。")
    st.write("**优化建议**：")
    st.success("检测到 '三防枕套' 视频完播率极高。建议立即复刻该脚本的 '暴力测试' 片段，并发布到 Instagram Reels。")
    
    if st.button("生成优化脚本"):
        st.write("📝 正在调用 GPT-4 生成脚本...")
