class AbstractLocus:
    def __init__(self, genes=None):
        self._genes = genes
        
    def get_phenotype(self):
        pass

class AbstractLocusGenerator:
    pass