import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from utils import DuckDBConnection # Assuming utils.py is in the same directory or accessible via PYTHONPATH

con = DuckDBConnection(connection_name='sample_data_con',md_db_name="sample_data")

df_preview = con._instance.sql("SELECT * FROM who.ambient_air_quality LIMIT 10").df()
st.title("Utah Ambient Air Quality")
air_quality_slc = con._instance.sql(
""" 
 SELECT * FROM who.ambient_air_quality
 WHERE country_name = 'United States of America' AND city LIKE '%UT%'
"""
).df()

st.dataframe(air_quality_slc)


cities = air_quality_slc["city"].unique()

for city in cities:
    subset = air_quality_slc[air_quality_slc["city"] == city]
    fig_pm10 = plt.figure(figsize=(10,6))
    sns.lineplot(x='year', y="pm10_concentration", data=subset)
    plt.title(f"Yearly PM 10 Concentration: {city}")
    plt.xlabel("Year")
    plt.ylabel("PM10 Concentration")
    st.pyplot(fig_pm10)

    fig_n02 = plt.figure(figsize=(10,6))
    sns.lineplot(x='year', y="no2_concentration", data=subset)
    plt.title(f"Yearly NO2 Concentration: {city}")
    plt.xlabel("Year")
    plt.ylabel("N02 Concentration")
    st.pyplot(fig_n02)
    
