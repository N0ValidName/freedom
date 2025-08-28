"""
ArkUI component property templates for fuzzing
"""

from utils.random import Random


class PropertyTemplate:
    """Base property template class"""
    
    def __init__(self, name, value_type, possible_values=None):
        self.name = name
        self.value_type = value_type  # "string", "number", "boolean", "resource", "color"
        self.possible_values = possible_values or []
    
    def generate_value(self):
        """Generate a random value for this property"""
        if self.possible_values:
            return Random.choice(self.possible_values)
        
        if self.value_type == "string":
            return f'"{Random.string()}"'
        elif self.value_type == "number":
            return str(Random.range(1, 100))
        elif self.value_type == "boolean":
            return Random.choice(["true", "false"])
        elif self.value_type == "color":
            return f'"#{Random.hex_digits(6)}"'
        elif self.value_type == "resource":
            return f'$r("app.{Random.choice(["string", "color", "media"])}.{Random.string()}")'
        else:
            return '""'


# Common properties for all components
COMMON_PROPERTIES = {
    "width": PropertyTemplate("width", "number", ["100", "200", "300", "'100%'", "'50vp'"]),
    "height": PropertyTemplate("height", "number", ["100", "200", "300", "'100%'", "'50vp'"]),
    "margin": PropertyTemplate("margin", "number", ["10", "20", "{top: 10, bottom: 20}"]),
    "padding": PropertyTemplate("padding", "number", ["10", "20", "{left: 5, right: 15}"]),
    "backgroundColor": PropertyTemplate("backgroundColor", "color"),
    "borderRadius": PropertyTemplate("borderRadius", "number", ["5", "10", "15"]),
    "opacity": PropertyTemplate("opacity", "number", ["0.5", "0.8", "1.0"]),
    "visibility": PropertyTemplate("visibility", "string", ["Visibility.Visible", "Visibility.Hidden"]),
    "enabled": PropertyTemplate("enabled", "boolean"),
    "id": PropertyTemplate("id", "string"),
}

# Container-specific properties
CONTAINER_PROPERTIES = {
    "justifyContent": PropertyTemplate("justifyContent", "string", 
        ["FlexAlign.Start", "FlexAlign.Center", "FlexAlign.End", "FlexAlign.SpaceBetween"]),
    "alignItems": PropertyTemplate("alignItems", "string",
        ["HorizontalAlign.Start", "HorizontalAlign.Center", "HorizontalAlign.End"]),
    "direction": PropertyTemplate("direction", "string", 
        ["Direction.Ltr", "Direction.Rtl"]),
    "wrap": PropertyTemplate("wrap", "string", 
        ["FlexWrap.NoWrap", "FlexWrap.Wrap", "FlexWrap.WrapReverse"]),
}

# Text-specific properties
TEXT_PROPERTIES = {
    "fontSize": PropertyTemplate("fontSize", "number", ["12", "16", "20", "24"]),
    "fontColor": PropertyTemplate("fontColor", "color"),
    "fontWeight": PropertyTemplate("fontWeight", "string", 
        ["FontWeight.Normal", "FontWeight.Bold", "FontWeight.Lighter"]),
    "textAlign": PropertyTemplate("textAlign", "string",
        ["TextAlign.Start", "TextAlign.Center", "TextAlign.End"]),
    "maxLines": PropertyTemplate("maxLines", "number", ["1", "2", "3"]),
    "textOverflow": PropertyTemplate("textOverflow", "string",
        ["TextOverflow.Clip", "TextOverflow.Ellipsis", "TextOverflow.None"]),
}

# Button-specific properties  
BUTTON_PROPERTIES = {
    "type": PropertyTemplate("type", "string", 
        ["ButtonType.Capsule", "ButtonType.Circle", "ButtonType.Normal"]),
    "stateEffect": PropertyTemplate("stateEffect", "boolean"),
}

# Image-specific properties
IMAGE_PROPERTIES = {
    "objectFit": PropertyTemplate("objectFit", "string",
        ["ImageFit.Cover", "ImageFit.Contain", "ImageFit.Fill", "ImageFit.ScaleDown"]),
    "alt": PropertyTemplate("alt", "string"),
    "interpolation": PropertyTemplate("interpolation", "string",
        ["ImageInterpolation.None", "ImageInterpolation.High", "ImageInterpolation.Medium"]),
}

# Input-specific properties
INPUT_PROPERTIES = {
    "placeholder": PropertyTemplate("placeholder", "string"),
    "type": PropertyTemplate("type", "string", 
        ["InputType.Normal", "InputType.Password", "InputType.Email", "InputType.Number"]),
    "maxLength": PropertyTemplate("maxLength", "number", ["10", "50", "100"]),
    "enterKeyType": PropertyTemplate("enterKeyType", "string",
        ["EnterKeyType.Go", "EnterKeyType.Search", "EnterKeyType.Send", "EnterKeyType.Done"]),
}

# List-specific properties
LIST_PROPERTIES = {
    "space": PropertyTemplate("space", "number", ["10", "20", "30"]),
    "initialIndex": PropertyTemplate("initialIndex", "number", ["0", "1", "2"]),
    "listDirection": PropertyTemplate("listDirection", "string",
        ["Axis.Vertical", "Axis.Horizontal"]),
}

# Grid-specific properties
GRID_PROPERTIES = {
    "columnsTemplate": PropertyTemplate("columnsTemplate", "string", 
        ["'1fr 1fr'", "'1fr 2fr 1fr'", "'repeat(3, 1fr)'"]),
    "rowsTemplate": PropertyTemplate("rowsTemplate", "string",
        ["'1fr 1fr'", "'auto 1fr auto'", "'repeat(2, 1fr)'"]),
    "columnsGap": PropertyTemplate("columnsGap", "number", ["10", "20", "30"]),
    "rowsGap": PropertyTemplate("rowsGap", "number", ["10", "20", "30"]),
}


def get_properties_for_component(component_name):
    """Get applicable properties for a specific component"""
    properties = dict(COMMON_PROPERTIES)
    
    component_lower = component_name.lower()
    
    if component_name in ["Column", "Row", "Flex", "Stack"]:
        properties.update(CONTAINER_PROPERTIES)
    
    if component_name == "Text":
        properties.update(TEXT_PROPERTIES)
    elif component_name == "Button":
        properties.update(BUTTON_PROPERTIES)
    elif component_name == "Image":
        properties.update(IMAGE_PROPERTIES)
    elif component_name in ["TextInput", "TextArea"]:
        properties.update(INPUT_PROPERTIES)
    elif component_name == "List":
        properties.update(LIST_PROPERTIES)
    elif component_name == "Grid":
        properties.update(GRID_PROPERTIES)
    
    return properties


def generate_random_properties(component_name, max_properties=5):
    """Generate random properties for a component"""
    available_props = get_properties_for_component(component_name)
    num_props = Random.range(1, min(max_properties, len(available_props)))
    
    selected_props = Random.sample(list(available_props.keys()), num_props)
    properties = {}
    
    for prop_name in selected_props:
        template = available_props[prop_name]
        properties[prop_name] = template.generate_value()
    
    return properties