from typing import Text, Dict, List, Union, Tuple, Any, Callable, Set
from instabase.model_utils.classifier import ClassifierInput
import logging


def get_logger(datapoint: ClassifierInput):
    logger, err = datapoint.get_fn_ctx().get_by_col_name('LOGGER')
    return logger


def get_clients(datapoint: ClassifierInput):
    clients, err = datapoint.get_fn_ctx().get_by_col_name('CLIENTS')
    return clients


class DocsizePrediction(object):  # You don't need to subclass Prediction
    def __init__(self, best_match):
        self.best_match = best_match
        self.debugging_data = dict()

def transform_path(input_path):
    parts = input_path.split('/')
    filename_with_extension = parts[-1]
    filename, extension = filename_with_extension.rsplit('.', 1)
    new_filename = filename.split('_')[0] + '.eml'
    parts[-1] = new_filename + '.' + 'pdf'

    new_path = '/'.join(parts)
    logging.info(f'new_path is : {new_path}')

    return new_path


class DocsizeDemoClassifier(object):  # You don't need to subclass Classifier
    """
    This is a demo heuristic Classifier.
    """

    def get_type(self):
        return u'ib:heuristic-demo'

    def get_version(self):
        return u'1.0.0'

    def train(self, training_context, reporting_context):
        """
        No training is necessary; this is a heuristic model.
        """
        return dict(), None

    def export_parameters_to_string(self):
        """
        Returns an empty string; this is a heuristic model.
        """
        return u'', None

    def load_parameters_from_string(self, model_string, model_metadata=None):
        """
        No-op; this is a heuristic model.
        """
        return True, None

    def predict(self, datapoint):
        """
        Classifies a document into categories EMPTY, SMALL, MEDIUM, and LARGE
        based on arbitrary thresholds defined in the constants at the top of the
        file.
        """
        try:
            logger = get_logger(datapoint)
            clients = get_clients(datapoint)
            parsed_ibocr = datapoint.get_ibocr()
            best_match = 'Pdf'
            supported_formats = ['pdf','jpeg','png','jpg','eml']

            for record in parsed_ibocr.get_ibocr_records():
                filetype = record.get_document_path().split('.')[-1]
                document_path = record.get_document_path()
                
                logging.info(f'document path : {record.get_document_path()}')
                
                extension = document_path.split('.')[-1]

                logging.info(f'extension is : {extension}')

                if document_path.lower().endswith('.jpeg') or document_path.lower().endswith('png'):
                    best_match = 'Image'
                break
            return DocsizePrediction(best_match), None
        except Exception as e:
            logging.info(f'error in predict method {e}')
            return DocsizePrediction('Pdf'), None


def register_classifiers():
    return {'ib:custom-classifier': {'class': DocsizeDemoClassifier}}
