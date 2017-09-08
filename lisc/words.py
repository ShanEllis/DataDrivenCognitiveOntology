"""Class for LISC word analysis (text analysis of abstract texts)."""

# Import custom code
from lisc.base import Base
from lisc.scrape import scrape_words

################################################################################################
#################################### LISC - WORDS - Classes ####################################
################################################################################################

class Words(Base):
    """Class for searching through words in the abstracts of specified papers.

    Attributes
    ----------
    result_keys : list of str
        Keys for each result data attached to object.
    results : list of Data() objects
        Results for each ERP, stored in custom Words object.
    """

    def __init__(self):
        """Initialize ERP-SCANR Words() object."""

        # Inherit from ERPSC Base Class
        Base.__init__(self)

        # Initialize a list to store results for all the erps
        self.result_keys = list()
        self.results = list()


    def __getitem__(self, key):
        """Index into Words object with ERP result key.

        Parameters
        ----------
        key : str
            xx
        """

        # Give up if object is empty
        if len(self.result_keys) == 0:
            raise IndexError('Object is empty - cannot index.')

        # Check if requested key is available
        try:
            ind = self.result_keys.index(key)
        except ValueError:
            raise IndexError('Requested key not available in object.')

        return self.results[ind]


    def add_results(self, new_result):
        """Add a new Data results object.

        Parameters
        ----------
        new_result : Data() object
            Object with information about current ERP term.
        """

        self.result_keys.append(new_result.label)
        self.results.append(new_result)


    def run_scrape(self, db='pubmed', retmax=None, use_hist=False, verbose=False):
        """Launch a scrape of words data."""

        self.results, self.meta_dat = scrape_words(self.terms, self.exclusions, db=db,
                                                   retmax=retmax, use_hist=use_hist, verbose=verbose)
        self.results_keys = [dat.label for dat in self.results]
