#imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import re
from nltk.corpus import stopwords #nltk is natural language toolkit #stopwords are words that dont add much importance to our text
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
import difflib
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import pyperclip
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

from tkinter import Canvas

print("hi")


def Favourite_movie(movie_name):
    if len(movie_name) != 0:
        movds=pd.read_csv('movies.csv')
        selected_features=['genres','keywords','tagline','cast','director']
        # print(selected_features)
        for feature in selected_features:
            movds[feature]=movds[feature].fillna('')
        newmovds=movds['genres']+''+movds['keywords']+''+movds['tagline']+''+movds['cast']+''+movds['director']
        # print(newmovds)


        vectorizer= TfidfVectorizer() #Term Frequency Inverse Document Frequency, counts number of times a word is repeating in a document. the repetion of the word signifies how important the word actuall is
        feature_vectors= vectorizer.fit_transform(newmovds)

        similarity= cosine_similarity(feature_vectors)


        list_of_all_titles=movds['title'].to_list()
        #print(list_of_all_titles)
        #finding close match for movie name given by the user
        find_close_match= difflib.get_close_matches(movie_name,list_of_all_titles)
        # print(find_close_match)
        close_match=find_close_match[0]
        #print(close_match)
        #finding index of movie with title
        index_movie=movds[movds.title==close_match]['index'].values[0]
        #print(index_movie)
        #getting a list of simillar movies
        similarity_score=list(enumerate(similarity[index_movie])) #enumerate is like running a loop in a list.
        #sorting the movies based on their similarity score
        sorted_similar_movies=sorted(similarity_score,key= lambda x:x[1], reverse=True)
        top10_recomended= sorted_similar_movies[:10]
        #finding title of movie with index
        # print(f'The top 10 related movies to {movie_name} are: ')
        k=1
        data = []
        # print(top10_recomended)
        for i in top10_recomended:
            index=i[0]

            title_of_movie=movds[movds.index==index]['title'].values
            for i in title_of_movie:
                print(k,i)
                data.append(i)
                text.insert(INSERT, i)

                k+=1
        print(data)
       
        

        #delete's the input
        movie.delete(0, END)
    else:
        messagebox.showerror("Oops", message="Please enter a movie name.")



window = Tk()
window.title("Movie Recommendation System")
window.config(padx=50, pady=50)

canvas = Canvas(width=128, height=140)
image = PhotoImage(file="logo-1.png")
canvas.create_image(64,64,image=image)


global text
#text
text= Text(window)


# my_img=ImageTk.PhotoImage(image)
canvas.grid(column=2, row=0)
# label=Label(window, image=my_img)


my_label_1 = Label(text="Favourite Movie:")
my_label_1.grid(column=0, row=1)
global movie
movie  = Entry(width=30)
movie.focus()
movie.grid(column=2, row=1)


search_button = Button(text="Search", width=10, command=lambda: Favourite_movie(movie_name=movie.get()))
window.bind('<Return>',lambda event: Favourite_movie(movie_name=movie.get()))

search_button.grid(column=4, row=1)


# Output = Text(root, height = 5,width = 25, bg = "light cyan")

window.mainloop()


