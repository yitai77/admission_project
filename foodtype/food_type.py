import streamlit as st
import random

def get_food_type():

    if st.button("점심 종류", use_container_width=True):
        choice = random.choice(['우동', '컵라면', '덮밥', '라멘'])
        st.write(f"{choice}")
        return choice
    return ""
