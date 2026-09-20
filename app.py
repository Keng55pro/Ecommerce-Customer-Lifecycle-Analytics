import streamlit as st
import pandas as pd
import numpy as np
import sqlite3
import joblib
import plotly.express as px
import os

st.set_page_config(page_title="E-Commerce Analytics", page_icon="🛒", layout="wide")

@st.cache_data
def load_data():
    db_path = 'data/ecommerce.db'
    if not os.path.exists(db_path):
        return None
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query("SELECT * FROM transactions", conn)
    conn.close()
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    return df

@st.cache_resource
def load_model():
    model_path = 'src/churn_xgboost_model.pkl'
    feature_path = 'src/model_features.pkl'
    if not os.path.exists(model_path) or not os.path.exists(feature_path):
        return None, None
    model = joblib.load(model_path)
    features = joblib.load(feature_path)
    return model, features

st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("เลือกหน้า:", ["Executive Dashboard", "Churn Prediction Tool"])

df = load_data()
model, model_features = load_model()

if df is None or model is None:
    st.warning("⚠️ ไม่พบข้อมูลหรือโมเดล กรุณารันไฟล์ notebooks/01_data_cleaning.ipynb ก่อนเปิด Web App")
    st.stop()

if page == "Executive Dashboard":
    st.title("🛒 Executive Business Dashboard")
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Revenue รวม", f"${df['TotalAmount'].sum():,.2f}")
    c2.metric("จำนวนคำสั่งซื้อ", f"{df['InvoiceNo'].nunique():,}")
    c3.metric("จำนวนลูกค้าทั้งหมด", f"{df['CustomerID'].nunique():,}")
    
    st.markdown("---")
    
    country_df = df.groupby('Country')['TotalAmount'].sum().reset_index().sort_values(by='TotalAmount', ascending=False).head(5)
    fig = px.bar(country_df, x='TotalAmount', y='Country', orientation='h', title="Top 5 ประเทศสร้างรายได้สูงสุด")
    st.plotly_chart(fig, use_container_width=True)

elif page == "Churn Prediction Tool":
    st.title("🤖 Customer Churn Prediction Tool")
    
    col1, col2 = st.columns(2)
    with col1:
        recency = st.number_input("Recency (จำนวนวันที่ไม่ได้สั่งซื้อ)", value=30)
        tenure = st.number_input("Tenure (อายุการเป็นลูกค้า - วัน)", value=180)
        frequency = st.number_input("Frequency (จำนวนออเดอร์)", value=5)
        total_qty = st.number_input("จำนวนสินค้าทั้งหมด", value=50)
    with col2:
        monetary_total = st.number_input("ยอดเงินรวม ($)", value=500.0)
        monetary_max = st.number_input("ยอดเงินสูงสุดต่อออเดอร์ ($)", value=150.0)
    
    if st.button("ทำนายโอกาส Churn", type="primary"):
        input_df = pd.DataFrame([{
            'Recency': recency, 'Tenure': tenure, 'Frequency': frequency,
            'Total_Quantity': total_qty, 'Avg_Quantity': total_qty/max(frequency,1),
            'Monetary_Total': monetary_total, 'Monetary_Avg': monetary_total/max(frequency,1),
            'Monetary_Max': monetary_max, 'Avg_Order_Value': monetary_total/max(frequency,1),
            'Purchase_Frequency_Days': tenure/max(frequency,1)
        }])
        
        prob = model.predict_proba(input_df)[0][1]
        st.metric("โอกาสในการ Churn", f"{prob:.1%}")
        if prob > 0.5:
            st.error("⚠️ ลูกค้ากลุ่มนี้เสี่ยงสูงที่จะ Churn")
        else:
            st.success("✅ ลูกค้ายังคง active ตามปกติ")