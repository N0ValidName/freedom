"""
Tests for ArkTS fuzzing functionality
"""

import unittest
import tempfile
import os
import shutil
from unittest.mock import patch

# Add the parent directory to the path so we can import the modules
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from arkui.components import create_component, get_random_component, ArkUIComponent
from arkui.properties import generate_random_properties, get_properties_for_component
from arkui.events import generate_random_events, get_events_for_component
from generator.arkts_generator import ArkTSGenerator, generate_arkts_application
from document.arkts import ArkTSDocument
from fuzzer import Fuzzer
from db import Manager


class TestArkUIComponents(unittest.TestCase):
    """Test ArkUI component functionality"""
    
    def test_create_component(self):
        """Test component creation"""
        component = create_component("Text")
        self.assertIsInstance(component, ArkUIComponent)
        self.assertEqual(component.name, "Text")
        self.assertEqual(component.component_type, "basic")
    
    def test_get_random_component(self):
        """Test random component generation"""
        component_name = get_random_component("container")
        self.assertIn(component_name, ["Column", "Row", "Stack", "Flex", "Grid", "List", "Swiper", "Tabs", "TabContent", "ScrollArea", "RelativeContainer"])
    
    def test_component_hierarchy(self):
        """Test component parent-child relationships"""
        parent = create_component("Column")
        child = create_component("Text")
        
        self.assertTrue(parent.add_child(child))
        self.assertEqual(child.parent, parent)
        self.assertIn(child, parent.children)
    
    def test_leaf_component_no_children(self):
        """Test that leaf components cannot have children"""
        text = create_component("Text")
        button = create_component("Button")
        
        self.assertFalse(text.add_child(button))
        self.assertEqual(len(text.children), 0)


class TestArkUIProperties(unittest.TestCase):
    """Test ArkUI property generation"""
    
    def test_get_properties_for_component(self):
        """Test getting properties for different components"""
        text_props = get_properties_for_component("Text")
        self.assertIn("fontSize", text_props)
        self.assertIn("fontColor", text_props)
        
        button_props = get_properties_for_component("Button")
        self.assertIn("type", button_props)
        
        # All components should have common properties
        self.assertIn("width", text_props)
        self.assertIn("height", button_props)
    
    def test_generate_random_properties(self):
        """Test random property generation"""
        properties = generate_random_properties("Text", max_properties=3)
        self.assertIsInstance(properties, dict)
        self.assertLessEqual(len(properties), 3)
    
    def test_property_values_are_strings(self):
        """Test that property values are properly formatted"""
        properties = generate_random_properties("Button", max_properties=1)
        for prop_name, prop_value in properties.items():
            self.assertIsInstance(prop_value, str)


class TestArkUIEvents(unittest.TestCase):
    """Test ArkUI event generation"""
    
    def test_get_events_for_component(self):
        """Test getting events for different components"""
        text_events = get_events_for_component("Text")
        self.assertIn("onClick", text_events)
        
        input_events = get_events_for_component("TextInput")
        self.assertIn("onChange", input_events)
    
    def test_generate_random_events(self):
        """Test random event generation"""
        events = generate_random_events("Button", max_events=2)
        self.assertIsInstance(events, list)
        self.assertLessEqual(len(events), 2)
        
        if events:
            event_name, handler = events[0]
            self.assertIsInstance(event_name, str)
            self.assertIsInstance(handler, str)


class TestArkTSGenerator(unittest.TestCase):
    """Test ArkTS code generation"""
    
    def test_generator_creation(self):
        """Test generator instantiation"""
        generator = ArkTSGenerator()
        self.assertIsInstance(generator, ArkTSGenerator)
        self.assertEqual(len(generator.components), 0)
    
    def test_generate_application(self):
        """Test complete application generation"""
        code = generate_arkts_application()
        self.assertIsInstance(code, str)
        self.assertIn("@Entry", code)
        self.assertIn("@Component", code)
        self.assertIn("struct MainPage", code)
        self.assertIn("build()", code)
    
    def test_generated_code_structure(self):
        """Test that generated code has proper structure"""
        generator = ArkTSGenerator()
        code = generator.generate_application()
        
        # Check for basic structure
        self.assertIn("import", code)
        self.assertIn("@Entry", code)
        self.assertIn("@Component", code)
        self.assertIn("build()", code)


class TestArkTSDocument(unittest.TestCase):
    """Test ArkTS document functionality"""
    
    def test_document_creation(self):
        """Test document creation"""
        doc = ArkTSDocument()
        self.assertIsInstance(doc, ArkTSDocument)
        self.assertEqual(doc.content, "")
    
    def test_document_generation(self):
        """Test document generation"""
        doc = ArkTSDocument()
        doc.generate()
        
        self.assertNotEqual(doc.content, "")
        self.assertIsInstance(str(doc), str)


class TestArkTSFuzzer(unittest.TestCase):
    """Test ArkTS fuzzer integration"""
    
    def setUp(self):
        """Set up test environment"""
        self.test_dir = tempfile.mkdtemp()
        self.manager = Manager(1, True, self.test_dir, file_extension=".ets")
        self.fuzzer = Fuzzer(None, self.manager)
    
    def tearDown(self):
        """Clean up test environment"""
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
    
    def test_generate_arkts_one(self):
        """Test generating single ArkTS document"""
        document = self.fuzzer.generate_arkts_one()
        self.assertIsInstance(document, ArkTSDocument)
        self.assertNotEqual(str(document), "")
    
    def test_generate_arkts_only(self):
        """Test generating multiple ArkTS documents"""
        self.fuzzer.generate_arkts_only(2)
        
        # Check that files were created
        files = os.listdir(self.test_dir)
        ets_files = [f for f in files if f.endswith('.ets')]
        self.assertEqual(len(ets_files), 2)
    
    def test_generated_files_contain_valid_structure(self):
        """Test that generated files contain valid ArkTS structure"""
        self.fuzzer.generate_arkts_only(1)
        
        files = os.listdir(self.test_dir)
        ets_file = [f for f in files if f.endswith('.ets')][0]
        
        with open(os.path.join(self.test_dir, ets_file), 'r') as f:
            content = f.read()
        
        self.assertIn("@Entry", content)
        self.assertIn("@Component", content)
        self.assertIn("struct MainPage", content)


if __name__ == '__main__':
    unittest.main()