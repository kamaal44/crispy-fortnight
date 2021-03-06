import argparse
import logging

logger = logging.getLogger(__name__)

class MyParserException(Exception):
    """ Custom exception. """
    pass

class CrispyArgumentParser(argparse.ArgumentParser):
    """ Forced to override argparse methods. """
    def __init__(self, *args, **kwargs):
        argparse.ArgumentParser.__init__(self, *args, **kwargs)

    def parse_known_args(self, args=None, namespace=None):
        """ Override method to prevent -h from printing then calling sys.exit(). """
        
        try:
            return argparse.ArgumentParser.parse_known_args(self, args, namespace)
        except SystemExit:
            pass
        
        return None, None

    def error(self, message):
        """ Override method to prevent argparse from calling sys.exit(). """
        
        self.print_usage()
        raise MyParserException
