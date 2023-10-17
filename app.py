import pandas as pd
import streamlit as st
df=pd.read_csv(r"data/final_zomato.csv")

def recommend_restaurant(cuisine,location):
    filtered_df =df[(df['restaurant_address'] == location)]
    # Popular Cuisine in the area
    popular_cuisine = filtered_df['cuisine'].mode()[0]
    
    # Average price for 1 person
    average_price = filtered_df['price for one'].mean()
    
    # Most Popular Restaurant and Cuisine they are serving
    most_popular_restaurant = filtered_df.loc[filtered_df['ratings'].idxmax(), 'name']
    most_popular_cuisine = filtered_df.loc[filtered_df['ratings'].idxmax(), 'cuisine']
    
    # Most Popular restaurant serving the same cuisine
    similar_cuisine_df = df[(df['cuisine'] == cuisine)& (df['restaurant_address'] == location)]
    most_popular_similar_cuisine_restaurant = similar_cuisine_df.loc[similar_cuisine_df['ratings'].idxmax(), 'name']
    
    output = {
        "Popular cuisine in this area": popular_cuisine,
        "Average price for one in this area": average_price,
        "Most popular restaurant in this area": most_popular_restaurant,
        "Cuisine served by the most popular restaurant in this area": most_popular_cuisine,
        "Most popular restaurant serving the same cuisine as user provided": most_popular_similar_cuisine_restaurant
    }
    
    return output


cuisines_list=['Arabian', ' Biryani', ' North Indian', ' Chinese', ' Fast Food',
       ' Sichuan', 'Chinese', ' Mughlai', 'Bakery', ' Desserts', 'Burger',
       ' American', ' Bakery', ' Italian', ' Oriental', ' Continental',
       ' Beverages', 'North Indian', ' Rajasthani', ' Mithai', ' BBQ',
       ' Seafood', ' Arabian', 'Pizza', ' Pasta', ' Kebab',
       ' South Indian', 'Biryani', ' Andhra', 'Fast Food', ' Rolls',
       ' Burger', 'Mithai', ' Street Food', ' Wraps', ' Sandwich',
       'Ice Cream', ' Shake', 'Mughlai', 'South Indian', 'Kerala',
       ' Lebanese', ' Ice Cream', ' Maharashtrian', ' Hyderabadi',
       ' Pizza', 'Continental', ' Healthy Food', 'Momos', ' Tibetan',
       'Mexican', 'Healthy Food', ' Salad', 'Rolls', 'Andhra', ' Afghan',
       'Street Food', ' Tea', ' Juices', 'Beverages', 'Tea', ' Coffee',
       ' Asian', ' Thai', ' Malaysian', ' Lucknowi', 'Waffle', ' Pancake',
       ' Chettinad', ' Momos', ' Cafe', ' Japanese', ' Indonesian',
       'Desserts', 'Sandwich', 'Asian', 'Cafe', 'Wraps', 'Shawarma',
       'Lebanese', 'Shake', 'Juices', 'Afghan', ' Waffle', 'Mangalorean',
       ' Kerala', ' Bengali', ' Mexican', ' French', ' Panini',
       'Portuguese', 'Japanese', ' Korean', ' Sushi', 'Pasta',
       ' European', 'Middle Eastern', ' Vietnamese', ' Burmese',
       ' Shawarma', 'Italian', 'Naga', 'BBQ', ' Finger Food',
       'Maharashtrian', 'Bengali', ' Mishti', 'Tibetan', 'Awadhi',
       'Chettinad', ' Bubble Tea', ' Kashmiri', 'Kebab', ' Iranian',
       'Seafood', 'North Eastern', 'Odia']

address_list=['Vijay Nagar, Bangalore', 'Shanti Nagar, Bangalore',
       'Vasanth Nagar, Bangalore', 'St. Marks Road, Bangalore',
       'MG Road, Bangalore', 'Koramangala 7th Block, Bangalore',
       'UB City, Bangalore', 'Nagawara, Bangalore',
       'Brigade Road, Bangalore', 'Shivajinagar, Bangalore',
       'Commercial Street, Bangalore', 'Residency Road, Bangalore',
       'Frazer Town, Bangalore', 'Mantri Square, Malleshwaram, Bangalore',
       'Basavanagudi, Bangalore', 'Malleshwaram, Bangalore',
       'Indiranagar, Bangalore', 'Kammanahalli, Bangalore',
       'Koramangala 6th Block, Bangalore', 'Jayanagar, Bangalore',
       'Rajajinagar, Bangalore', 'Richmond Road, Bangalore',
       'Ulsoor, Bangalore', 'Church Street, Bangalore',
       'Garuda Mall, Magrath Road, Bangalore',
       'Cunningham Road, Bangalore', 'BTM, Bangalore',
       'Majestic, Bangalore', 'Wilson Garden, Bangalore',
       'Sigma Mall, Cunningham Road, Bangalore', 'Domlur, Bangalore',
       'Seshadripuram, Bangalore', 'JP Nagar, Bangalore',
       'Lavelle Road, Bangalore', 'Koramangala 8th Block, Bangalore',
       'Koramangala 5th Block, Bangalore', 'Sadashiv Nagar, Bangalore',
       'Jeevan Bhima Nagar, Bangalore', 'Old Madras Road, Bangalore',
       'Koramangala 4th Block, Bangalore', 'Banashankari, Bangalore',
       'HBR Layout, Bangalore', 'Basaveshwara Nagar, Bangalore',
       'Old Airport Road, Bangalore', 'Thippasandra, Bangalore',
       'RT Nagar, Bangalore', 'Kumaraswamy Layout, Bangalore',
       'Orion East, Banaswadi, Bangalore', 'Hosur Road, Bangalore',
       'Bannerghatta Road, Bangalore', 'Langford Town, Bangalore',
       'Yeshwantpur, Bangalore',
       'Building 105, Koramangala 5th Block, Bangalore',
       'Ejipura, Bangalore', 'Banaswadi, Bangalore',
       'City Market, Bangalore',
       'Jatti Building, Koramangala 5th Block, Bangalore',
       '153 Biere Street, Bangalore', '1 Sobha, Bangalore',
       'New BEL Road, Bangalore',
       'Royal Orchid Hotel,  Old Airport Road, Bangalore',
       'Sanjay Nagar, Bangalore', 'Kalyan Nagar, Bangalore',
       'Koramangala 2nd Block, Bangalore', 'Infantry Road, Bangalore',
       'Koramangala 1st Block, Bangalore', 'Race Course Road, Bangalore',
       'Nexus, Koramangala, Bangalore']

def app():
    st.title("Restaurant Recommender")

    # Add user input fields
    cuisine = st.selectbox('Cuisine:', cuisines_list)
    location = st.selectbox('location:', address_list)
    # Add a button to call the function
    if st.button("Recommend"):
        # Call the function and display the results
        results = recommend_restaurant(cuisine, location)
        for key, value in results.items():
            st.write(f"{key}: {value}")

# Run the app
if __name__ == '__main__':
    app()