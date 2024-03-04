import pickle
import streamlit as st
import requests
import pandas as pd 

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=b6b456ec4fa733fba3c347df8daef79a&&language=en-US%27'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie ].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse = True,key=lambda x:x[1] )[1:6]


    recommended_movies = []
    recommended_movies_posters = []
    
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        
        recommended_movies.append(movies.iloc[i[0]].title)
        #fetch posters from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters


movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)


similarity = pickle.load(open('similarity.pkl','rb'))


st.title("Movies Recommender System")


selected_movie_name = st.selectbox(
    'How would you like to be seee the movie?',
    (movies['title'].values))


if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    
    
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.write(names[0])
        st.image(posters[0])

    with col2:
        st.write(names[1])
        st.image(posters[1])

    with col3:
        st.write(names[2])
        st.image(posters[2])
        
    with col4:
        st.write(names[3])
        st.image(posters[3])
        
    with col5:
        st.write(names[4])
        st.image(posters[4])
 
 
 
#     col1, col2, col3, col4, col5 = st.columns(5)

# # Display text in the first column
#     with col1:
#         for name in names:
#             st.write(name)

# # Display images in the second column
#     with col2:
#         for poster in posters:
#             st.image(poster)

# # Display images in the second column
#     with col3:
#         for poster in posters:
#             st.image(poster)
# # Display images in the second column
#     with col4:
#         for poster in posters:
#             st.image(poster)
# # Display images in the second column
#     with col5:
#         for poster in posters:
#             st.image(poster)