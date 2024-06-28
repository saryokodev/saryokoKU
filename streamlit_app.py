import streamlit as st
import pandas as pd

house = pd.read_csv('house_clean.csv')

def main():
    st.header('Halaman Utama Saryoko')
    st.subheader('This is SubHeader')
    st.markdown('# Rendering Markdown')
    st.write('Some Pythagorean Equation : ')
    st.latex('c^2 = a^2+b^2')
    
    st.dataframe(house)
    st.write('metrics')
    st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

if __name__ == '__main__':
    main()
