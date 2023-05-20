import streamlit as st
import plotly.express as px


def calculate_sum(temp, unit):
    if unit == "Celsius" or unit == 'C' or unit == "c":
        return temp
    elif unit == "Fahrenheit" or unit == 'F' or unit == 'f':
        return round((temp -32) * 5/9 , 3)

def main():
    st.title("Temperature Converter")
    temp = st.number_input("Enter the temperature: ")
    unit = st.selectbox("Select the weather unit: " , ('Celsius','Fahrenheit'))

    converted_temp = calculate_sum(temp, unit)
    st.write("Converted temperature", converted_temp)



if __name__ =="__main__":
    main()








