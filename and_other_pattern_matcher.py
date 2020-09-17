from pattern_matcher import PatternMatcher
from spacy.tokens import Doc
from relation import Relation


class AndOtherPatternMatcher(PatternMatcher):


    def __init__(self, nlp):
        '''
        "look for structures containing 4 words: 
        1. the first word is a NOUN (POS stands for Part-Of-Speech), 
        2. second word is <<and>>, 
        3. third is <<other>>
        4.  and the last word is also a Noun".
        '''

        pattern = [{'POS': 'NOUN'},
                   {'LOWER': 'and'},
                   {'LOWER': 'other'},
                   {'POS': 'NOUN'}]
        PatternMatcher.__init__(self, pattern, nlp, "andOther")

    def getRelations(self, doc: Doc) -> [Relation]:
        '''

        returns a list of spaCy Span objects
        '''
        relations = []
        matches = self._matcher(doc)
        for match_id, start, end in matches:
            span = doc[start:end]
            firstToken = span.root.head
            results = [firstToken]
            while firstToken and firstToken.head.pos_ == "NOUN":
                results.append(firstToken.head)
                firstToken = firstToken.head
            hypernym = span.text.split()[-1]
            relations.append(Relation(hypernym, span.text.split()[0]))
            if len(results) > 0:
                for result in results:
                    relations.append(Relation(hypernym, result.text))
        return relations


