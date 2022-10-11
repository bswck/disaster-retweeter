
# Disaster Retweeter
A Twitter bot which purpose is to retweet tweets that relate to emergencies such as fires, storms, explosions and other types of disasters.

## 🔗 Related Projects 
* Parent repository: [nlp-disaster-tweets](https://github.com/SzymkowskiDev/nlp-disaster-tweets)
* Live bot analytics: [nlp-disaster-tweets.com](https://nlp-disaster-tweets.herokuapp.com/)
* Related: [Kaggle problem](https://www.kaggle.com/competitions/nlp-getting-started/overview)

## 👨‍💻 Contributing
* [bswck](https://github.com/bswck)
* [SzymkowskiDev](https://github.com/SzymkowskiDev)
* [OlegTkachenkoY](https://github.com/OlegTkachenkoY)
* [PanNorek](https://github.com/PanNorek)


## 📂 Directory Structure
```
├───media
│   ├───banner.png
│   └───profile_picture.png
├───tests
│   ├───test_classification.py
│   ├───test_crawler.py
│   ├───test_db.py
│   ├───test_retweeter.py
│   ├───test_web_app.py
│   └───test_web_client.py
├───retweeter
│   ├───__init__.py
│   ├───classification.py
│   ├───crawler.py
│   ├───retweeter.py
│   └───db
│       ├───analytics
│       │   ├───crud.py
│       │   ├───database.py
│       │   └───schemas.py
│       └───persistent_log
│           ├───crud.py
│           ├───database.py
│           ├───models.py
│           └───schemas.py
└───retweeter_web
    ├───client.py
    └───app
        ├───__init__.py
        ├───dependencies.py
        ├───main.py
        └───routers
            ├───analytics.py
            └───logs.py

```

## 🏛️ Architecture
Link to the wiki or external site.

## 🎓 Learning Materials
* [Twitter Developer Platform](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api)
* [Tweepy Documentation](https://docs.tweepy.org/en/latest/)
* [FastAPI documentation](https://fastapi.tiangolo.com/)
