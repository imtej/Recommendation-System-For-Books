# End-to-End Recommendation System Project


## Recommendation System for Books

### Introduction About the Data :


**Book Recommendation Kaggle dataset:** 
In a very general way, recommender systems are algorithms aimed at suggesting relevant items to users (items being movies to watch, text to read, products to buy or anything else depending on industries).

**Content:**

The Book-Crossing dataset comprises 3 files.

**Users:**

Contains the users. Note that user IDs (`User-ID`) have been anonymized and map to integers. Demographic data is provided (`Location`, `Age`) if available. Otherwise, these fields contain NULL-values.


**Books:**

Books are identified by their respective `ISBN`. Invalid ISBNs have already been removed from the dataset. Moreover, some content-based information is given (`Book-Title`, `Book-Author`, `Year-Of-Publication`, `Publisher`), obtained from Amazon Web Services. Note that in the case of several authors, only the first is provided. URLs linking to cover images are also given, appearing in three different flavours (`Image-URL-S`, `Image-URL-M`, `Image-URL-L`), i.e., small, medium, and large. These URLs point to the Amazon website.


**Ratings:**

Contains the book rating information. Ratings (`Book-Rating`) are either explicit, expressed on a scale from 1-10 (higher values denoting higher appreciation), or implicit, expressed by 0.

Kaggle Dataset Source Link:
[https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset?resource=download]

### Project Objective

- Build and deploy an ML Model (Recommendation System) which takes a book name as input and recommends similar books as per the collaborative ratings of the users. Along with that it also shows the most popular top 50 books as per the ratings of the users.



# Approach for the project 


#### Data Ingestion

 **Loading the Data**: Every csv dataset `books`, `Users`, and `Ratings` are loaded into pandas DataFrames.

#### Data Transformation

- **Data Preparation:**
   
   - Cleaning the data
   - Handling missing values
   - Handling Categorical features
   - Feature engineering

#### Model Building
  - Generated new Features like `num_ratings`, `avg_ratings` after merging the relevant dataframes to find the insights. (eg: `popular_df` have the top 50 most popular Books as per the ratings of the users.)
  - **Vectorization of user-book interactions:** Vectorization of Books having Users' ratings as the elements of the vector in higher dimensional space. (No. of relevant users = Dimensionality of space, No. of relevant Books = No. of vectors (points) in that higher dimensional space.)
  - Made the pandas `pivot table` for the vectorization.
  - Employed `collaborative filterings technique` as `cosine similarities` amongst the books to find the recommendation of similar books as per the collaborative ratings of the users.
  - Defined and implemented the `recommend function` which takes input as Book Title and follows the considerations of `collaborative filterings` into the account to give the recommendations of similar Books.
 
#### Model Saving
 - stored (`serialized`) the relevant dataframes and models by dumping them in the `pickle` format to load in `app.py`(eg: `books.pkl`, `popular.pkl`, `pivot_table.pkl`, `similarity_scores.pkl`).

#### Flask App creation : 
 - Made `Flask app` using `HTML` (for `css`, implemented `Bootstrap` inside the HTML file) with two pages (`index.html` and `recommend.html`) as a `UI` inside a Web Application.


#### Deployment of Flask application on Render:

 - `Render` deployed link : [https://recommendation-system-for-books.onrender.com/]


# Screenshot of UI
Filling features in the Homepage
![HomepageUI](./Screenshots/student_performance_filled_data.png)
