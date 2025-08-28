"""
ArkUI component definitions and hierarchy for fuzzing
"""

from utils.random import Random


class ArkUIComponent:
    """Base class for ArkUI components"""
    
    def __init__(self, name, component_type="container"):
        self.name = name
        self.component_type = component_type  # container, basic, media
        self.children = []
        self.parent = None
        self.properties = {}
        self.events = []
        
    def add_child(self, child):
        """Add a child component"""
        if self.can_have_children():
            child.parent = self
            self.children.append(child)
            return True
        return False
    
    def can_have_children(self):
        """Check if this component can have children"""
        return self.component_type == "container"
    
    def set_property(self, name, value):
        """Set a property for this component"""
        self.properties[name] = value
    
    def add_event(self, event_name, handler):
        """Add an event handler"""
        self.events.append((event_name, handler))


# Container Components
CONTAINER_COMPONENTS = [
    "Column", "Row", "Stack", "Flex", "Grid", "List", "Swiper", 
    "Tabs", "TabContent", "ScrollArea", "RelativeContainer"
]

# Basic Components  
BASIC_COMPONENTS = [
    "Text", "Button", "TextInput", "Image", "Progress", "Slider",
    "Switch", "Radio", "Checkbox", "Rating", "Toggle", "LoadingProgress"
]

# Media Components
MEDIA_COMPONENTS = [
    "Video", "Camera", "Audio", "Lottie", "Canvas", "Web"
]

# Drawing Components
DRAWING_COMPONENTS = [
    "Shape", "Circle", "Ellipse", "Line", "Polyline", "Polygon", 
    "Path", "Rect"
]

ALL_COMPONENTS = CONTAINER_COMPONENTS + BASIC_COMPONENTS + MEDIA_COMPONENTS + DRAWING_COMPONENTS


def get_random_component(component_type=None):
    """Get a random ArkUI component"""
    if component_type == "container":
        return Random.choice(CONTAINER_COMPONENTS)
    elif component_type == "basic":
        return Random.choice(BASIC_COMPONENTS)
    elif component_type == "media":
        return Random.choice(MEDIA_COMPONENTS)
    elif component_type == "drawing":
        return Random.choice(DRAWING_COMPONENTS)
    else:
        return Random.choice(ALL_COMPONENTS)


def create_component(name=None):
    """Create a new ArkUI component instance"""
    if name is None:
        name = get_random_component()
    
    if name in CONTAINER_COMPONENTS:
        component_type = "container"
    elif name in BASIC_COMPONENTS:
        component_type = "basic"
    elif name in MEDIA_COMPONENTS:
        component_type = "media"
    else:
        component_type = "drawing"
    
    return ArkUIComponent(name, component_type)


def get_component_hierarchy():
    """Get component hierarchy rules"""
    return {
        "root_components": ["Column", "Row", "Stack", "Flex"],
        "container_components": CONTAINER_COMPONENTS,
        "leaf_components": BASIC_COMPONENTS + MEDIA_COMPONENTS + DRAWING_COMPONENTS
    }