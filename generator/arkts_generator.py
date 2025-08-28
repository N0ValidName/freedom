"""
Main ArkTS code generator for OpenHarmony applications
"""

from config import ArkTSConfig
from arkui.components import create_component, get_random_component, CONTAINER_COMPONENTS
from arkui.properties import generate_random_properties
from arkui.events import generate_random_events
from generator.state_manager import generate_state_management
from generator.api_generator import generate_system_apis
from utils.random import Random


class ArkTSGenerator:
    """Main generator for ArkTS application code"""
    
    def __init__(self):
        self.components = []
        self.state_variables = []
        self.functions = []
        self.imports = set()
        self.component_tree = None
        self.api_imports = []
        
    def generate_application(self):
        """Generate a complete ArkTS application"""
        self.reset()
        self.generate_component_tree()
        self.generate_state_and_api_management()
        return self.build_application_code()
    
    def reset(self):
        """Reset generator state"""
        self.components = []
        self.state_variables = []
        self.functions = []
        self.imports = set()
        self.component_tree = None
        self.api_imports = []
    
    def generate_component_tree(self):
        """Generate a tree of ArkUI components"""
        # Create root component
        root_name = Random.choice(["Column", "Row", "Stack"])
        self.component_tree = create_component(root_name)
        
        # Generate component hierarchy
        self.generate_component_hierarchy(self.component_tree, 0)
        
    def generate_component_hierarchy(self, parent, depth):
        """Recursively generate component hierarchy"""
        if depth >= ArkTSConfig.max_component_depth:
            return
        
        # Generate child components
        num_children = Random.range(0, 4) if depth < 2 else Random.range(0, 2)
        
        for _ in range(num_children):
            # Choose component type based on depth
            if depth < ArkTSConfig.max_component_depth - 1 and Random.bool():
                # Container component
                child_name = get_random_component("container")
            else:
                # Leaf component
                child_name = Random.choice([
                    get_random_component("basic"),
                    get_random_component("media"),
                    get_random_component("drawing")
                ])
            
            child = create_component(child_name)
            
            # Generate properties
            child.properties = generate_random_properties(
                child_name, ArkTSConfig.max_property_count
            )
            
            # Generate events
            child.events = generate_random_events(
                child_name, ArkTSConfig.max_event_handler_count
            )
            
            # Add to parent
            if parent.add_child(child):
                # Recursively generate children for container components
                if child.can_have_children():
                    self.generate_component_hierarchy(child, depth + 1)
    
    def generate_state_and_api_management(self):
        """Generate state variables, management functions, and API calls"""
        # Generate state management
        self.state_variables, state_functions = generate_state_management()
        
        # Generate system API calls
        api_imports, api_functions = generate_system_apis()
        self.api_imports = api_imports
        
        # Combine all functions
        self.functions = state_functions + api_functions
    
    def build_application_code(self):
        """Build the complete ArkTS application code"""
        code_parts = []
        
        # Imports
        code_parts.append(self.generate_imports())
        
        # Page decorator and class
        code_parts.append("@Entry")
        code_parts.append("@Component")
        code_parts.append("struct MainPage {")
        
        # State variables
        if self.state_variables:
            for state_var in self.state_variables:
                code_parts.append(f"  {state_var}")
            code_parts.append("")
        
        # Build method
        code_parts.append("  build() {")
        code_parts.append(self.generate_component_code(self.component_tree, 2))
        code_parts.append("  }")
        
        # Helper functions
        if self.functions:
            code_parts.append("")
            for func in self.functions:
                code_parts.append(func)
        
        code_parts.append("}")
        
        return "\n".join(code_parts)
    
    def generate_imports(self):
        """Generate import statements"""
        default_imports = [
            "import { CommonConstants } from '../common/constants/CommonConstants';",
            "import Logger from '../common/utils/Logger';",
        ]
        
        # Add API imports
        all_imports = default_imports + self.api_imports
        all_imports.append("")
        
        return "\n".join(all_imports)
    
    def generate_component_code(self, component, indent_level):
        """Generate code for a component and its children"""
        indent = "  " * indent_level
        lines = []
        
        # Component opening
        if component.name in ["Text", "Button"] and not component.children:
            # Text components need content
            content = f'"{Random.string()}"' if component.name == "Text" else f'"{Random.choice(["Click", "Submit", "Cancel", "OK"])}"'
            lines.append(f"{indent}{component.name}({content})")
        else:
            lines.append(f"{indent}{component.name}() {{")
        
        # Add children for container components
        if component.children:
            for child in component.children:
                lines.append(self.generate_component_code(child, indent_level + 1))
        
        # Close container if it has children
        if component.children:
            lines.append(f"{indent}}}")
        
        # Add properties
        property_lines = self.generate_property_code(component.properties, indent_level)
        if property_lines:
            if component.children:
                # Properties go after the closing brace
                lines.extend(property_lines)
            else:
                # Properties go directly after the component
                lines.extend(property_lines)
        
        # Add events
        event_lines = self.generate_event_code(component.events, indent_level)
        if event_lines:
            lines.extend(event_lines)
        
        return "\n".join(lines)
    
    def generate_property_code(self, properties, indent_level):
        """Generate property code"""
        if not properties:
            return []
        
        indent = "  " * indent_level
        lines = []
        
        for prop_name, prop_value in properties.items():
            lines.append(f"{indent}.{prop_name}({prop_value})")
        
        return lines
    
    def generate_event_code(self, events, indent_level):
        """Generate event handler code"""
        if not events:
            return []
        
        indent = "  " * indent_level
        lines = []
        
        for event_name, handler in events:
            lines.append(f"{indent}.{event_name}({handler})")
        
        return lines


def generate_arkts_application():
    """Generate a complete ArkTS application"""
    generator = ArkTSGenerator()
    return generator.generate_application()