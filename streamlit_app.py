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

#response api
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")

#Display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")

#input for fruit_choice
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

#normalize api response to a database
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)
