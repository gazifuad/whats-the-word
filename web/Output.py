import numpy as np
from Bert_Model import Bert_Model
from Bert_Summarizer import Bert_Summarizer
from speech_to_text import speech_to_text

class Output:

    def __init__(self):
        self.sentences = None
        self.bert = Bert_Model()

    def set_sentences(self, sentences_list):
        self.sentences = sentences_list

    def set_sentences_using_srt_path(self, path):
        self.set_sentences(self.bert.make_english_sentences(path))

    def set_sentences_using_mp3_path(self, path):
        self.set_sentences(speech_to_text(path))

    def compute_notes(self):
        bert_encode = self.bert.run_bert_encoding(self.sentences)
        summary = Bert_Summarizer(self.sentences, bert_encode)
        sentence_ind, kmeans, n_cluster = summary.get_indices()
        return summary.indices_to_english(sentence_ind, toPrint=False)


# out1 = Output()
# out1.set_sentences_using_srt_path('Test_SRT.srt')
# print(out1.compute_notes())

# out2 = Output()
# out2.set_sentences_using_mp3_path("gs://lecture_audio_files/Phil Lempert's 2 minute Speech Demo.mp3")
# print(out2.compute_notes())

