import  pandas as pd
import streamlit as st
import plotly.express as px

data = pd.read_csv('test.csv')
def filterdata(weather, temp):

    filtered_df_weather = data[(data['weather'] == weather) & (data['temp_max'] >= temp)]
    return filtered_df_weather




def main():
    st.title("Test weather project")
    weather = st.selectbox("Select the weather ",("rain","snow","sun","drizzle"))
    temp_max = st.number_input("Enter the tempeture: ")
    test = filterdata(weather, temp_max)
    st.write(test)

    fig = px.density_heatmap(test,x= 'date',y='temp_max', z = 'weather')
    st.plotly_chart(fig)




if __name__ == '__main__':
    main()