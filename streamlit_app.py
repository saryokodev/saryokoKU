import streamlit as st

def main():
    st.header('Halaman Utama Saryoko')
    st.subheader('This is SubHeader')
    st.markdown('# Rendering Markdown')
    st.write('Some Pythagorean Equation : ')
    st.latex('c^2 = a^2+b^2')
if __name__ == '__main__':
    main()
