import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Student Performance Dashboard", layout="wide")
st.title("📘 Student Performance Dashboard")

# Upload CSV
uploaded_file = st.file_uploader("📤 Upload Student Marks CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    subjects = df.columns[1:]  # all columns except 'Name'
    
    # Calculate Total and Average
    df["Total"] = df[subjects].sum(axis=1)
    df["Average"] = df[subjects].mean(axis=1)
    
    # Tabs
    tab1, tab2, tab3, tab4 = st.tabs(["📈 Subject Averages", "🏆 Top Performers", "✅ Pass/Fail Analysis", "📊 Correlation Heatmap"])

    with tab1:
        st.subheader("📊 Average Score per Subject")
        subject_avg = df[subjects].mean().sort_values()
        st.bar_chart(subject_avg)

    with tab2:
        st.subheader("🏅 Top 5 Performers")
        top_df = df.sort_values("Average", ascending=False).head(5).reset_index(drop=True)
        top_df["🏆"] = ["🥇", "🥈", "🥉", "🎖️", "🎖️"]
        st.dataframe(top_df[["🏆", "Name", "Total", "Average"]])

    with tab3:
        st.subheader("✅ Pass/Fail Summary")
        pass_mark = st.slider("Set passing marks per subject:", 0, 100, 35)
        
        pass_matrix = df[subjects] >= pass_mark
        df["Passed_All"] = pass_matrix.all(axis=1)
        pass_count = df["Passed_All"].sum()
        fail_count = len(df) - pass_count

        st.write(f"✔️ Passed: {pass_count} students")
        st.write(f"❌ Failed: {fail_count} students")

        fig, ax = plt.subplots()
        ax.pie([pass_count, fail_count], labels=["Pass", "Fail"], autopct="%1.1f%%", colors=["#4CAF50", "#F44336"])
        st.pyplot(fig)

    with tab4:
        st.subheader("📉 Subject Correlation Heatmap")
        corr = df[subjects].corr()
        fig, ax = plt.subplots()
        sns.heatmap(corr, annot=True, cmap="YlGnBu", ax=ax)
        st.pyplot(fig)

    # Download button
    csv = df.to_csv(index=False).encode()
    st.download_button("📥 Download Processed CSV", csv, "processed_student_data.csv", "text/csv")
else:
    st.info("Upload a CSV file with columns like: Name, Math, Science, English, ...")

