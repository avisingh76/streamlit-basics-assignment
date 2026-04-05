import streamlit as st
import pandas as pd
 
 # Task 1: Building the App
st.title("Sales Dashboard")
st.subheader("Filter product by category to view sales data.")

df = pd.DataFrame({
    "Product":['Denim Jacket','Silk Scarf','Running Sneakers','Wool Sweater','Leather Handbag','Ankle Boots'],
    "Category":['Outerwear','Accessories','Footwear','Outerwear','Accessories','Footwear'],
    "Sales":[8200,3100,6750,5400,9300,7100]
})

# Task 2: Adding Sidebar
category = st.sidebar.selectbox("Select Category",df['Category'].unique())

df_filtered = df[df['Category'] == category]

st.dataframe(df_filtered)
st.line_chart(df_filtered.set_index('Product')['Sales'])
