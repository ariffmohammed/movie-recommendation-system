# Movie Recommendation System

A machine learning project that recommends movies based on user ratings using collaborative filtering and cosine similarity. Built with Python and scikit-learn.

## How It Works

The model builds a matrix of movies and user ratings. It then calculates cosine similarity between every pair of movies — movies rated similarly by the same users score high, movies rated differently score low. Given a movie you liked, it returns the most similar ones.

## Example

Input: Inception
Output:
- Interstellar — 0.97
- The Dark Knight — 0.84
- Avengers — 0.48

## What I Learned

- Collaborative filtering — a completely different type of ML from classification
- Cosine similarity — measuring similarity between vectors mathematically
- Item based recommendation logic
- How Netflix and Spotify style recommendation systems work at a fundamental level
- Pandas matrix operations

## Limitations

- Small hardcoded dataset of 7 movies
- Full version using MovieLens 100,000 rating dataset coming soon

## Tech Stack

- Python
- scikit-learn
- Pandas

## Dataset

Sample data hardcoded for demonstration. Full project will use the [MovieLens Small Dataset](https://grouplens.org/datasets/movielens/latest/) with 9,000 movies and 100,000 ratings.
