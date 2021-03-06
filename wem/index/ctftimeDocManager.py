from wem.index.spec.iDocManager import iDocManager
import pickle, time


class ctftimeDocManager(iDocManager):
    """
    Document Manager can save/load document to/from a pickle file
    """

    def __init__(self, filename):
        super().__init__()
        self._pickleFile = filename
        self._documents = None

    def saveToPickle(self, documents):
        """
        Save every Document in a pickle file
        :return: pickle file name
        """
        self._documents = documents
        pickle.dump(documents, open(self._pickleFile, "wb"))
        print("docs saved into %s" %(self._pickleFile))
        return self._pickleFile

    def openPickle(self, filename):
        """
        Open a specific pickle file
        :param filename: file name
        :return: List of Document
        """
        self._documents = pickle.load(open(filename, "rb"))
        return self._documents

    def getFileName(self):
        return self._pickleFile

    def getDocuments(self):
        """
        Return previously opened documents
        :return: list of documents
        """
        return self._documents
