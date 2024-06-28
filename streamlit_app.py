import streamlit as st

def main():
    st.header('Halaman Utama Saryoko')
    st.subheader('This is SubHeader')
    st.markdown('# Rendering Markdown')
    st.write('Some Pythagorean Equation : ')
    st.latex('c^2 = a^2+b^2')
    
    house = 'house_clean.csv'
    st.dataframe(house)
    st.writer('metrics')
    st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
if __name__ == '__main__':
    main()
