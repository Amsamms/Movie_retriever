import streamlit as st
import requests
import pandas as pd

st.title("TMDb Movie Info Retriever")

# Predefined list of available attributes.
available_attributes = [
    "Title",
    "Original Title",
    "Release Date",
    "Runtime (minutes)",
    "Adult Content",
    "Rating (Vote Average)",
    "Vote Count",
    "Popularity",
    "Overview",
    "Tagline",
    "Genres",
    "Budget",
    "Revenue",
    "Status",
    "Spoken Languages",
    "Production Companies",
    "Production Countries",
    "Actors (Top 5)"
]

# Input for TMDb API key and movie name.
api_key = st.text_input("Enter your TMDb API Key:", type="password")
movie_name = st.text_input("Enter movie name:")

# Let the user select attributes before hitting the button.
# "ALL" option will override any other selection.
selected_options = st.multiselect(
    "Select attributes to display:",
    options=["ALL"] + available_attributes,
    default=["ALL"]
)

if "ALL" in selected_options:
    selected_attributes = available_attributes
else:
    selected_attributes = selected_options

if st.button("Get Movie Info"):
    if not api_key or not movie_name:
        st.error("Please enter both an API key and a movie name.")
    else:
        # Search for the movie to obtain its ID.
        search_url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={movie_name}"
        search_response = requests.get(search_url)
        if search_response.status_code != 200:
            st.error("Error fetching movie search data.")
        else:
            search_data = search_response.json()
            if search_data["results"]:
                movie = search_data["results"][0]
                movie_id = movie["id"]

                # Retrieve movie details.
                details_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"
                details_response = requests.get(details_url)
                if details_response.status_code != 200:
                    st.error("Error fetching movie details.")
                else:
                    details_data = details_response.json()

                    # Retrieve credits for cast info.
                    credits_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={api_key}"
                    credits_response = requests.get(credits_url)
                    credits_data = {}
                    if credits_response.status_code == 200:
                        credits_data = credits_response.json()

                    # Build the full attributes dictionary.
                    attributes_dict = {}
                    attributes_dict["Title"] = details_data.get("title", "N/A")
                    attributes_dict["Original Title"] = details_data.get("original_title", "N/A")
                    attributes_dict["Release Date"] = details_data.get("release_date", "N/A")
                    runtime = details_data.get("runtime")
                    attributes_dict["Runtime (minutes)"] = runtime if runtime is not None else "N/A"
                    attributes_dict["Adult Content"] = details_data.get("adult", "N/A")
                    attributes_dict["Rating (Vote Average)"] = details_data.get("vote_average", "N/A")
                    attributes_dict["Vote Count"] = details_data.get("vote_count", "N/A")
                    attributes_dict["Popularity"] = details_data.get("popularity", "N/A")
                    attributes_dict["Overview"] = details_data.get("overview", "N/A")
                    attributes_dict["Tagline"] = details_data.get("tagline", "N/A")
                    
                    # Genres as comma-separated names.
                    genres = details_data.get("genres")
                    if genres:
                        genres_str = ", ".join([genre.get("name", "") for genre in genres])
                    else:
                        genres_str = "N/A"
                    attributes_dict["Genres"] = genres_str
                    
                    attributes_dict["Budget"] = details_data.get("budget", "N/A")
                    attributes_dict["Revenue"] = details_data.get("revenue", "N/A")
                    attributes_dict["Status"] = details_data.get("status", "N/A")
                    
                    # Spoken languages.
                    languages = details_data.get("spoken_languages")
                    if languages:
                        languages_str = ", ".join([lang.get("name", "") for lang in languages])
                    else:
                        languages_str = "N/A"
                    attributes_dict["Spoken Languages"] = languages_str
                    
                    # Production companies.
                    companies = details_data.get("production_companies")
                    if companies:
                        companies_str = ", ".join([comp.get("name", "") for comp in companies])
                    else:
                        companies_str = "N/A"
                    attributes_dict["Production Companies"] = companies_str
                    
                    # Production countries.
                    countries = details_data.get("production_countries")
                    if countries:
                        countries_str = ", ".join([ctry.get("name", "") for ctry in countries])
                    else:
                        countries_str = "N/A"
                    attributes_dict["Production Countries"] = countries_str
                    
                    # Actors (top 5 from credits).
                    cast = credits_data.get("cast", [])
                    if cast:
                        top_actors = [actor.get("name", "") for actor in cast[:5]]
                        actors_str = ", ".join(top_actors)
                    else:
                        actors_str = "N/A"
                    attributes_dict["Actors (Top 5)"] = actors_str

                    # Filter the dictionary based on the user's selection.
                    filtered_data = {key: attributes_dict.get(key, "N/A") for key in selected_attributes}
                    # Convert to DataFrame and ensure all values are strings.
                    df = pd.DataFrame(filtered_data.items(), columns=["Attribute", "Value"])
                    df["Value"] = df["Value"].astype(str)
                    st.table(df)
            else:
                st.error("Movie not found. Please try another title.")
