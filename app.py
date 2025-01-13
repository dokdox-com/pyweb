import cohere
import streamlit as st

# Streamlit secrets에서 API 키 가져오기
api_key = st.secrets["COHERE_API_KEY"]



# API 클라이언트 초기화
co = cohere.ClientV2(api_key)

# 제목과 설명
st.title("Dokdox Free AI Service")
st.write("Dokdox is the world's most wonderful web service.")
st.write("Thank you for using the free AI service!")
st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
# 사용자 입력 받기
user_input = st.chat_input("대화하려면 여기에 입력하세요...")

# 응답 히스토리 초기화
if user_input:
    # Cohere API 호출
    response = co.chat(
        model="command-r7b-12-2024",  # 모델명
        messages=[{'role': 'user', 'content': user_input }]
    )
    st.chat_message("AI").write(response.message.content[0].text)
    st.write("This AI response was generated using Cohere's language model. / Non-commercial use only.")
