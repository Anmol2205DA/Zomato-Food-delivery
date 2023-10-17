import streamlit as st
import pandas as pd
import joblib

# Load the prebuilt Random Forest model
model = joblib.load('model.pkl')

# Define a function to make predictions
def predict_price(cuisine, ratings, delivery_reviews_count, restaurant_address):
    # Create a DataFrame with user input
    input_data = pd.DataFrame({
        'ratings': [ratings],
        'cuisine': [cuisine],
        'delivery_reviews_Count': [delivery_reviews_count],
        'restaurant_address': [restaurant_address]
    })

    # Make predictions using the loaded model
    predicted_price = model.predict(input_data)

    return predicted_price[0]

# Streamlit UI
st.title('Restaurant Price Predictor')

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


dic1={'Arabian': 69, ' Biryani': 9, ' North Indian': 44, ' Chinese': 15, ' Fast Food': 20, ' Sichuan': 57, 'Chinese': 80, ' Mughlai': 43, 'Bakery': 73, ' Desserts': 18, 'Burger': 77, ' American': 1, ' Bakery': 6, ' Italian': 28, ' Oriental': 45, ' Continental': 17, ' Beverages': 8, 'North Indian': 101, ' Rajasthani': 50, ' Mithai': 41, ' BBQ': 5, ' Seafood': 54, ' Arabian': 3, 'Pizza': 104, ' Pasta': 48, ' Kebab': 32, ' South Indian': 58, 'Biryani': 76, ' Andhra': 2, 'Fast Food': 83, ' Rolls': 51, ' Burger': 11, 'Mithai': 96, ' Street Food': 59, ' Wraps': 66, ' Sandwich': 53, 'Ice Cream': 85, ' Shake': 55, 'Mughlai': 98, 'South Indian': 111, 'Kerala': 90, ' Lebanese': 35, ' Ice Cream': 25, ' Maharashtrian': 37, ' Hyderabadi': 24, ' Pizza': 49, 'Continental': 81, ' Healthy Food': 23, 'Momos': 97, ' Tibetan': 63, 'Mexican': 94, 'Healthy Food': 84, ' Salad': 52, 'Rolls': 106, 'Andhra': 68, ' Afghan': 0, 'Street Food': 112, ' Tea': 61, ' Juices': 30, 'Beverages': 75, 'Tea': 113, ' Coffee': 16, ' Asian': 4, ' Thai': 62, ' Malaysian': 38, ' Lucknowi': 36, 'Waffle': 115, ' Pancake': 46, ' Chettinad': 14, ' Momos': 42, ' Cafe': 13, ' Japanese': 29, ' Indonesian': 26, 'Desserts': 82, 'Sandwich': 107, 'Asian': 70, 'Cafe': 78, 'Wraps': 116, 'Shawarma': 110, 'Lebanese': 91, 'Shake': 109, 'Juices': 88, 'Afghan': 67, ' Waffle': 65, 'Mangalorean': 93, ' Kerala': 33, ' Bengali': 7, ' Mexican': 39, ' French': 22, ' Panini': 47, 'Portuguese': 105, 'Japanese': 87, ' Korean': 34, ' Sushi': 60, 'Pasta': 103, ' European': 19, 'Middle Eastern': 95, ' Vietnamese': 64, ' Burmese': 12, ' Shawarma': 56, 'Italian': 86, 'Naga': 99, 'BBQ': 72, ' Finger Food': 21, 'Maharashtrian': 92, 'Bengali': 74, ' Mishti': 40, 'Tibetan': 114, 'Awadhi': 71, 'Chettinad': 79, ' Bubble Tea': 10, ' Kashmiri': 31, 'Kebab': 89, ' Iranian': 27, 'Seafood': 108, 'North Eastern': 100, 'Odia': 102} 
dic2={'Vijay Nagar, Bangalore': 65, 'Shanti Nagar, Bangalore': 57, 'Vasanth Nagar, Bangalore': 64, 'St. Marks Road, Bangalore': 60, 'MG Road, Bangalore': 38, 'Koramangala 7th Block, Bangalore': 33, 'UB City, Bangalore': 62, 'Nagawara, Bangalore': 42, 'Brigade Road, Bangalore': 8, 'Shivajinagar, Bangalore': 58, 'Commercial Street, Bangalore': 12, 'Residency Road, Bangalore': 51, 'Frazer Town, Bangalore': 16, 'Mantri Square, Malleshwaram, Bangalore': 41, 'Basavanagudi, Bangalore': 6, 'Malleshwaram, Bangalore': 40, 'Indiranagar, Bangalore': 20, 'Kammanahalli, Bangalore': 27, 'Koramangala 6th Block, Bangalore': 32, 'Jayanagar, Bangalore': 24, 'Rajajinagar, Bangalore': 50, 'Richmond Road, Bangalore': 52, 'Ulsoor, Bangalore': 63, 'Church Street, Bangalore': 10, 'Garuda Mall, Magrath Road, Bangalore': 17, 'Cunningham Road, Bangalore': 13, 'BTM, Bangalore': 2, 'Majestic, Bangalore': 39, 'Wilson Garden, Bangalore': 66, 'Sigma Mall, Cunningham Road, Bangalore': 59, 'Domlur, Bangalore': 14, 'Seshadripuram, Bangalore': 56, 'JP Nagar, Bangalore': 22, 'Lavelle Road, Bangalore': 37, 'Koramangala 8th Block, Bangalore': 34, 'Koramangala 5th Block, Bangalore': 31, 'Sadashiv Nagar, Bangalore': 54, 'Jeevan Bhima Nagar, Bangalore': 25, 'Old Madras Road, Bangalore': 46, 'Koramangala 4th Block, Bangalore': 30, 'Banashankari, Bangalore': 3, 'HBR Layout, Bangalore': 18, 'Basaveshwara Nagar, Bangalore': 7, 'Old Airport Road, Bangalore': 45, 'Thippasandra, Bangalore': 61, 'RT Nagar, Bangalore': 48, 'Kumaraswamy Layout, Bangalore': 35, 'Orion East, Banaswadi, Bangalore': 47, 'Hosur Road, Bangalore': 19, 'Bannerghatta Road, Bangalore': 5, 'Langford Town, Bangalore': 36, 'Yeshwantpur, Bangalore': 67, 'Building 105, Koramangala 5th Block, Bangalore': 9, 'Ejipura, Bangalore': 15, 'Banaswadi, Bangalore': 4, 'City Market, Bangalore': 11, 'Jatti Building, Koramangala 5th Block, Bangalore': 23, '153 Biere Street, Bangalore': 1, '1 Sobha, Bangalore': 0, 'New BEL Road, Bangalore': 43, 'Royal Orchid Hotel,  Old Airport Road, Bangalore': 53, 'Sanjay Nagar, Bangalore': 55, 'Kalyan Nagar, Bangalore': 26, 'Koramangala 2nd Block, Bangalore': 29, 'Infantry Road, Bangalore': 21, 'Koramangala 1st Block, Bangalore': 28, 'Race Course Road, Bangalore': 49, 'Nexus, Koramangala, Bangalore': 44}


# User input
cuisine = st.selectbox('Cuisine:', cuisines_list)
ratings = st.number_input('Ratings')
delivery_reviews_count = st.number_input('Delivery Reviews Count:')
restaurant_address = st.selectbox('address:', address_list)
if st.button('Predict Price'):
    # Ensure the user has provided input
    if cuisine and restaurant_address:
        for i,j in dic1.items():
            if i==cuisine:
                cuisine=j
        for i,j in dic2.items():
            if i==restaurant_address:
                restaurant_address=j

        predicted_price = predict_price(cuisine, ratings, delivery_reviews_count, restaurant_address)
        st.success(f'Predicted Price: {predicted_price:.2f}')
    else:
        st.error('Please provide Cuisine and Restaurant Address.')