import streamlit as st
import pandas as pd

st.set_page_config(page_title="📄 CSV Comparator", layout="wide")

st.title("🔍 Perbandingan Dua File CSV")
st.markdown("Unggah dua file CSV, lalu pilih kolom yang ingin dibandingkan.")

# Upload file CSV
col1, col2 = st.columns(2)
with col1:
    file1 = st.file_uploader("Unggah CSV Pertama", type="csv", key="file1")
with col2:
    file2 = st.file_uploader("Unggah CSV Kedua", type="csv", key="file2")

if file1 and file2:
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    st.subheader("🧾 Pratinjau Data")
    st.write("CSV 1:")
    st.dataframe(df1.head())
    st.write("CSV 2:")
    st.dataframe(df2.head())

    # Pilih kolom untuk dibandingkan
    common_cols = list(set(df1.columns) & set(df2.columns))
    if not common_cols:
        st.error("Tidak ada kolom yang sama di kedua file.")
    else:
        selected_col = st.selectbox("Pilih kolom yang ingin dibandingkan", common_cols)

        # Bandingkan nilai unik
        st.subheader(f"📊 Hasil Perbandingan Kolom: {selected_col}")
        set1 = set(df1[selected_col].dropna())
        set2 = set(df2[selected_col].dropna())

        only_in_df1 = set1 - set2
        only_in_df2 = set2 - set1
        intersection = set1 & set2

        st.markdown(f"✅ **Sama di kedua file:** {len(intersection)} nilai")
        st.markdown(f"❌ **Hanya di CSV 1:** {len(only_in_df1)} nilai")
        st.markdown(f"❌ **Hanya di CSV 2:** {len(only_in_df2)} nilai")

        with st.expander("📁 Detail nilai hanya ada di CSV 1"):
            st.write(only_in_df1)
        with st.expander("📁 Detail nilai hanya ada di CSV 2"):
            st.write(only_in_df2)

else:
    st.info("Silakan unggah dua file CSV terlebih dahulu.")
