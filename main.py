from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {
        'Hello': 'World'
    }

@app.get('/tweets/{tweet_id}/')
def tweets(tweet_id):
    return {
        'tweet_id' : tweet_id
    }



