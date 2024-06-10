from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

# Load pickled data
books = pickle.load(open('model_files_as_pickle/books.pkl', 'rb'))
popular_df = pickle.load(open('model_files_as_pickle/popular.pkl', 'rb'))
pivot_table = pickle.load(open('model_files_as_pickle/pivot_table.pkl', 'rb'))
similarity_scores = pickle.load(open('model_files_as_pickle/similarity_scores.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                           book_name=list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           image=list(popular_df['Image-URL-M'].values),
                           votes=list(popular_df['num_ratings'].values),
                           rating=list(popular_df['avg_rating'].values),
                           published_year=list(popular_df['Year-Of-Publication'].values)
                           )

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_books', methods=['post'])
def recommend():
    user_input = request.form.get('user_input')
    if not user_input:
        return render_template('recommend.html', 
                               error="Please enter a book name to get recommendations.")

    try:
        index = np.where(pivot_table.index == user_input)[0][0]
        similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[0:8]
        data = []
        for i in similar_items:
            item = []
            temp_df = books[books['Book-Title'] == pivot_table.index[i[0]]]
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Year-Of-Publication'].values))
            data.append(item)
        return render_template('recommend.html', data=data)
    except IndexError:
        return render_template('recommend.html', 
                               error="Book not found. Please try a different book name.")

@app.route('/suggest_books', methods=['get'])
def suggest_books():
    query = request.args.get('query', '')
    suggestions = [book for book in pivot_table.index if query.lower() in book.lower()]
    return jsonify(suggestions)

if __name__ == '__main__':
    app.run(debug=True)
