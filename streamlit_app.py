import streamlit
import pandas
import requests

#Title of the Diner
streamlit.title('MY PARENTS NEW HEALTHY DINER!')

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
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_to_show = my_fruit_list.loc[fruits_selected]

#Data Visualization
streamlit.dataframe(fruits_to_show)

#Display fruityvice api response
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
