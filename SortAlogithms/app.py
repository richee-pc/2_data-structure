import streamlit as st
import os

def main():
    # HTML 파일 경로 설정 (app.py와 같은 디렉토리에 있다고 가정)
    html_file_path = os.path.join(os.path.dirname(__file__), "sorting_algorithms.html")

    try:
        with open(html_file_path, "r", encoding="utf-8") as f:
            html_content = f.read()
    except FileNotFoundError:
        st.error(f"HTML 파일을 찾을 수 없습니다: {html_file_path}")
        st.info("HTML 파일이 'app.py'와 같은 디렉토리에 있는지 확인하고, 파일명이 'sorting_algorithms.html'인지 확인해주세요.")
        return

    # st.components.v1.html을 사용하여 HTML 콘텐츠를 Streamlit 앱에 렌더링
    # height와 scrolling을 'True'로 설정하여 HTML 콘텐츠가 잘리지 않고 스크롤 가능하도록 함
    st.components.v1.html(html_content, height=800, scrolling=True)

if __name__ == "__main__":
    main()

