# Travel.pk Review Sentiment Checker

## What I Built
The **Travel.pk Review Sentiment Checker** is a lightweight, web-based internal tool built for TechAbout's OTA platform. It allows customer service agents and managers to instantly analyze user reviews for flights, hotels, and holiday packages. By pasting a review into the tool, users receive an immediate classification (**Positive, Neutral, or Negative**) along with a percentage-based confidence score. 

## How I Built It
This tool prioritizes speed and simplicity without requiring heavy machine learning frameworks or expensive API calls.
* **Frontend UI:** Built with **Streamlit** (Python) for a fast, responsive, and visually appealing dashboard.
* **Sentiment Engine:** Powered by **NLTK VADER** (Valence Aware Dictionary and sEntiment Reasoner). VADER is a rule-based sentiment analysis model specifically optimized for social media, short-form text, and customer reviews.
* **Logic:** The application extracts the `compound` score from VADER (ranging from -1.0 to +1.0) and uses a set threshold to categorize the text, rendering dynamic color-coded feedback.

## What It Can Do
* **Instant Classification:** Quickly determines if a piece of text leans positive, negative, or neutral.
* **Confidence Scoring:** Translates raw algorithmic scores into an easy-to-read percentage.
* **Handles Slang & Emojis:** VADER is specifically trained to understand modern digital text, including punctuation (like exclamation marks) and common emojis.
* **Local Processing:** Runs entirely locally without needing internet access for third-party AI APIs, ensuring customer data privacy and zero API costs.

## What It Can't Do (Limitations)
Because VADER is a rule/lexicon-based model (it looks at a dictionary of words rather than understanding deep context like an LLM), it struggles with certain human nuances:
1. **Sarcasm:** A review like *"Oh brilliant, another 6-hour flight delay. Just what I needed!"* contains positive words ("brilliant", "needed"). The model will likely flag this as Positive or Neutral, completely missing the angry sarcasm.
2. **Contextual Negativity:** *"My hotel room was right next to the elevator and the ice machine."* Any human traveler knows this is a terrible, noisy experience. However, since there are no inherently "negative" words in the sentence, the model will score it as Neutral.
3. **Mixed Sentiments:** *"The view from the balcony was absolutely breathtaking, but the bed bugs completely ruined our vacation."* The extreme positive of "breathtaking" cancels out the extreme negative of "ruined," causing the model to output Neutral—missing the fact that the customer had a terrible overall experience.

## 15 Test Sentences & Results

| # | Test Sentence (Review) | Expected Result |
|---|---|---|
| 1 | The room was spacious and the bed was incredibly comfortable. | Positive 🟢 |
| 2 | Absolutely terrible experience, the bathroom was filthy. | Negative 🔴 |
| 3 | The hotel is located in the city center. | Neutral ⚪ |
| 4 | We loved the breakfast buffet, highly recommended! | Positive 🟢 |
| 5 | Flight was delayed by 4 hours and no one helped us. | Negative 🔴 |
| 6 | It was an average stay, nothing special but not bad either. | Neutral ⚪ |
| 7 | The staff went out of their way to make our anniversary special. | Positive 🟢 |
| 8 | AC was broken and the room was boiling hot all night. | Negative 🔴 |
| 9 | The resort offers free Wi-Fi and complimentary parking. | Neutral ⚪ |
| 10 | Beautiful views from the balcony, I would definitely come back. | Positive 🟢 |
| 11 | Hidden charges on the final bill completely ruined our trip. | Negative 🔴 |
| 12 | Check-in is at 3 PM and check-out is at 11 AM. | Neutral ⚪ |
| 13 | The tour guide in Hunza was very knowledgeable and friendly. | Positive 🟢 |
| 14 | Food at the hotel restaurant was bland and overpriced. | Negative 🔴 |
| 15 | The airport transfer was provided as part of the holiday package. | Neutral ⚪ |
