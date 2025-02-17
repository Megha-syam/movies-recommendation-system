**Movie Recommendation System**

**📌 Overview**

This project is a Content-Based Movie Recommendation System implemented using Jupyter Notebook for data processing and model training, and Streamlit for the frontend UI. The system recommends movies based on the similarity of movie descriptions and metadata.

**🚀 Features**

**Content-Based Filtering**: Uses movie metadata to find similar movies.

**Data Preprocessing**: Cleans and structures the dataset for analysis.

**TF-IDF Vectorization**: Converts movie descriptions into numerical vectors.

**Cosine Similarity**: Measures similarity between movie vectors.

**Interactive UI**: Built with Streamlit for user-friendly recommendations.

**Movie Posters Fetching**: Uses TMDb API to fetch movie posters dynamically.

**🛠️ Tools & Technologies Used**

**Python:** Core programming language

**Pandas**: For data preprocessing

**NumPy:** Efficient numerical computations

**Scikit-learn**: Used for vectorization and similarity calculations

**NLTK**: Text preprocessing and tokenization

**Pickle:** Model serialization for efficiency

**Requests**: Fetching data from external APIs

**Streamlit**: Interactive frontend design

**TMDb API**: Fetching movie metadata and posters

**🔧 How to Run the Project**

**1️⃣ Install Dependencies**

Ensure you have Python 3.x installed, then run:

pip install -r requirements.txt

**2️⃣Run Jupyter Notebook**

jupyter notebook

Open the notebook and run all cells to process the data and train the model.

**3️⃣ Run Streamlit App**

streamlit run app.py



The system fetches the most similar movies and displays recommendations along with posters.

**📸 Screenshots**

![image](https://github.com/user-attachments/assets/77cc6466-c9c8-4383-ab50-f43c0cad58d5)

![image](https://github.com/user-attachments/assets/c502471b-538f-4cd0-87fe-938fcb1cf080)



**🔗 Future Enhancements**

Implement Hybrid Filtering by incorporating collaborative filtering.

Improve recommendations by using Deep Learning (e.g., NLP-based embeddings).

Optimize UI/UX with a more dynamic design.

Add user ratings & reviews for better personalization.

**🤝 Acknowledgments**

TMDb API for providing movie metadata and posters.

Open-source datasets used for training.

**🔥 Hope you enjoy using this Movie Recommendation System! 🎬**
