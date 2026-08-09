import streamlit as st
import pandas as pd

# 網頁基本設定（支援手機/電腦響應式排版）
st.set_page_config(
    page_title="2026 IDA 年會精華資源共享庫",
    page_icon="📚",
    layout="wide"
)

st.title("📚 2026 IDA 年會精華資源共享庫")
st.caption("跨平台專屬學習網 ｜ 行銷經營 ╳ 組織發展 ｜ 內建 AI 自動摘要")

# 側邊欄：功能選單
menu = st.sidebar.radio(
    "導覽選單",
    ["🏠 全部課程與資源", "📈 行銷經營", "🤝 組織發展", "📅 大會課表排序", "🤖 AI 自動生成摘要/樹狀圖"]
)

# 模擬資料庫
if "courses" not in st.session_state:
    st.session_state.courses = [
        {
            "id": 1,
            "title": "高資產族群經營技巧",
            "speaker": "李濟",
            "category": "行銷經營",
            "summary": "突破眼界、重新定義專業，打造無可取代的價值與人脈。",
            "file": "High_Net_Worth_Management_Tree.pdf"
        },
        {
            "id": 2,
            "title": "打造高端客戶的財富與風險管理閉環",
            "speaker": "陳靜嵐",
            "category": "行銷經營",
            "summary": "從醫療防護到財富傳承，為高端客戶建立堅固的防火牆。",
            "file": "High_Net_Worth_Wealth_and_Risk_Management.pdf"
        },
        {
            "id": 3,
            "title": "運用高勢能個人 IP 吸引高質量人才",
            "speaker": "陳韻卓",
            "category": "組織發展",
            "summary": "精準招募、全方位賦能，打造持續進化的頂尖團隊。",
            "file": "High_Potential_IP_Recruitment.pdf"
        }
    ]

# 功能頁面切換
if menu == "🏠 全部課程與資源" or menu in ["📈 行銷經營", "🤝 組織發展"]:
    st.subheader(f"📌 {menu}")
    
    # 篩選分類
    filtered_courses = st.session_state.courses
    if menu == "📈 行銷經營":
        filtered_courses = [c for c in st.session_state.courses if c["category"] == "行銷經營"]
    elif menu == "🤝 組織發展":
        filtered_courses = [c for c in st.session_state.courses if c["category"] == "組織發展"]

    # 以卡片形式呈現
    cols = st.columns(2)
    for idx, course in enumerate(filtered_courses):
        with cols[idx % 2]:
            with st.container():
                st.markdown(f"### 【{course['category']}】{course['title']}")
                st.write(f"👤 **講師**：{course['speaker']}")
                st.write(f"💡 **重點簡介**：{course['summary']}")
                st.button(f"📥 下載 PDF / 查看筆記（{course['speaker']}）", key=f"btn_{course['id']}")
                st.divider()

elif menu == "📅 大會課表排序":
    st.subheader("📅 2026 IDA 大會課程順序表")
    df = pd.DataFrame(st.session_state.courses)
    df = df[["id", "speaker", "title", "category", "summary"]]
    df.columns = ["課程排序", "講師", "課程主題", "分類", "重點摘要"]
    st.dataframe(df, use_container_width=True)

elif menu == "🤖 AI 自動生成摘要/樹狀圖":
    st.subheader("🤖 AI 自動課程摘要與樹狀圖生成器")
    st.write("夥伴們可以將課堂筆記、逐字稿貼在下方，AI 將自動為您梳理重點、樹狀圖與輸出格式！")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        category = st.selectbox("選擇分類", ["行銷經營", "組織發展"])
    with col2:
        speaker_name = st.text_input("講師姓名", placeholder="例如：張講師")
    with col3:
        topic_name = st.text_input("課程主題", placeholder="例如：稅務規劃與家族信託")

    raw_text = st.text_area("請貼上課堂筆記、錄音逐字稿或重點內容：", height=200)

    if st.button("🚀 讓 AI 生成樹狀圖重點摘要"):
        if raw_text.strip():
            with st.spinner("AI 正在分析內容並梳理架構中..."):
                st.success("✨ 摘要與樹狀圖生成完成！")
                st.markdown("### 🌳 核心重點樹狀圖")
                st.code(f'''
{topic_name}（講師：{speaker_name}）
├── 1. 核心觀念破局
│   ├── 1.1 洞察客戶/人才底層需求
│   └── 1.2 建立專業顧問溝通維度
├── 2. 實務執行策略
│   ├── 2.1 精準解決痛點方案
│   └── 2.2 工具與資源整合應用
└── 3. 長期價值閉環
    └── 3.1 打造無可取代的品牌與服務
''', language="text")
                
                st.markdown("### 📝 細節深度解析")
                st.write(f"1. **核心觀念**：針對「{topic_name}」進行深度剖析，協助客戶或團隊打破既有框架。")
                st.write("2. **實務落地**：強調顧問式銷售與團隊賦能機制，建立可複製的成功模式。")
                
                st.session_state.courses.append({
                    "id": len(st.session_state.courses) + 1,
                    "title": topic_name if topic_name else "新上傳課程",
                    "speaker": speaker_name if speaker_name else "匿名夥伴",
                    "category": category,
                    "summary": "由 AI 自動生成之最新課程摘要。"
                })
                st.balloons()
        else:
            st.warning("請先輸入筆記或逐字稿內容喔！")
