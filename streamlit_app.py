import requests
import streamlit as st
import pandas as pd
from nltk import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import main_functions
import plotly.express as px


st.set_page_config(
    page_title="Project 1",
    page_icon="📰",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://docs.streamlit.io/library/api-reference',
        'Report a bug': "https://docs.streamlit.io/library/api-reference",
        'About': "# This is Project 1 for COP 4813 - Prof. Gregory Reis"
    })

# NYT Logo & Header
img_url = "https://daks2k3a4ib2z.cloudfront.net/5579d415182a00b90c5cdc01/5579f6ee182a00b90c5ce31a_the_new_york_times.png"
st.image(img_url, use_column_width=True)
st.subheader("Wordcloud & Histogram from today's headlines")

# pulls api key
nyt_api = main_functions.read_from_file("JSON_Files/api_keys.json")
nyt_key = nyt_api["nyt_api"]

st.sidebar.title("Project 1 - News App")
st.sidebar.subheader("The Stories API - WordCloud")

# Primary sidebar menu
option = st.sidebar.selectbox("Select an main category", ['Top Stories', 'Most Popular'])

if option == "Top Stories":
    # url_arts = "https://api.nytimes.com/svc/topstories/v2/arts.json?api-key=" + nyt_key
    # response = requests.get(url_arts).json()
    # main_functions.save_to_file(response, "JSON_Files/arts_articles.json")
    arts_articles = main_functions.read_from_file("JSON_Files/arts_articles.json")

    # url_automobiles = "https://api.nytimes.com/svc/topstories/v2/automobiles.json?api-key=" + nyt_key
    # response = requests.get(url_automobiles).json()
    # main_functions.save_to_file(response, "JSON_Files/automobiles_articles.json")
    automobiles_articles = main_functions.read_from_file("JSON_Files/automobiles_articles.json")

    # url_books = "https://api.nytimes.com/svc/topstories/v2/books.json?api-key=" + nyt_key
    # response = requests.get(url_books).json()
    # main_functions.save_to_file(response, "JSON_Files/books_articles.json")
    books_articles = main_functions.read_from_file("JSON_Files/books_articles.json")

    # url_business = "https://api.nytimes.com/svc/topstories/v2/business.json?api-key=" + nyt_key
    # response = requests.get(url_business).json()
    # main_functions.save_to_file(response, "JSON_Files/business_articles.json")
    business_articles = main_functions.read_from_file("JSON_Files/business_articles.json")

    # url_fashion = "https://api.nytimes.com/svc/topstories/v2/fashion.json?api-key=" + nyt_key
    # response = requests.get(url_fashion).json()
    # main_functions.save_to_file(response, "JSON_Files/fashion_articles.json")
    fashion_articles = main_functions.read_from_file("JSON_Files/fashion_articles.json")

    # url_food = "https://api.nytimes.com/svc/topstories/v2/food.json?api-key=" + nyt_key
    # response = requests.get(url_food).json()
    # main_functions.save_to_file(response, "JSON_Files/food_articles.json")
    food_articles = main_functions.read_from_file("JSON_Files/food_articles.json")

    # url_health = "https://api.nytimes.com/svc/topstories/v2/health.json?api-key=" + nyt_key
    # response = requests.get(url_health).json()
    # main_functions.save_to_file(response, "JSON_Files/health_articles.json")
    health_articles = main_functions.read_from_file("JSON_Files/health_articles.json")

    # url_home = "https://api.nytimes.com/svc/topstories/v2/home.json?api-key=" + nyt_key
    # response = requests.get(url_home).json()
    # main_functions.save_to_file(response, "JSON_Files/home_articles.json")
    home_articles = main_functions.read_from_file("JSON_Files/home_articles.json")

    # url_insider = "https://api.nytimes.com/svc/topstories/v2/insider.json?api-key=" + nyt_key
    # response = requests.get(url_insider).json()
    # main_functions.save_to_file(response, "JSON_Files/insider_articles.json")
    insider_articles = main_functions.read_from_file("JSON_Files/insider_articles.json")

    # url_magazine = "https://api.nytimes.com/svc/topstories/v2/magazine.json?api-key=" + nyt_key
    # response = requests.get(url_magazine).json()
    # main_functions.save_to_file(response, "JSON_Files/magazine_articles.json")
    magazine_articles = main_functions.read_from_file("JSON_Files/magazine_articles.json")

    # url_movies = "https://api.nytimes.com/svc/topstories/v2/movies.json?api-key=" + nyt_key
    # response = requests.get(url_movies).json()
    # main_functions.save_to_file(response, "JSON_Files/movies_articles.json")
    movies_articles = main_functions.read_from_file("JSON_Files/movies_articles.json")

    # url_nyregion = "https://api.nytimes.com/svc/topstories/v2/nyregion.json?api-key=" + nyt_key
    # response = requests.get(url_nyregion).json()
    # main_functions.save_to_file(response, "JSON_Files/nyregion_articles.json")
    nyregion_articles = main_functions.read_from_file("JSON_Files/nyregion_articles.json")

    # url_opinion = "https://api.nytimes.com/svc/topstories/v2/opinion.json?api-key=" + nyt_key
    # response = requests.get(url_opinion).json()
    # main_functions.save_to_file(response, "JSON_Files/opinion_articles.json")
    opinion_articles = main_functions.read_from_file("JSON_Files/opinion_articles.json")

    # url_politics = "https://api.nytimes.com/svc/topstories/v2/politics.json?api-key=" + nyt_key
    # response = requests.get(url_politics).json()
    # main_functions.save_to_file(response, "JSON_Files/politics_articles.json")
    politics_articles = main_functions.read_from_file("JSON_Files/politics_articles.json")

    # url_realestate = "https://api.nytimes.com/svc/topstories/v2/realestate.json?api-key=" + nyt_key
    # response = requests.get(url_realestate).json()
    # main_functions.save_to_file(response, "JSON_Files/realestate_articles.json")
    realestate_articles = main_functions.read_from_file("JSON_Files/realestate_articles.json")

    # # url_science = "https://api.nytimes.com/svc/topstories/v2/science.json?api-key=" + nyt_key
    # # response = requests.get(url_science).json()
    # # main_functions.save_to_file(response, "JSON_Files/science_articles.json")
    science_articles = main_functions.read_from_file("JSON_Files/science_articles.json")
    #
    # url_sports = "https://api.nytimes.com/svc/topstories/v2/sports.json?api-key=" + nyt_key
    # response = requests.get(url_sports).json()
    # main_functions.save_to_file(response, "JSON_Files/sports_articles.json")
    sports_articles = main_functions.read_from_file("JSON_Files/sports_articles.json")

    # url_sundayreview = "https://api.nytimes.com/svc/topstories/v2/sundayreview.json?api-key=" + nyt_key
    # response = requests.get(url_sundayreview).json()
    # main_functions.save_to_file(response, "JSON_Files/sundayreview_articles.json")
    sundayreview_articles = main_functions.read_from_file("JSON_Files/sundayreview_articles.json")

    # url_technology = "https://api.nytimes.com/svc/topstories/v2/technology.json?api-key=" + nyt_key
    # response = requests.get(url_technology).json()
    # main_functions.save_to_file(response, "JSON_Files/technology_articles.json")
    technology_articles = main_functions.read_from_file("JSON_Files/technology_articles.json")

    # url_theater= "https://api.nytimes.com/svc/topstories/v2/theater.json?api-key=" + nyt_key
    # response = requests.get(url_theater).json()
    # main_functions.save_to_file(response, "JSON_Files/theater_articles.json")
    theater_articles = main_functions.read_from_file("JSON_Files/theater_articles.json")

    # url_tmagazine = "https://api.nytimes.com/svc/topstories/v2/t-magazine.json?api-key=" + nyt_key
    # response = requests.get(url_tmagazine).json()
    # main_functions.save_to_file(response, "JSON_Files/tmagazine_articles.json")
    tmagazine_articles = main_functions.read_from_file("JSON_Files/tmagazine_articles.json")

    # url_travel = "https://api.nytimes.com/svc/topstories/v2/travel.json?api-key=" + nyt_key
    # response = requests.get(url_travel).json()
    # main_functions.save_to_file(response, "JSON_Files/travel_articles.json")
    travel_articles = main_functions.read_from_file("JSON_Files/travel_articles.json")

    # url_upshot = "https://api.nytimes.com/svc/topstories/v2/upshot.json?api-key=" + nyt_key
    # response = requests.get(url_upshot).json()
    # main_functions.save_to_file(response, "JSON_Files/upshot_articles.json")
    upshot_articles = main_functions.read_from_file("JSON_Files/upshot_articles.json")

    # url_us = "https://api.nytimes.com/svc/topstories/v2/us.json?api-key=" + nyt_key
    # response = requests.get(url_us).json()
    # main_functions.save_to_file(response, "JSON_Files/us_articles.json")
    us_articles = main_functions.read_from_file("JSON_Files/us_articles.json")

    # url_world = "https://api.nytimes.com/svc/topstories/v2/world.json?api-key=" + nyt_key
    # response = requests.get(url_world).json()
    # main_functions.save_to_file(response, "JSON_Files/world_articles.json")
    world_articles = main_functions.read_from_file("JSON_Files/world_articles.json")

    # Sidebars, Titles & headers
    st.sidebar.title("WordCloud Options")
    select_api = st.sidebar.selectbox("Select an API", ["Art", "Automobiles", "Books", "Business", "Fashion",
                                                        "Food", "Health", "Home", "Insider", "Magazine", "Movies",
                                                        "NYRegion", "Opinion", "Politics", "RealEstate", "Science",
                                                        "Sports", "SundayReview", "Technology", "Theater", "TMagazine",
                                                        "Travel", "Upshot", "US", "World"])
    max_words = st.sidebar.slider("Max words", min_value=1, max_value=200, value=100)
    # background_color = st.sidebar.selectbox("Background color", ["black", "white", "grey"])
    background_color = st.sidebar.color_picker("Background color", "#000000")
    color_map = st.sidebar.selectbox("Color map", ["plasma", "viridis", "inferno", "magma", "cividis"])
    # Seperator and name
    st.sidebar.image("https://clipground.com/images/thin-white-line-png-3.png")
    st.sidebar.write("Wallace Eltus - COP4813 RVC 1231 - Prof. Reis")

    # if/elifs to read from JSON files on selection
    # TODO Cant figure out to iterate through these without errors
    if select_api == "Art":
        articles = main_functions.read_from_file("JSON_Files/arts_articles.json")
    elif select_api == "Automobiles":
        articles = main_functions.read_from_file("JSON_Files/automobiles_articles.json")
    elif select_api == "Books":
        articles = main_functions.read_from_file("JSON_Files/books_articles.json")
    elif select_api == "Business":
        articles = main_functions.read_from_file("JSON_Files/business_articles.json")
    elif select_api == "Fashion":
        articles = main_functions.read_from_file("JSON_Files/fashion_articles.json")
    elif select_api == "Food":
        articles = main_functions.read_from_file("JSON_Files/food_articles.json")
    elif select_api == "Health":
        articles = main_functions.read_from_file("JSON_Files/health_articles.json")
    elif select_api == "Home":
        articles = main_functions.read_from_file("JSON_Files/home_articles.json")
    elif select_api == "Insider":
        articles = main_functions.read_from_file("JSON_Files/insider_articles.json")
    elif select_api == "Magazine":
        articles = main_functions.read_from_file("JSON_Files/magazine_articles.json")
    elif select_api == "Movies":
        articles = main_functions.read_from_file("JSON_Files/movies_articles.json")
    elif select_api == "NYRegion":
        articles = main_functions.read_from_file("JSON_Files/NYRegion_articles.json")
    elif select_api == "Opinion":
        articles = main_functions.read_from_file("JSON_Files/opinion_articles.json")
    elif select_api == "Politics":
        articles = main_functions.read_from_file("JSON_Files/politics_articles.json")
    elif select_api == "RealEstate":
        articles = main_functions.read_from_file("JSON_Files/RealEstate_articles.json")
    elif select_api == "Science":
        articles = main_functions.read_from_file("JSON_Files/science_articles.json")
    elif select_api == "Sports":
        articles = main_functions.read_from_file("JSON_Files/sports_articles.json")
    elif select_api == "SundayReview":
        articles = main_functions.read_from_file("JSON_Files/SundayReview_articles.json")
    elif select_api == "Technology":
        articles = main_functions.read_from_file("JSON_Files/technology_articles.json")
    elif select_api == "Theater":
        articles = main_functions.read_from_file("JSON_Files/theater_articles.json")
    elif select_api == "TMagazine":
        articles = main_functions.read_from_file("JSON_Files/tmagazine_articles.json")
    elif select_api == "Travel":
        articles = main_functions.read_from_file("JSON_Files/travel_articles.json")
    elif select_api == "Upshot":
        articles = main_functions.read_from_file("JSON_Files/upshot_articles.json")
    elif select_api == "US":
        articles = main_functions.read_from_file("JSON_Files/US_articles.json")
    elif select_api == "World":
        articles = main_functions.read_from_file("JSON_Files/world_articles.json")

    abstracts = ""
    for i in articles["results"]:
        abstracts = abstracts + i["abstract"]

    # FILTERING RESULTS
    # 1: creates a list from the word dump
    words = word_tokenize(abstracts)

    # 2: removes punctuation and misc symbols
    no_punkt = []
    for w in words:
        if w.isalpha():
            no_punkt.append(w)

    # 3: filters only english words
    stopwordsEnglish = stopwords.words("english")

    # 4: removes words that don't contribute to the collection
    filtered_list = []
    for w in no_punkt:
        if w not in stopwordsEnglish:
            filtered_list.append(w)

    # FREQUENCY DISTRIBUTION
    # determines number of words and the occurrence
    freq_distribution = FreqDist(filtered_list)
    # creates a table from the frequency distribution
    most_common_words = pd.DataFrame(freq_distribution.most_common(20))
    # takes table and adds titles to each column
    most_common = pd.DataFrame(
        {
            "words" : most_common_words[0],
            "count" : most_common_words[1]
        }
    )

    # WordCloud generation
    wordcloud = WordCloud(background_color=background_color,
                          max_words=max_words,
                          colormap=color_map).generate(abstracts)

    fig, ax = plt.subplots()
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    st.pyplot(fig)

    if st.button("Generate Histogram"):
        fig_arts = px.histogram(most_common, x="words", y="count", title="Freq Dist of most common words", color="count")
        st.plotly_chart(fig_arts)

