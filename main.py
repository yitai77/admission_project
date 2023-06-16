import streamlit as st
import random

from foodtype.food_type import get_food_type
from foodcafe.foodcafe_list import get_food_list

st.title("Lunch Choice Helper")

st.subheader("음식 테마")
ft = get_food_type()

st.subheader(f"{ft} 관련 음식점 추천")
get_food_list(ft)



