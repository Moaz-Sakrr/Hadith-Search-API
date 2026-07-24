from flask import Flask , request , jsonify
from flasgger import Swagger
from utilz import load_data
from preprocess import Preprocess
from Search import Search

df = load_data()
preprocessor = Preprocess()
Searcher = Search(df, preprocessor = preprocessor)


app = Flask(__name__)
swagger = Swagger(app)

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'message': 'Welcome to the Hadeth Search API',
        'description': 'API for searching hadeths',
        'swagger': '/apidocs',
        'Search_example': "/search?search=الصيام"
    })

@app.route('/clean', methods=['GET'])
def clean_input():
    """
    Clean the user input to remove any special characters and the TASHKIL 
    ---
    tags:
        - clean
    parameters:
        - name: search
          in: query
          type: string
          required: true
          description: The user input to clean
          example: وَاللَّهُ يَعْصِمُكَ مِنَ النَّاسِ
    responses:
        200:
            description: Cleaned input
        400:
            description: Invalid input
    """
    user_input = request.args.get('search')
    if not user_input:
        return jsonify({'error': 'Search query is required'}), 400
    cleaned_input = preprocessor.clean_text(user_input)
    return jsonify({'cleaned_input': cleaned_input})

@app.route('/search', methods=['GET'])
def search():
    """
    Search Hadiths
    ---
    tags:
      - Search
    parameters:
      - name: search
        in: query
        type: string
        required: true
        description: Search query
        example: التقوى
    responses:
      200:
        description: Successful search
      400:
        description: Missing parameter
    """
    user_input = request.args.get('search')

    if not user_input:
        return jsonify({'error': 'Missing search parameter'}), 400

    results = Searcher.find_closest_match(user_input, top_n=10)

    return jsonify({
        'original': user_input,
        'processed': results
    })

@app.route('/search/exact', methods=['GET'])
def exact_search():
    """
    Exact Match Search
    ---
    tags:
      - Search
    parameters:
      - name: search
        in: query
        type: string
        required: true
        description: Exact search query
        example: قال رسول الله صلى الله عليه و سلم 
    responses:
      200:
        description: Successful exact match search
      400:
        description: Missing parameter
    """
    user_input = request.args.get('search')

    if not user_input:
        return jsonify({'error': 'Missing search parameter'}), 400

    results = Searcher.exact_match(user_input)

    return jsonify({
        'original': user_input,
        'processed': results
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)