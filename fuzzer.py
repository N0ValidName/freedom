from config import TreeConfig, GlobalConfig
from document import Document
from document.arkts import ArkTSDocument
from utils.random import Random

import os
import time
import pickle
from enum import Enum


class Fuzzer:
    def __init__(self, executor, manager):
        super().__init__()
        self.manager = manager
        self.executor = executor
        self.start_time = time.time()

    def generate_one(self):
        document = Document(Random.range(TreeConfig.min_element_count, TreeConfig.max_element_count))
        document.generate_nodes()
        document.generate_attributes()
        document.generate_css_rules()
        document.generate_js_functions()
        return document
    
    def generate_arkts_one(self):
        """Generate a single ArkTS document"""
        document = ArkTSDocument()
        document.generate()
        return document

    def generate_only(self, num):
        for i in range(num):
            print("Generating testcase #{}".format(i))
            document = self.generate_one()
            self.manager.save_testcase(document)
        print("Total {} testcases have been written to '{}'".format(num, os.path.abspath(self.manager.output_dir)))
    
    def generate_arkts_only(self, num):
        """Generate only ArkTS testcases"""
        for i in range(num):
            print("Generating ArkTS testcase #{}".format(i))
            document = self.generate_arkts_one()
            self.manager.save_testcase(document)
        print("Total {} ArkTS testcases have been written to '{}'".format(num, os.path.abspath(self.manager.output_dir)))
    
    def generate_hybrid(self, num):
        """Generate both DOM and ArkTS testcases"""
        dom_count = num // 2
        arkts_count = num - dom_count
        
        # Generate DOM testcases
        original_extension = self.manager.file_extension
        self.manager.file_extension = ".html"
        for i in range(dom_count):
            print("Generating DOM testcase #{}".format(i))
            document = self.generate_one()
            self.manager.save_testcase(document)
        
        # Generate ArkTS testcases  
        self.manager.file_extension = ".ets"
        for i in range(arkts_count):
            print("Generating ArkTS testcase #{}".format(dom_count + i))
            document = self.generate_arkts_one()
            self.manager.save_testcase(document)
        
        self.manager.file_extension = original_extension
        print("Total {} testcases ({} DOM, {} ArkTS) have been written to '{}'".format(
            num, dom_count, arkts_count, os.path.abspath(self.manager.output_dir)))

