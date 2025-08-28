"""
ArkUI event handling templates for fuzzing
"""

from utils.random import Random


class EventTemplate:
    """Base event template class"""
    
    def __init__(self, name, handler_template):
        self.name = name
        self.handler_template = handler_template
    
    def generate_handler(self, function_name=None):
        """Generate an event handler function"""
        if function_name is None:
            function_name = f"handle{self.name.capitalize()}{Random.range(1, 100)}"
        
        return self.handler_template.format(function_name=function_name)


# Common UI events
COMMON_EVENTS = {
    "onClick": EventTemplate("onClick", 
        "() => {{\n    console.log('Click event triggered');\n    this.{function_name}();\n  }}"),
    "onTouch": EventTemplate("onTouch", 
        "(event: TouchEvent) => {{\n    console.log('Touch event:', event.type);\n  }}"),
    "onAppear": EventTemplate("onAppear", 
        "() => {{\n    console.log('Component appeared');\n  }}"),
    "onDisAppear": EventTemplate("onDisAppear",
        "() => {{\n    console.log('Component disappeared');\n  }}"),
    "onFocus": EventTemplate("onFocus",
        "() => {{\n    console.log('Component focused');\n  }}"),
    "onBlur": EventTemplate("onBlur",
        "() => {{\n    console.log('Component blurred');\n  }}"),
}

# Text input events
INPUT_EVENTS = {
    "onChange": EventTemplate("onChange",
        "(value: string) => {{\n    console.log('Input changed:', value);\n    this.inputValue = value;\n  }}"),
    "onSubmit": EventTemplate("onSubmit",
        "(value: string) => {{\n    console.log('Input submitted:', value);\n  }}"),
    "onEditChanged": EventTemplate("onEditChanged",
        "(isEditing: boolean) => {{\n    console.log('Edit state changed:', isEditing);\n  }}"),
    "onCopy": EventTemplate("onCopy",
        "(value: string) => {{\n    console.log('Text copied:', value);\n  }}"),
    "onCut": EventTemplate("onCut",
        "(value: string) => {{\n    console.log('Text cut:', value);\n  }}"),
    "onPaste": EventTemplate("onPaste",
        "(value: string) => {{\n    console.log('Text pasted:', value);\n  }}"),
}

# Gesture events
GESTURE_EVENTS = {
    "onPanGesture": EventTemplate("onPanGesture",
        "(event: PanGestureEvent) => {{\n    console.log('Pan gesture:', event.offsetX, event.offsetY);\n  }}"),
    "onPinchGesture": EventTemplate("onPinchGesture", 
        "(event: PinchGestureEvent) => {{\n    console.log('Pinch gesture:', event.scale);\n  }}"),
    "onRotationGesture": EventTemplate("onRotationGesture",
        "(event: RotationGestureEvent) => {{\n    console.log('Rotation gesture:', event.angle);\n  }}"),
    "onSwipeGesture": EventTemplate("onSwipeGesture",
        "(event: SwipeGestureEvent) => {{\n    console.log('Swipe gesture:', event.angle);\n  }}"),
    "onLongPressGesture": EventTemplate("onLongPressGesture",
        "(event: LongPressGestureEvent) => {{\n    console.log('Long press gesture');\n  }}"),
}

# List events
LIST_EVENTS = {
    "onItemDelete": EventTemplate("onItemDelete",
        "(index: number) => {{\n    console.log('Item deleted at index:', index);\n    return true;\n  }}"),
    "onItemMove": EventTemplate("onItemMove",
        "(from: number, to: number) => {{\n    console.log('Item moved from', from, 'to', to);\n    return true;\n  }}"),
    "onScrollIndex": EventTemplate("onScrollIndex",
        "(start: number, end: number) => {{\n    console.log('Scroll index changed:', start, end);\n  }}"),
    "onReachStart": EventTemplate("onReachStart",
        "() => {{\n    console.log('Reached start of list');\n  }}"),
    "onReachEnd": EventTemplate("onReachEnd",
        "() => {{\n    console.log('Reached end of list');\n  }}"),
}

