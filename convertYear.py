import streamlit as st
2
st.title("แอปพลิเคชั่นแปลงปี พ.ศ. เป็น ค.ศ.")
3
4
bh_year=st.number_input("กรอกปี พ.ศ. ที่ต้องการแปลง", value=
5
ce_year=bh_year-543
6
st.header(f"ปี ค.ศ. คือ : {ce_year}")
