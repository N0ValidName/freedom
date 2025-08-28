"""
ArkTS Document class for generating ArkTS application files
"""

from generator.arkts_generator import generate_arkts_application


class ArkTSDocument:
    """Document class for ArkTS applications"""
    
    def __init__(self):
        self.content = ""
        self.label = None
    
    def generate(self):
        """Generate ArkTS application content"""
        self.content = generate_arkts_application()
    
    def __str__(self):
        """Return the generated ArkTS content"""
        return self.content