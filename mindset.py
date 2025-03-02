import streamlit as st

st.set_page_config(page_title="Growth mindset project", page_icon="✶")
st.title("Growth Mindset AI Project")
st.write("If you are mistakes in our present so you are independent in your future! ")
#quote section
st.header("Today's Growth Mindset Quotes")
st.write("Failure is a sucess , if you learn from it ")

st.header("Whats Your Challage Today?")
User_input=st.text_input("Describe a challage you are facing:")
#Condition
if User_input:
    st.success(f"You are facing: {User_input}. Keep pushing forward towards your goal!")
else:
        st.warning("Tell us about your challenge to get started!")
 #reflexing
st.header("Relect On Your Learning")
reflection=st.text_area("write your reflections here :")

if reflection:
    st.success(f"Great Insight! your reflection: {reflection}")
else:
    st.info("Reflecting on past experience help you grow! Share your difficulties")

#achievement
st.header("Celebrate Your Wins!") 
achievement=st.text_input("Share something you are recently accomplished:")

if achievement:
    st.success(f"Amazing! you achieved: {achievement}")
else:
    st.info("Big or small ,every achievement counts! Share one now")

#footer
st.write("- - -")
st.write("Keep believing in yourself . Growth is a jorney, not a destination!")
st.write("""Created by Muhammad Ehtisham""")