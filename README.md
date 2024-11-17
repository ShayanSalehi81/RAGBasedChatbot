# RAG Based ChatBot Framework with Spelling Correction and Profanity Filtering

This repository provides a framework for building a Persian-language chatbot with capabilities for dynamic text-based question answering, spelling correction, and profanity filtering. Leveraging language models and natural language processing techniques, this chatbot is designed to handle common user queries, identify and correct spelling errors, and filter inappropriate language in Persian.

## Project Structure

- **ChatBot**: Core logic for the chatbot, responsible for answering user questions based on relevant contexts.
  - `ChatBot.py`: Implements a chatbot that utilizes OpenAI's language model (through LangChain integration) to answer questions about specific events (e.g., "Winter Seminar Series") based on contextual information. It also includes retrieval mechanisms to enhance response accuracy.

- **SpellingMistakeCorrector**: Module for correcting spelling mistakes in user queries.
  - `SpellingMistakeCorrector.py`: Uses Levenshtein distance and a BK-tree to identify and correct spelling errors. This component helps improve the chatbot's comprehension of misspelled words by finding the closest correct token in a frequency dictionary.
  - `frequency_combined.csv`: A frequency dictionary that lists commonly used Persian words and their frequencies, enhancing the spell-checking accuracy by prioritizing frequent words.

- **SwearWordDetector**: Module to detect and filter profanity.
  - `SwearWordDetector.py`: Detects and replaces swear words in Persian text with a specified symbol (e.g., `*`). It supports dynamic addition and removal of words in the profanity list.
  - `swear_words.json`: Contains a list of Persian swear words used by `SwearWordDetector` to identify inappropriate language in user input.

- **Main.py**: Entry point script that brings together all modules (ChatBot, SpellingMistakeCorrector, and SwearWordDetector) to create an interactive chatbot experience with additional text processing functionalities.

- **requirements.txt**: Lists Python dependencies required to run the project.

## Key Features

- **Context-Based Question Answering**: The chatbot is equipped with a context-based retrieval system using FAISS and LangChain's OpenAI model to answer questions based on pre-loaded context documents (such as "Winter Seminar Series" event information). If the answer is not known, the bot will respond accordingly.
- **Spelling Correction**: Uses a Levenshtein-based BK-tree to identify and correct spelling mistakes in Persian. The `SpellingMistakeCorrector` improves the chatbot's ability to understand and respond to user queries despite potential misspellings.
- **Profanity Filtering**: Automatically detects and replaces Persian swear words to maintain appropriate interactions. The `SwearWordDetector` can dynamically update its list of offensive words, making it adaptable to different contexts.
- **Prompt-Based Query Transformation**: `ChatBot.py` includes a query transformation chain to rephrase user questions into general queries before retrieving contextually relevant information.

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/ShayanSalehi81/RAGBasedChatbot
   cd RAGBasedChatbot
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Ensure the `.env` file is set up with the necessary credentials (e.g., OpenAI API key).

4. Prepare context files for the chatbot to use as background information for answering questions. Save these files in a folder named `datasets` (e.g., `datasets/QA.txt` and `datasets/dataset.txt`).

## Usage

To run the chatbot, execute `Main.py`:

```bash
python Main.py
```

The chatbot will load context data from specified files, allowing it to answer questions based on pre-defined information. Users can interact with the bot via the console or integrate it into a web interface.

### Example Usage of Each Module

- **ChatBot**:
  ```python
  from ChatBot.ChatBot import Chat

  chat = Chat()
  user_input = "What is Abriment"
  response = chat.chat(user="user1", message=user_input)
  print(response)  # Outputs the chatbot's response based on available context
  ```

- **Spelling Correction**:
  ```python
  from SpellingMistakeCorrector.SpellingMistakeCorrector import SpellingMistakeCorrector

  corrector = SpellingMistakeCorrector("SpellingMistakeCorrector/frequency_combined.csv", threshold=0.3)
  corrected_text = corrector.correct_spelling("مثال ناصحی")
  print(corrected_text)  # Corrects spelling mistakes in Persian text
  ```

- **Profanity Filtering**:
  ```python
  from SwearWordDetector.SwearWordDetector import SwearWordDetector

  detector = SwearWordDetector("SwearWordDetector/swear_words.json")
  clean_text = detector.filter_words("Some text with a swear word.")
  print(clean_text)  # Filters and replaces swear words with asterisks
  ```

## Future Enhancements

- **Enhanced Contextual Retrieval**: Implement more advanced retrieval techniques for better response accuracy.
- **Customizable Profanity Filter**: Allow users to upload custom profanity lists for more flexible filtering.
- **Multi-Language Support**: Expand the framework to support additional languages for broader usability.
- **Real-Time Spell Correction Feedback**: Provide spelling suggestions in real-time as users type queries.

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Feel free to submit issues, feature requests, or pull requests to enhance this project.
