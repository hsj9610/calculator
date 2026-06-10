import streamlit as st
import math
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="다기능 계산기",
    page_icon="🧮",
    layout="centered"
)

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
