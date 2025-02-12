#!/usr/bin/env python
import sys
import warnings
from datetime import datetime
from talent_finder.crew import SearchScrapeCrew
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'Software Engineer in Starkville, MS',
        'date': datetime.now().strftime('%Y-%m-%d')
    }
    
    SearchScrapeCrew().crew().kickoff(inputs=inputs)

run()
