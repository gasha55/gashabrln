import streamlit as st

st.title("selamat datang di website gashamonyong")
st.write(
    "ngodingseru bersama gashamonyong"
)

st.image("IMG-20250527-WA0002.jpg")


st.title("Aplikasi Sederhana")
st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis sebuah Angka:", value=0 ,step=1)

if (angka % 2) == 0:
    st.write(f"{angka} adalah Bilangan Genap")
else:
    st.write("{angka} adalah Bilangan Ganjil")
