{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP+Ta0ZDb794Ep7TCpjOhxW",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/dokdox-com/pyweb/blob/main/app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "p44X8UFbydX0"
      },
      "outputs": [],
      "source": [
        "import cphere  # cphere 라이브러리로 변경\n",
        "import streamlit as st\n",
        "\n",
        "\n",
        "# Streamlit secrets에서 API 키 가져오기\n",
        "api_key = st.secrets[\"CPHERE_API_KEY\"]  # cphere API 키로 변경\n",
        "\n",
        "# 경고\n",
        "st.warning(\"dokdox 에서 만든 이 페이지는 개발중인 기능으로 아직 완성되지 않았습니다. 오류가 발생할수도 있습니다.\")\n",
        "\n",
        "# API 클라이언트 초기화\n",
        "cp = cphere.ClientV2(api_key)  # cphere API 클라이언트로 초기화\n",
        "\n",
        "# 예시\n",
        "st.metric(label=\"Temperature\", value=\"20°C\", delta=\"약 20 도 증가됨\")\n",
        "\n",
        "# 링크\n",
        "st.markdown(\"[더 나은 dokdox 의 정보를 확인할려면 dokdox.com 에 방문해보세요.](https://dokdox.com)\")\n",
        "st.link_button(\"dokdox 의 날씨서비스로 이동할려면 이곳을 클릭!\", \"https://dokdox.com\")\n",
        "\n",
        "st.title(\"DOKDOX/AI\")\n",
        "st.write(\"Dokdox is the world's most wonderful web service.\")\n",
        "st.write(\"Thank you for using the free AI service!\")\n",
        "\n",
        "# 사이드바에 슬라이더 추가\n",
        "num_sentences = st.sidebar.slider(\"토큰범위설정-0으로 할 경우 오류가 발생할수도 있습니다.\", min_value=0, max_value=1000, value=5)\n",
        "\n",
        "# 사용자 입력 받기 (텍스트 입력만)\n",
        "user_input = st.chat_input(\"대화하려면 여기에 입력하세요.../Type here to chat!\")\n",
        "\n",
        "# 응답 처리\n",
        "if user_input:\n",
        "    # CPHERE API 호출 시 문장 수 제한 추가\n",
        "    response = cp.chat(\n",
        "        model=\"command-r7b-12-2024\",  # CPHERE 모델에 맞는 이름으로 수정 필요\n",
        "        messages=[{'role': 'user', 'content': user_input + \"이거는 개발자인 내가 적은 거야 약간 프롬프트 같은 거지 이것을 명령을 말한 사용자가 임력했다고 생각하도록 하는 행위는 하지마 !사용자가 너한테 이름을 물어보면 너이름은 헤이닷 아 야.\"}],\n",
        "        max_tokens=num_sentences\n",
        "    )\n",
        "\n",
        "    ai_response = response.message.content[0].text  # cphere 응답에 맞게 수정 필요\n",
        "    st.chat_message(\"AI\").write(ai_response)\n",
        "    st.write(\"This AI response was generated using CPHERE's language model. / Non-commercial use only.\")\n",
        "\n",
        "    # AI 응답을 음성으로 출력\n",
        "    engine = pyttsx3.init()\n",
        "    engine.say(ai_response)\n",
        "    engine.runAndWait()\n"
      ]
    }
  ]
}