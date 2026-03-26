import streamlit as st
from crewai import Crew, Agent, Task
from dotenv import load_dotenv

load_dotenv()

# --- 1. SET UP GIAO DIỆN (UI) CƠ BẢN ---
st.set_page_config(page_title="CrewAI Chatbot", page_icon="🤖")
st.title("🤖 Chatbot trợ lý chuyên sâu - Powered by CrewAI")

# Hàm khởi tạo CrewAI (chạy mỗi khi có người hỏi)
def run_crewai_process(user_input):
    # Khai báo Agent
    researcher = Agent(
        role='Nhà nghiên cứu bách khoa',
        goal='Tìm hiểu thông tin đa chiều',
        backstory='Bạn là bộ bách khoa toàn thư...',
        llm='Gemini 2.5 flash' # Mô hình của bạn
    )
    
    # Khai báo Task (Sử dụng biến {user_input} ở đây)
    answer_task = Task(
        description='Trả lời câu hỏi của người dùng một cách chính xác nhất. Câu hỏi: {user_input}',
        expected_output='Câu trả lời định dạng chuẩn Markdown.',
        agent=researcher
    )
    
    # Khai báo Crew
    crew = Crew(
        agents=[researcher],
        tasks=[answer_task],
        verbose=False # Set True nếu bạn muốn xem log trên Terminal
    )
    
    # Chạy Crew với đầu vào từ người dùng
    result = crew.kickoff(inputs={"user_input": user_input})
    return result

# --- 2. XỬ LÝ LƯU TRỮ LỊCH SỬ CHAT TRÊN WEB ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Hiển thị lại các tin nhắn cũ
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- 3. XỬ LÝ KHI NGƯỜI DÙNG NHẬP TIN NHẮN MỚI ---
if prompt := st.chat_input("Hãy hỏi tôi bất cứ điều gì..."):
    # 1. In câu hỏi của User lên màn hình
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 2. Xử lý câu trả lời từ CrewAI
    with st.chat_message("assistant"):
        with st.spinner("Đội ngũ AI đang làm việc..."): 
            # Gọi CrewAI
            final_answer = run_crewai_process(prompt)
            st.markdown(final_answer)
    
    # 3. Lưu câu trả lời vào lịch sử
    st.session_state.messages.append({"role": "assistant", "content": final_answer})
