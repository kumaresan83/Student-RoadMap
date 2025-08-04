from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load course catalog
with open("final_course_catalog.json", "r") as f:
    course_catalog = json.load(f)

# Helper function to recommend courses
def recommend_courses(level=None, category=None):
    results = []
    for course in course_catalog:
        if (not level or course['Level'].lower() == level.lower()) and \           (not category or course['Category'].lower() == category.lower()):
            results.append(course)
    return results[:5]  # Top 5 matches

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    level = data.get('level')
    category = data.get('category')
    results = recommend_courses(level, category)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)