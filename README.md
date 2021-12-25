# _What's the Word?_

What’s the Word? is a lecture-notes assistant web app that condenses hefty audio lectures and transcripts into manageable bullet-point summaries. We used tools such as Bidirectional Encoder Representations from Transformers (BERT) to perform natural language processing and convert English sentences into numerical vectors, k-means clustering to find clusters of sentence ideas, Google Cloud's Speech-to-text API, Web Stack, and Flask.

Check out our video explaining it below:

[![Watch the video](https://img.youtube.com/vi/xLZnbt6bYIY/maxresdefault.jpg)](https://www.youtube.com/watch?v=xLZnbt6bYIY)

Our Devpost submission can be found [here](https://devpost.com/software/what-s-the-word-machine-learning-to-summarize-lectures).

## Run

Clone, install requirements from `requirements.txt`, and from within `web/` run:

```sh
FLASK_APP=app flask run
```

## Team

[Gazi Fuad](https://github.com/gazifuad), [George Lyu](https://github.com/SeventhPrize), [Shreyas Minocha](https://github.com/shreyasminocha) & [Zachary Katz](https://github.com/unary-code)
