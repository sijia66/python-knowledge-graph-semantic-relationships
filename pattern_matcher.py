from spacy.matcher import Matcher
from abc import abstractmethod
from spacy.tokens import Doc
from relation import Relation


class PatternMatcher:


    def __init__(self, pattern, nlp, matcherId):
        '''
        The *pattern* para: contains the actual pattern extract the nodes 
        the *nlp* argument: the spaCy pre-trained NLP model. 
        the matcherId string: identify from which matcher each match comes.
        '''
        
        self._nlp = nlp
        self._matcher = Matcher(nlp.vocab)
        self._matcher.add(matcherId, None, pattern)

    @abstractmethod
    def getRelations(self, doc: Doc) -> [Relation]:
        ...
