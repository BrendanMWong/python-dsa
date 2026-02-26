class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        output = []
        # keep track of if word can fit into a line
        total_letters = 0
        # store words to use for counting and justification
        current_words = []
        for word in words:
            # if next word will overflow
            if total_letters + len(current_words) + len(word) > maxWidth:
                # determine how long the spaces between letters should be
                total_spaces = maxWidth - total_letters
                gaps = len(current_words) - 1

                # generate the next line for the output
                if gaps == 0:
                    line = current_words[0] + " " * total_spaces
                else:
                    # inside loop to avoid divide by 0 errors
                    base_spaces = total_spaces // gaps
                    first_space = total_spaces % gaps

                    line = ""
                    for i in range(gaps):
                        line += current_words[i]
                        if i < first_space:
                            line += " " * (base_spaces + 1)
                        else:
                            line += " " * base_spaces
                    line += current_words[-1]

                # put that line into the output
                output.append(line)
                current_words = []
                total_letters = 0

            # put the current word into current_words to be stored
            current_words.append(word)
            # keep track of how many letters there are in current_words
            total_letters += len(word)
        # if current_words isn't empty, deal with leftovers
        if current_words:
            line = " ".join(current_words)
            output.append(line + " " * (maxWidth - len(line)))
        return output
        