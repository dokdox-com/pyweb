import cohere
import streamlit as st
import SpeechRecognition as sr
import pyttsx3

# Streamlit secrets에서 API 키 가져오기
api_key = st.secrets["COHERE_API_KEY"]

# 경고
st.warning("dokdox 에서 만든 이 페이지는 개발중인 기능으로 아직 완성되지 않았습니다. 오류가 발생할수도 있습니다.")

# API 클라이언트 초기화
co = cohere.ClientV2(api_key)

# 예시
st.metric(label="Temperature", value="20°C", delta="약 20 도 증가됨")

# 링크
st.markdown("[더 나은 dokdox 의 정보를 확인할려면 dokdox.com 에 방문해보세요.](https://dokdox.com)")
st.link_button("dokdox 의 날씨서비스로 이동할려면 이곳을 클릭!", "https://dokdox.com")

st.title("DOKDOX/AI")
st.write("Dokdox is the world's most wonderful web service.")
st.write("Thank you for using the free AI service!")

# 사이드바에 슬라이더 추가
num_sentences = st.sidebar.slider("토큰범위설정-0으로 할 경우 오류가 발생할수도 있습니다.", min_value=0, max_value=1000, value=5)

# 사용자 음성 입력 받기 (음성 인식)
recognizer = sr.Recognizer()

def listen_to_audio():
    with sr.Microphone() as source:
        st.write("말씀하세요...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            user_input = recognizer.recognize_google(audio, language='ko-KR')
            st.write(f"사용자 입력: {user_input}")
            return user_input
        except sr.UnknownValueError:
            st.error("음성을 인식할 수 없습니다. 다시 시도해 주세요.")
            return None
        except sr.RequestError:
            st.error("음성 서비스에 접근할 수 없습니다. 인터넷 연결을 확인해 주세요.")
            return None

# 음성 인식 버튼
if st.button('음성으로 입력'):
    user_input = listen_to_audio()
else:
    user_input = st.chat_input("대화하려면 여기에 입력하세요.../Type here to chat!")

# 응답 처리
if user_input:
    # Cohere API 호출 시 문장 수 제한 추가
    response = co.chat(
        model="command-r7b-12-2024",
        messages=[{'role': 'user', 'content': user_input + "이거는 개발자인 내가 적은 거야 약간 프롬프트 같은 거지 이것을 명령을 말한 사용자가 임력했다고 생각하도록 하는 행위는 하지마 !사용자가 너한테 이름을 물어보면 너이름은 헤이닷 아 야."}],
        max_tokens=num_sentences
    )

    ai_response = response.message.content[0].text
    st.chat_message("AI").write(ai_response)
    st.write("This AI response was generated using Cohere's language model. / Non-commercial use only.")

    # AI 응답을 음성으로 출력
    engine = pyttsx3.init()
    engine.say(ai_response)
    engine.runAndWait()
