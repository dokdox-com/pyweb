import cohere
import streamlit as st

# Streamlit secrets에서 API 키 가져오기
api_key = st.secrets["COHERE_API_KEY"]



# API 클라이언트 초기화
co = cohere.ClientV2(api_key)

#예시
st.metric(label="Temperature", value="20°C", delta="약 20 도 증가됨")
#링크
st.markdown("[더 나은 dokdox 의 정보를 확인할려면 dokdox.com 에 방문해보세요.](https://dokdox.com)")
st.link_button("dokdox 의 날씨서비스로 이동할려면 이곳을 클릭!", "https://dokdox.com")

st.title("Dokdox Free AI Service")
st.write("Dokdox is the world's most wonderful web service.")
st.write("Thank you for using the free AI service!")

# 사용자 입력 받기
user_input = st.chat_input("대화하려면 여기에 입력하세요.../Type here to chat!")
# 사이드바에 슬라이더 추가
n = st.sidebar.slider("응답메시지 길이 설정--만약 너무 잛거나 길게 하면 응답오류가 발생할수도 있습니다!:(단위:문장)", 0, 100, 50)
# 응답 히스토리 초기화
if user_input:
    # Cohere API 호출
    response = co.chat(
        model="command-r7b-12-2024",  # 모델명
        messages=[{'role': 'user', 'content': user_input + n +"문장 보다 길게 메시지를 작성해줄래." }]
    )
    st.chat_message("AI").write(response.message.content[0].text)
    st.write("This AI response was generated using Cohere's language model. / Non-commercial use only.")














# Additional content in the main area
st.write("This is some content displayed regardless of the sidebar selection.")