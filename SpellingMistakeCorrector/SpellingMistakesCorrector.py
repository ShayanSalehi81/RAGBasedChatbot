import re
import pandas as pd
import Levenshtein

    
class SpellingMistakeCorrector:
    def __init__(self, dict_path, threshold) -> None:
        self.frequency_dict = self.load_frequency_dict(dict_path)
        self.threshold = threshold
        self.max_freq = max(self.frequency_dict.values())
        self.valid_tokens = list(self.frequency_dict.keys())
        self.bk_tree = self.build_bk_tree()

    def levenshtein_distance(self, term1, term2):
        distance = Levenshtein.distance(term1, term2)
        if distance >= 10:
            return 1
        return distance / 10

    def build_bk_tree(self):
        tree = BKTree(self.levenshtein_distance)
        for token in self.valid_tokens:
            tree.add(token)
        return tree

    def load_frequency_dict(self, filepath):
        frequency_df = pd.read_csv(filepath)
        frequency_dict = dict(zip(frequency_df['Token'], frequency_df['Frequency']))
        return frequency_dict

    def tokenize_persian(self, text):
        tokens = re.findall(r'\w+', text)
        return tokens

    def get_closest_token_bktree(self, token):
        candidates = self.bk_tree.find(token, self.threshold)
        closest_token = token
        max_score = 0
        
        for candidate, dist in candidates:
            frequency_score = self.frequency_dict.get(candidate, 0) / self.max_freq
            
            combined_score = ((1 - dist) + (frequency_score / 4)) / 2
            
            if combined_score > max_score:
                max_score = combined_score
                closest_token = candidate
        return closest_token

    def correct_spelling(self, query):
        tokens = self.tokenize_persian(query)
        corrected_tokens = []
                
        for token in tokens:
            closest_token = self.get_closest_token_bktree(token)
            corrected_tokens.append(closest_token)
        
        corrected_query = ' '.join(corrected_tokens)
        return corrected_query
    

class BKTree:
    def __init__(self, distance_fn):
        self.distance_fn = distance_fn
        self.tree = None

    def add(self, term):
        node = (term, {})
        if self.tree is None:
            self.tree = node
        else:
            self._add(self.tree, node)

    def _add(self, parent, node):
        parent_term, children = parent
        term, _ = node
        distance = self.distance_fn(parent_term, term)
        if distance in children:
            self._add(children[distance], node)
        else:
            children[distance] = node

    def find(self, term, max_distance):
        if self.tree is None:
            return []

        candidates = [self.tree]
        found = []

        while candidates:
            candidate, children = candidates.pop()
            distance = self.distance_fn(term, candidate)
            if distance <= max_distance:
                found.append((candidate, distance))

            candidates.extend(child for d, child in children.items()
                              if distance - max_distance <= d <= distance + max_distance)
        return found