import streamlit as st

st.title('Aplikasi perhitungan molaritas')

bobot = st.number_input('Masukan nilai bobot')
volume = st.number_input('Masukan nilai volume')
mr = st.number_input('Masukan nilai Mr')

tombol = st.button('Hitung nilai molaritas')

if tombol:
    nilai_molaritas = bobot/(mr*volume)
    st.success(f'Nilai molaritas adalah {nilai_molaritas}')