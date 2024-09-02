import unittest
from EmotionDetection import emotion_detector

class test_emotion_detector(unittest.TestCase):

    def test_emotions(self):
        test_sentences = {
            "I am glad this happened": 	"joy",
            "I am really mad about this":"anger",
            "I feel disgusted just hearing about this":"disgust",
            "I am so sad about this":"sadness",
            "I am really afraid that this will happen":"fear"
        }

        for text, expected_emotion in test_sentences.items():
            predicted_emotions = emotion_detector(text)
            assert predicted_emotions["dominant_emotion"] == expected_emotion

if __name__ == '__main__':
    unittest.main()
