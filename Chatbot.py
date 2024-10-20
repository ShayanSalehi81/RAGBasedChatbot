from SpellingMistakeCorrector.SpellingMistakesCorrector import SpellingMistakeCorrector
from SwearWordDetector.SwearWordDetector import SwearWordDetector


class Chatbot:
    def __init__(self) -> None:
        self.swear_detector = SwearWordDetector('SwearWordDetector/swear_words.json')
        self.spelling_corrector = SpellingMistakeCorrector('SpellingMistakeCorrector/frequency_combined.csv', threshold=0.2)

    def chat(self, query) -> str:
        spellCorrectedQuery = self.spelling_corrector.correct_spelling(query)
        censoredQuery = self.swear_detector.filter_words(spellCorrectedQuery)
        return censoredQuery


if __name__ == '__main__':
    chatbot = Chatbot()
    print(chatbot.chat('صلام'))