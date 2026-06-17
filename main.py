import streamlit as st
import math
import numpy as np
import matplotlib.pyplot as plt
import time

st.set_page_config(
    page_title="다기능 계산기",
    page_icon="🧮",
    layout="centered"
)

# 멋진 배경 이미지 URL 리스트 (건축물, 자연풍경 등이 골고루 어우러짐)
background_images = [
    "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=1200&h=800&fit=crop",  # 산 풍경
    "https://images.unsplash.com/photo-1480714378408-67cf0d13bc1b?w=1200&h=800&fit=crop",  # 도시 야경
    "https://images.unsplash.com/photo-1469022563149-aa64dbd37dae?w=1200&h=800&fit=crop",  # 자연 숲
    "https://images.unsplash.com/photo-1449824913935-59a10b8d2000?w=1200&h=800&fit=crop",  # 현대 건축물
    "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=1200&h=800&fit=crop",  # 풍경
    "https://images.unsplash.com/photo-1486299967070-08de976cb1d8?w=1200&h=800&fit=crop",  # 도시 건축
    "https://images.unsplash.com/photo-1519904981063-b0cf448d479e?w=1200&h=800&fit=crop",  # 자연 호수
    "https://images.unsplash.com/photo-1479839672679-a46482f0e7c8?w=1200&h=800&fit=crop",  # 도시 풍경
    "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=1200&h=800&fit=crop",  # 산봉우리
    "https://images.unsplash.com/photo-1470114716159-e389f8712fda?w=1200&h=800&fit=crop",  # 현대 건축
]

# 현재 시간을 기반으로 배경이미지 선택 (5초마다 변경)
current_image_index = int(time.time() / 5) % len(background_images)
current_background = background_images[current_image_index]

# CSS로 배경이미지 적용
st.markdown(f"""
    <style>
        .stApp {{
            background-image: url('{current_background}');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            transition: background-image 0.5s ease-in-out;
        }}
        body {{
            background-image: url('{current_background}');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        /* 콘텐츠 가독성을 위한 반투명 배경 */
        [data-testid="stVerticalBlock"] > div {{
            background-color: rgba(255, 255, 255, 0.95);
            border-radius: 10px;
            padding: 20px;
            margin: 10px 0;
        }}
        .element-container {{
            background-color: rgba(255, 255, 255, 0.95);
            border-radius: 10px;
            padding: 15px;
        }}
        h1, h2, h3 {{
            color: #1f77b4;
        }}
    </style>
    """, unsafe_allow_html=True)

# 페이지 새로고침 (5초마다)
st.markdown("""
    <script>
        setInterval(function() {{
            location.reload();
        }}, 5000);
    </script>
    """, unsafe_allow_html=True)

st.title("🧮 다기능 계산기 웹앱")
st.write("사칙연산 / 모듈러 / 지수 / 로그 계산 / 함수 그래프")

# 기능 선택
operation = st.selectbox(
    "기능을 선택하세요",
    [
        "덧셈",
        "뺄셈",
        "곱셈",
        "나눗셈",
        "모듈러 연산 (%)",
        "지수 연산",
        "로그 연산",
        "함수 그래프"
    ]
)

# ------------------------
# 함수 그래프
# ------------------------
if operation == "함수 그래프":

    st.subheader("📈 함수 그래프 그리기")

    st.write("쉼표(,)로 여러 함수를 입력할 수 있습니다.")
    st.write("예시: x**2, x**3, np.sin(x), np.cos(x)")

    functions_input = st.text_input(
        "함수 입력",
        value="x**2"
    )

    x_min = st.number_input(
        "x 최소값",
        value=-10.0
    )

    x_max = st.number_input(
        "x 최대값",
        value=10.0
    )

    if st.button("그래프 그리기"):

        try:
            if x_min >= x_max:
                st.error("x 최소값은 x 최대값보다 작아야 합니다.")
                st.stop()

            x = np.linspace(x_min, x_max, 1000)

            functions = [
                f.strip()
                for f in functions_input.split(",")
                if f.strip()
            ]

            fig, ax = plt.subplots(figsize=(8, 5))

            for function in functions:

                y = eval(
                    function,
                    {
                        "__builtins__": {},
                        "np": np,
                        "x": x,
                        "sin": np.sin,
                        "cos": np.cos,
                        "tan": np.tan,
                        "log": np.log,
                        "sqrt": np.sqrt,
                        "exp": np.exp,
                        "pi": np.pi
                    }
                )

                ax.plot(
                    x,
                    y,
                    label=f"y = {function}"
                )

            ax.set_title("함수 그래프")
            ax.set_xlabel("x")
            ax.set_ylabel("y")
            ax.grid(True)
            ax.legend()

            st.pyplot(fig)

        except Exception as e:
            st.error(f"그래프를 그릴 수 없습니다: {e}")

# ------------------------
# 로그 연산
# ------------------------
elif operation == "로그 연산":

    value = st.number_input(
        "로그를 구할 숫자",
        value=1.0
    )

    base = st.number_input(
        "밑(base)",
        value=10.0
    )

    if st.button("계산하기"):

        try:
            if value <= 0:
                st.error("로그의 진수는 0보다 커야 합니다.")
                st.stop()

            if base <= 0 or base == 1:
                st.error("밑은 0보다 크고 1이 아니어야 합니다.")
                st.stop()

            result = math.log(value, base)

            st.success(
                f"log{base}({value}) = {result}"
            )

        except Exception as e:
            st.error(f"오류 발생: {e}")

# ------------------------
# 사칙연산 / 모듈러 / 지수
# ------------------------
else:

    num1 = st.number_input(
        "첫 번째 숫자",
        value=0.0
    )

    num2 = st.number_input(
        "두 번째 숫자",
        value=0.0
    )

    if st.button("계산하기"):

        try:
            if operation == "덧셈":
                result = num1 + num2

            elif operation == "뺄셈":
                result = num1 - num2

            elif operation == "곱셈":
                result = num1 * num2

            elif operation == "나눗셈":

                if num2 == 0:
                    st.error("0으로 나눌 수 없습니다.")
                    st.stop()

                result = num1 / num2

            elif operation == "모듈러 연산 (%)":

                if num2 == 0:
                    st.error(
                        "0으로 나눈 나머지는 계산할 수 없습니다."
                    )
                    st.stop()

                result = num1 % num2

            elif operation == "지수 연산":
                result = num1 ** num2

            st.success(f"결과: {result}")

        except Exception as e:
            st.error(f"오류 발생: {e}")
