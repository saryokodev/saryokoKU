import streamlit as st
import pandas as pd
from st_aggrid import AgGrid

house = pd.read_csv('house_clean.csv')

def main():
    st.header('Halaman Streamlit Saryoko')
    st.subheader('This is SubHeader')
    st.markdown('# Rendering Markdown')
    st.write('Some Pythagorean Equation : ')
    st.latex('c^2 = a^2+b^2')
    
    # st.dataframe(house)
    st.write('metrics')
    st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
    st.write('Menampilkan DataFrame dengan St Agrid')
    # AgGrid(house)

    st.table([x for x in range(1,5)])

    col1, col2, col3 = st.columns(3)
    with col1:
        jml_row = len(df)
        st.metric(label="Jumlah kolom", value=f"{jml_row} rows")
    with col2:    
        jml_col = len(df.columns)
        st.metric(label="Jumlah row", value=f"{jml_col} rows")
    with col3:    
        st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

    col1, col2 = st.columns(2)
    with col1:
        st.write('bedrooms vs price')
        fig,ax = plt.subplots()
        plt.scatter(df['bedrooms'],df['price'])
        st.pyplot(fig)
    with col2:    
        plotly_fig = px.scatter(df['bedrooms'],df['price'])
        st.plotly_chart(plotly_fig)

    click_me_btn = st.button('Click Me')
    st.write(click_me_btn) #Return True kalo di Click 
    check_btn = st.checkbox('Klik Jika Setuju')
    if check_btn :
        st.write('Anda Setuju')    
    
    radio_button= st.radio('Choose below',[x for x in range(1,3)])
    st.write('Anda Memilih',radio_button)
    
    #slider 
    age_slider = st.slider('Berapa Usia Anda',0,100)
    st.write('Usia Anda',age_slider)
    
    #Input (Typing)
    num_input = st.number_input('Input Berapapun')
    st.write('Kuadrat dari {} adalah {}'.format(num_input,num_input**2))

    #sidebar 
    sidebar_checkbox = st.sidebar.checkbox('Checkbox di Sidebar')
    sidebar_radio_button = st.sidebar.radio('Pilih Menu',options=['A','B','C'])

    #sidebar 
    with st.form("Data Diri"):
       st.write("Inside the form")
       slider_val = st.slider('Berapa Usia Anda',0,100)
       st.write('Anda Memilih',slider_val)
        
       checkbox_val = st.checkbox('Klik Jika Setuju')
       if check_btn :
           st.write('Anda Setuju')    

       # Every form must have a submit button.
       submitted = st.form_submit_button("Submit")
       if submitted:
           st.write("slider", slider_val, "checkbox", checkbox_val)

    st.write("Outside the form")
    
    #columns :
    col1, col2, col3 = st.columns(3)

    with col1:
       st.header("A cat")
       st.image("https://static.streamlit.io/examples/cat.jpg")

    with col2:
       st.header("A dog")
       st.image("https://static.streamlit.io/examples/dog.jpg")

    with col3:
       st.header("An owl")
       st.image("https://static.streamlit.io/examples/owl.jpg")
    #expander 
    #dengan with atau dengan assignment 
    expander = st.expander("Klik Untuk Detail ")
    expander.write('Anda Telah Membuka Detail')

def profile():
    st.title("Data Overview")
    st.write("Ini adalah halaman Profile.")
    st.write("Di sini Anda dapat menambahkan konten untuk halaman Profile Anda.")
    # Tambahkan konten halaman Profile di sini
    
if _name_ == '_main_' : 
  main()
