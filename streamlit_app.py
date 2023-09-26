import streamlit
import pandas

#Title of the Diner
streamlit.title('My Parents New Healthy Diner')

#Menu
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

#Smoothie
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#Data
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#Option to Pick Fruits
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

#Data Visualization
streamlit.dataframe(my_fruit_list)

