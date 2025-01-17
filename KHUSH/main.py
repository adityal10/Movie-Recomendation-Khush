#imports ML
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

#UI imports
import pyperclip
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import Canvas
import customtkinter

# def Clear():
#     try:
#         entry.delete(0, END)
#         textbox.delete(0, END)
#     except AttributeError:
#         pass



# def get_movie(movie_name):

#     return len(movie_name)



def Favourite_movie(movie_name):


    # ---------------- updates a new textbox with a new textbox --------------
    global textbox
    #destroy's the previous box
    textbox.destroy()
    #creates a new textbox
    textbox = customtkinter.CTkTextbox(master=window,
        width=470,
        height=440,
        border_width=2,
        text_font= 'Poppins 12')
    textbox.place(relx=0.73, rely=0.555, anchor=CENTER)
    # -----------------------------------------------------------------------------

    try:
        if len(movie_name) != 0:
            movds=pd.read_csv('KHUSH\movies.csv')
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

            top = "Top"
            num = "10"
            related = "related"
            movies = "movies"
            for_ = "for"
            name = movie_name
            are = "are"
            movie_name_len = int(len(name))
            font = 'Poppins 12 bold'

            #inserts text inside the textbox
            textbox.insert(END, f"{top} {num} {related} {movies} {for_} ' {name} ' {are}: \n\n")


            textbox.tag_add(top, '1.0','1.3')
            textbox.tag_config(top, font=font)

            textbox.tag_add(num, '1.4','1.6')
            textbox.tag_config(num, font=font)

            textbox.tag_add(related, '1.7','1.14')
            textbox.tag_config(related, font=font)

            textbox.tag_add(movies, '1.15','1.21')
            textbox.tag_config(movies, font=font)

            textbox.tag_add(for_, '1.22','1.25')
            textbox.tag_config(for_, font=font)

            textbox.tag_add(name, '1.26',f'1.{27+movie_name_len}')
            textbox.tag_config(name, font='Poppins 12 bold italic')

            textbox.tag_add(top, f'1.{27+movie_name_len}','1.50')
            textbox.tag_config(are, font=font)


            for i in top10_recomended:
                index=i[0]
                title_of_movie=movds[movds.index==index]['title'].values
                for i in title_of_movie:
                    # print(k,i)
                    data.append(i)
                    # text.insert(INSERT, i)
                    textbox.insert(END, f'{k}. {i}\n\n')
                    k+=1
            # print(data)
            
        else:
            messagebox.showerror("Oops", message="Please enter a movie name.")

            #destroy's the previous box
            textbox.destroy()
            #creates a new textbox
            textbox = customtkinter.CTkTextbox(master=window,
                width=470,
                height=440,
                border_width=2,
                text_font= 'Poppins 12')
            textbox.place(relx=0.73, rely=0.555, anchor=CENTER)


    except IndexError:
            messagebox.showerror("Oops", message="Please enter a valid movie name.")


            #destroy's the previous box
            textbox.destroy()
            #creates a new textbox
            textbox = customtkinter.CTkTextbox(master=window,
                width=470,
                height=440,
                border_width=2,
                text_font= 'Poppins 12')
            textbox.place(relx=0.73, rely=0.555, anchor=CENTER)
            
            
            







window = customtkinter.CTk()
window.geometry(f"{900}x{550}")
window.title("Movie Recomendation System")
window.minsize(900,550)
window.maxsize(900,550)


textbox = customtkinter.CTkTextbox(master=window,
                width=470,
                height=440,
                border_width=2,
                text_font= 'Poppins 12')
textbox.place(relx=0.73, rely=0.555, anchor=CENTER)



entry = customtkinter.CTkEntry(master=window,
                               placeholder_text="Enter you're favourite film",
                               width=460,
                               height=30,
                               border_width=2,
                               corner_radius=0)
entry.place(relx=0.73, rely=0.1, anchor=CENTER)


#buttons
img_search = PhotoImage(file="KHUSH\search1.png")
button_search = customtkinter.CTkButton(master=window,
                                 image = img_search,
                                 fg_color='white',
                                 hover_color="grey",
                                 width=34,
                                 height=30,
                                 border_width=0,
                                 corner_radius=0,
                                 text=None,
                                 command=lambda: Favourite_movie(movie_name=entry.get()))
button_search.place(relx=0.97, rely=0.1, anchor=CENTER)

# button_clear = customtkinter.CTkButton(master=window,
#                                  width=35,
#                                  height=7.5,
#                                  fg_color='red',
#                                  border_width=0,
#                                  corner_radius=4,
#                                  text="Clear",
#                                  command=Clear)
# button_clear.place(relx=0.95, rely=0.1, anchor=CENTER)

window.bind('<Return>',lambda event: Favourite_movie(movie_name=entry.get()))#enter key


#image
img = PhotoImage(file="KHUSH\pic.png")
image = customtkinter.CTkButton(master=window,
                                fg_color=None,
                                image = img, 
                                text=None, 
                                border_color=None,
                                hover=False, 
                                corner_radius=8
                                )
image.place(relx=0, rely=0)

window.mainloop()
