import streamlit as st
import numpy as np
import pandas as pd
from streamlit_option_menu import option_menu
import time
import joblib
import db

custom_css = """
<style>
audio {
    display: none;
}
</style>
"""

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if 'user' not in st.session_state:
    st.session_state.user = ['Dummy']

def login():

    st.set_page_config(page_title="Spam Email Detection",page_icon="✉️")

    side = option_menu(
    menu_title=None,
    options=['Login','Sign Up'],
    icons=['house-door-fill','graph-up-arrow','plus-circle','info-circle'],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal"
)

    if side == 'Login':
        j,k,l = st.columns([2,2,1])
        k.header("Login")

        a,b,o = st.columns([1,2,1])
        user = b.text_input("Enter Username")

        st.markdown("<br>",unsafe_allow_html=True)

        c,d,p = st.columns([1,2,1])
        pas = d.text_input("Enter Password",type='password')

        st.markdown("<br>",unsafe_allow_html=True)    

        e,f,g = st.columns([1,2,1])

        login = f.button("Login",use_container_width=True)

        if login:
            if user != "" and pas != "":
                data = [user,pas]

                result = db.check_login(data)

                if result:
                    st.session_state.logged_in = True
                    st.session_state.user = result
                    st.rerun()

                else:
                    st.error("Wrong Credentials !!")
                    st.session_state.logged_in = False

    if side == 'Sign Up':
        m,n,o = st.columns(3)
        n.header("Sign Up")
        a,b = st.columns(2)
        f_name = a.text_input("First Name")
        l_name = b.text_input("Last Name")

        c,d = st.columns(2)
        user = c.text_input("Username")
        pas = d.text_input("Password")

        e,f = st.columns(2)
        mail = e.text_input("Mail")

        g,h = st.columns(2)
        submit = g.button("Submit",use_container_width=True)

        if submit:
            if f_name != "" and user != "" and pas != "" and mail != "":
                data = [f_name,l_name,user,mail,pas]

                db.insert_login(data)
                st.success("Hurayy !! Succesfully inserted your details")
            else:
                st.error("Couldn't insert your details, Mandotary Fields are blank !!")

def main():

    if not st.session_state.logged_in:
        login() 

    else:
        st.set_page_config(page_title="Spam Email Detection",page_icon="✉️")

        df = pd.read_csv('dataset.csv')
        user = str(st.session_state.user[0])

        st.header('Hello '+user)

        side = option_menu(
            menu_title=None,
            options=['Home','Predict','Contribute','History'],
            icons=['house-door-fill','graph-up-arrow','plus-circle','info-circle'],
            menu_icon="cast",
            default_index=0,
            orientation="horizontal"
        )

        if side == 'Home':
            st.title("Email Spam Detection")
            st.markdown("###  Training Dataset 📅")
            r = st.radio("Select One Option",['Show first 10 data','Show last 10 data'],index=0,horizontal=True)

            if r == 'Show first 10 data':
                st.table(data=df.head(10))
            if r == 'Show last 10 data':
                st.table(data=df.tail(10))

        if side == 'Predict':
            st.title("Predict Now 📈")

            predict_textt = st.text_area("Enter Your Mail :",placeholder="Hey Ashu ! You have won a prize.")
            a,b,c,d = st.columns(4)
            predict_button = a.button("Check",use_container_width=True)

            if predict_button == True:
                if predict_textt != "":
                    predict_text = [predict_textt]
                    bar = st.progress(2)
                    bar.progress(2,"Loading 2%")
                    model = joblib.load('model_saved.joblib')
                    message_encoder = joblib.load('message_encoder.joblib')
                    encoded_text = message_encoder.transform(predict_text)
                    encoded_text = encoded_text.toarray()
                    ans = model.predict(encoded_text)

                    for i in range(3,101):
                        time.sleep(0.03)
                        bar.progress(i,f"Analyzing {i} %")
                    
                    bar.empty()

                    if ans[0] == 0:
                        st.success("It is Not a Spam Mail")
                        st.markdown(custom_css,unsafe_allow_html=True)
                        audiofile = "Audio/success.mp3"
                        st.audio(audiofile,autoplay=True)
                        a = 'Not Spam'
                    else:
                        st.error("It seems to be a Spam Mail")
                        st.markdown(custom_css,unsafe_allow_html=True)
                        audiofile = "Audio/warning.mp3"
                        st.audio(audiofile,autoplay=True)
                        a = 'Spam'
                        
                    db.insert_history([user,predict_textt,a])
                else:
                    st.warning("Please Enter a valid Mail !!")

        if side == 'Contribute':
            st.title("Contribute to dataset 📅")
            mail,target = st.columns([0.7,0.3])

            mail_text = mail.text_area("Enter Mail Content")
            category_selected = target.selectbox(
            "Choose Category",
            ("Spam", "Not Spam"),
            index=0, )
            if category_selected == 'Spam':
                category_selected = 'spam'
            elif category_selected == 'Not Spam':
                category_selected = 'ham'

            a,b,c,d = st.columns([0.4,0.2,0.2,0.2])
            submit_button = a.button("Add To Dataset",use_container_width=True)

            if submit_button == True:
                to_add ={
                    'Category':category_selected,
                    'Message':' '.join(mail_text.splitlines())
                }
                to_add = pd.DataFrame([to_add])
                to_add.to_csv('dataset.csv',mode='a',header=False,index=False)
                st.table(to_add)
                st.success('**Success !! This data has been added to the Dataset**')

        if side =='History':
            st.title("History")

            lst = db.show_history([user])

            st.table(lst)

            
main()