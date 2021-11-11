from flask import Flask, json, jsonify, request
import csv

allArticles = []

file = open('article.csv', encoding='utf-8')
reader = csv.reader(file)

data = list(reader)
allArticles = data[1:]

likedArticles = []
dislikedArticles = []

app = Flask(__name__)

@app.route('/get-article')
def get_article():
    return jsonify({
        'data' : allArticles[0],
        'status' : 'Success',
    })

@app.route('/liked-article', methods=['POST'])
def liked_article():
    article = allArticles[0]
    allArticles = allArticles[1:]
    likedArticles.append(article)
    return jsonify({
        'status' : 'Success'
    }),201

@app.route('/dislike-article', methods=['POST'])
def disliked_article():
    article = allArticles[0]
    allArticles = allArticles[1:]
    dislikedArticles.append(article)
    return jsonify({
        'status' : 'Success'
    }),201

if __name__ == '__main__':
    app.run()