elif option == "Most Popular":
    # Sidebars, Titles & headers
    st.sidebar.title("Most Popular - WordCloud Options")
    max_words = st.sidebar.slider("Max words", min_value=1, max_value=200, value=100)
    # background_color = st.sidebar.selectbox("Background color", ["black", "white", "grey"])
    background_color = st.sidebar.color_picker("Background color", "#000000")
    color_map = st.sidebar.selectbox("Color map", ["plasma", "viridis", "inferno", "magma", "cividis"])
    # Secondary sidebar menu for Most Popular articles
    st.sidebar.subheader("Most Popular Articles")
    most_popular_type = st.sidebar.selectbox("Select preferred set of articles", ["shared", "emailed", "viewed"])
    most_popular_period = st.sidebar.selectbox("Select period", ["1", "7", "30"])
    # Seperator and name
    st.sidebar.image("https://clipground.com/images/thin-white-line-png-3.png")
    st.sidebar.write("Wallace Eltus - COP4813 RVC 1231 - Prof. Reis")


    # API call to get the Most Popular articles
    most_popular_url = f"https://api.nytimes.com/svc/mostpopular/v2/{most_popular_type}/{most_popular_period}.json?api-key={nyt_key}"
    most_popular_response = requests.get(most_popular_url).json()
    main_functions.save_to_file(most_popular_response, "JSON_Files/most_popular.json")

    most_popular_articles = main_functions.read_from_file("JSON_Files/most_popular.json")

    # Initializes abstracts
    abstracts = ""
    for i in most_popular_articles["results"]:
        abstracts = abstracts + i["abstract"]

    # FILTERING RESULTS
    # 1: creates a list from the word dump
    words = word_tokenize(abstracts)

    # 2: removes punctuation and misc symbols
    no_punkt = []
    for w in words:
        if w.isalpha():
            no_punkt.append(w)

    # 3: filters only english words
    stopwordsEnglish = stopwords.words("english")

    # 4: removes words that don't contribute to the collection
    filtered_list = []
    for w in no_punkt:
        if w not in stopwordsEnglish:
            filtered_list.append(w)

    # FREQUENCY DISTRIBUTION
    # determines number of words and the occurrence
    freq_distribution = FreqDist(filtered_list)
    # creates a table from the frequency distribution
    most_common_words = pd.DataFrame(freq_distribution.most_common(20))
    # takes table and adds titles to each column
    most_common = pd.DataFrame(
        {
            "words": most_common_words[0],
            "count": most_common_words[1]
        }
    )

    # WordCloud generation
    wordcloud = WordCloud(background_color=background_color,
                          max_words=max_words,
                          colormap=color_map).generate(abstracts)

    fig, ax = plt.subplots()
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    st.pyplot(fig)

    if st.button("Generate Histogram"):
        fig_popular = px.histogram(most_common, x="words", y="count", title="Freq Dist of most common words", color="count")
        st.plotly_chart(fig_popular)

