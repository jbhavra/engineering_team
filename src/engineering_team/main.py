#!/usr/bin/env python
import sys
import warnings
import os

from datetime import datetime

from engineering_team.crew import EngineeringTeam

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

requirements = # your rewuirements here
module_name = # your module name here
class_name = # your class name here

def run():
    """
    Run the engineering crew.
    """
    inputs = {
        'requirements': requirements,
        'module_name': module_name,
        'class_name': class_name
    }

    result = EngineeringTeam().crew.kickoff(inputs=inputs)

if __name__ == "__main__":
    run()