# Tab events
TAB_EVENTS = {
    "onTabBarClick": EventTemplate("onTabBarClick",
        "(index: number) => {{\n    console.log('Tab clicked:', index);\n  }}"),
    "onAnimationStart": EventTemplate("onAnimationStart",
        "() => {{\n    console.log('Tab animation started');\n  }}"),
    "onAnimationEnd": EventTemplate("onAnimationEnd",
        "() => {{\n    console.log('Tab animation ended');\n  }}"),
    "onGestureSwipe": EventTemplate("onGestureSwipe",
        "(index: number, extraInfo: TabsAnimationEvent) => {{\n    console.log('Tab gesture swipe:', index);\n  }}"),
}

# Scroll events
SCROLL_EVENTS = {
    "onScroll": EventTemplate("onScroll",
        "(xOffset: number, yOffset: number) => {{\n    console.log('Scroll offset:', xOffset, yOffset);\n  }}"),
    "onScrollEdge": EventTemplate("onScrollEdge",
        "(side: Edge) => {{\n    console.log('Scroll reached edge:', side);\n  }}"),
    "onScrollEnd": EventTemplate("onScrollEnd",
        "() => {{\n    console.log('Scroll ended');\n  }}"),
    "onScrollStart": EventTemplate("onScrollStart",
        "() => {{\n    console.log('Scroll started');\n  }}"),
}


def get_events_for_component(component_name):
    """Get applicable events for a specific component"""
    events = dict(COMMON_EVENTS)
    
    if component_name in ["TextInput", "TextArea"]:
        events.update(INPUT_EVENTS)
    elif component_name == "List":
        events.update(LIST_EVENTS)
    elif component_name in ["Tabs", "TabContent"]:
        events.update(TAB_EVENTS)
    elif component_name == "ScrollArea":
        events.update(SCROLL_EVENTS)
    
    # All components can have gesture events
    if Random.bool():
        events.update(GESTURE_EVENTS)
    
    return events


def generate_random_events(component_name, max_events=3):
    """Generate random events for a component"""
    available_events = get_events_for_component(component_name)
    num_events = Random.range(0, min(max_events, len(available_events)))
    
    if num_events == 0:
        return []
    
    selected_events = Random.sample(list(available_events.keys()), num_events)
    events = []
    
    for event_name in selected_events:
        template = available_events[event_name]
        handler = template.generate_handler()
        events.append((event_name, handler))
    
    return events


def generate_state_management_functions():
    """Generate random state management functions"""
    functions = []
    
    # State variables
    state_vars = []
    for i in range(Random.range(1, 5)):
        var_name = f"state{Random.choice(['Value', 'Flag', 'Count', 'Text'])}{i}"
        var_type = Random.choice(["string", "number", "boolean"])
        default_value = get_default_value(var_type)
        state_vars.append(f"@State {var_name}: {var_type} = {default_value};")
    
    # Functions that modify state
    for i in range(Random.range(1, 3)):
        func_name = f"updateState{i}"
        func_body = generate_state_update_function(state_vars)
        functions.append(f"  {func_name}() {{\n{func_body}\n  }}")
    
    return state_vars, functions


def get_default_value(var_type):
    """Get default value for a type"""
    if var_type == "string":
        return f'"{Random.string()}"'
    elif var_type == "number":
        return str(Random.range(0, 100))
    elif var_type == "boolean":
        return Random.choice(["true", "false"])
    else:
        return '""'


def generate_state_update_function(state_vars):
    """Generate function body that updates state"""
    if not state_vars:
        return "    console.log('No state to update');"
    
    var_name = Random.choice(state_vars).split()[1].rstrip(':')
    operations = [
        f"    this.{var_name} = !this.{var_name};",
        f"    this.{var_name} = this.{var_name} + 1;",
        f"    this.{var_name} = '{Random.string()}';",
        f"    console.log('Updated {var_name}:', this.{var_name});",
    ]
    
    return Random.choice(operations)