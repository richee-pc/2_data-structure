import streamlit as st
import os
import streamlit.components.v1 as components

# Streamlit 페이지 설정
st.set_page_config(layout="wide", page_title="정렬 알고리즘 시뮬레이터")

# HTML 파일의 경로를 지정합니다.
# 이 파일을 app_sorting.py와 같은 디렉토리에 두세요.
SORTING_HTML_FILE_PATH = "sorting_algorithms.html"

# HTML 파일을 읽어오는 함수
def load_html_file(file_path):
    # 파일이 존재하는지 확인
    if not os.path.exists(file_path):
        st.error(f"오류: HTML 파일이 '{file_path}' 경로에 없습니다. 파일을 업로드하거나 경로를 확인해주세요.")
        # 파일이 없으면 앱 실행을 중지하고 오류 메시지를 명확히 표시
        st.stop()
    
    with open(file_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    return html_content

st.title("정렬 알고리즘 교육 시뮬레이터 🧑‍💻")
st.write("다양한 정렬 알고리즘의 동작을 시뮬레이션을 통해 직접 확인하고 배워보세요!")

# 디버깅 정보 추가: 현재 작업 디렉토리 및 파일 목록 확인
st.info(f"현재 Streamlit 앱이 실행되는 경로: `{os.getcwd()}`")
st.info(f"현재 디렉토리의 파일 목록: `{os.listdir()}`")

st.header("정렬 알고리즘의 세계 🚀")
html_content = load_html_file(SORTING_HTML_FILE_PATH)
# height와 scrolling 속성은 필요에 따라 조절할 수 있습니다.
components.html(html_content, height=10000, scrolling=True) # 정렬 페이지는 내용이 길므로 height를 충분히 줌

st.markdown("---")
st.write("질문이 있으시면 언제든지 문의해주세요!")

