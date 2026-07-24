from rapidfuzz import process, fuzz
from preprocess import Preprocess

class Search:
    def __init__(
        self,
        df,
        text_column='cleaned_text',
        processed_column='cleaned_text_processed',
        preprocessor: Preprocess = None,
    ):
        self.df = df.reset_index(drop=True)
        self.text_column = text_column
        self.processed_column = processed_column
        self.preprocessor = preprocessor or Preprocess()

    def find_closest_match(self, user_input, top_n=7, threshold=80): 
        if not isinstance(user_input, str) or not user_input.strip():
            return ["Can't search for empty string."]

        processed_input = self.preprocessor.clean_text(user_input)

        all_texts = self.df[self.processed_column].tolist()
        fuzzy_match = process.extract(
            processed_input,
            all_texts,
            scorer=fuzz.partial_ratio,
            limit=top_n,
        )
        fuzzy_results = [
            self.df.iloc[match[2]][self.text_column]
            for match in fuzzy_match
            if match[1] >= threshold
        ]

        keywords = self.df[
            self.df[self.processed_column].str.contains(
                processed_input, na=False, regex=False
            )
        ][self.text_column].tolist()

        all_results = []
        for result in fuzzy_results + keywords:
            if result not in all_results:
                all_results.append(result)
            if len(all_results) >= top_n:
                break
        return all_results if all_results else ["No matching hadeth found."]

    def exact_match(self, user_input): 
        if not isinstance(user_input, str) or not user_input.strip():
            return ["Can't search for empty string."]

        processed_input = self.preprocessor.clean_text(user_input)

        results = self.df[
            self.df[self.processed_column] == processed_input
        ][self.text_column].tolist()

        return results if results else ["No exact match found."]