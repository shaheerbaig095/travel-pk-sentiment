import streamlit as st
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# MUST BE THE FIRST STREAMLIT COMMAND
st.set_page_config(page_title="Travel.pk Sentiment Checker", layout="centered")

# Download VADER lexicon (runs once)
@st.cache_resource
def download_nltk_data():
    nltk.download('vader_lexicon', quiet=True)

download_nltk_data()

sia = SentimentIntensityAnalyzer()

def analyze_sentiment(review_text):
    scores = sia.polarity_scores(review_text)
    compound = scores['compound']
    
    # Calculate sentiment and assign a UI theme color
    if compound >= 0.05:
        sentiment = "Positive 🟢"
        confidence = max(scores['pos'], abs(compound)) 
        theme = "success"
    elif compound <= -0.05:
        sentiment = "Negative 🔴"
        confidence = max(scores['neg'], abs(compound))
        theme = "error"
    else:
        sentiment = "Neutral ⚪"
        confidence = scores['neu']
        theme = "info"
        
    confidence_pct = round(confidence * 100, 2)
    return sentiment, confidence_pct, scores, theme

# UI Formatting & Layout
st.title("Travel.pk Review Sentiment Checker")
st.markdown("Analyze the sentiment of hotel, flight, and tour reviews for TechAbout's OTA.")
st.divider()

user_review = st.text_area(
    "Enter a customer review below:", 
    height=150, 
    placeholder="e.g., The room was spacious and the bed was incredibly comfortable."
)

# Make the button span the full width for a cleaner look
if st.button("Analyze Sentiment", type="primary", use_container_width=True):
    if user_review.strip():
        sentiment, confidence, raw_scores, theme = analyze_sentiment(user_review)
        
        st.subheader("Analysis Result")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Apply dynamic color boxes based on the result
            if theme == "success":
                st.success(f"**Sentiment:** {sentiment}")
            elif theme == "error":
                st.error(f"**Sentiment:** {sentiment}")
            else:
                st.info(f"**Sentiment:** {sentiment}")
                
        with col2:
            st.metric(label="Confidence Level", value=f"{confidence}%")
            
        st.write("") # Add a small spacing gap
        
        # Detailed Raw Scores section
        with st.expander("📊 View Raw Model Scores & Explanation"):
            st.markdown("""
            **Understanding the VADER Model Outputs:**
            * **`neg`**: The proportion of words in the text classified as negative (0.0 to 1.0).
            * **`neu`**: The proportion of words classified as neutral.
            * **`pos`**: The proportion of words classified as positive.
            * **`compound`**: The primary metric. This is a normalized score ranging from **-1.0** (extremely negative) to **+1.0** (extremely positive). We use this value to determine the final sentiment.
            """)
            st.json(raw_scores)
    else:
        st.warning("Please enter a valid review to analyze.")