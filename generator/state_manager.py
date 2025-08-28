"""
State management code generation for ArkTS applications
"""

from utils.random import Random


class StateVariable:
    """Represents a state variable in ArkTS"""
    
    def __init__(self, name, var_type, default_value):
        self.name = name
        self.var_type = var_type
        self.default_value = default_value
    
    def to_declaration(self):
        """Generate state variable declaration"""
        return f"@State {self.name}: {self.var_type} = {self.default_value};"


class StateManager:
    """Manages state variables and related functions"""
    
    def __init__(self):
        self.variables = []
        self.functions = []
        self.observers = []
    
    def generate_state_variables(self, count=None):
        """Generate random state variables"""
        if count is None:
            count = Random.range(1, 6)
        
        variable_names = [
            "userName", "userAge", "isLoggedIn", "itemCount", "selectedIndex",
            "loadingState", "errorMessage", "dataList", "currentPage", "totalPages"
        ]
        
        for i in range(count):
            name_suffix = Random.choice(["", "0", "1", "2"])
            var_name = Random.choice(variable_names) + name_suffix
            var_type = Random.choice(["string", "number", "boolean"])
            default_value = self.get_default_value(var_type)
            
            state_var = StateVariable(var_name, var_type, default_value)
            self.variables.append(state_var)
    
    def get_default_value(self, var_type):
        """Get appropriate default value for type"""
        if var_type == "string":
            values = ['"Sample Text"', '"Hello World"', '""', '"Item"']
            return Random.choice(values)
        elif var_type == "number":
            return str(Random.range(0, 100))
        elif var_type == "boolean":
            return Random.choice(["true", "false"])
        else:
            return '""'
    
    def generate_state_functions(self):
        """Generate functions that manipulate state"""
        if not self.variables:
            return
        
        function_count = Random.range(1, min(4, len(self.variables) + 1))
        
        for i in range(function_count):
            func_name = f"updateState{i}"
            func_body = self.generate_function_body()
            function_code = f"  {func_name}() {{\n{func_body}\n  }}"
            self.functions.append(function_code)
    
    def generate_function_body(self):
        """Generate function body that modifies state"""
        if not self.variables:
            return "    console.log('No state to update');"
        
        operations = []
        num_operations = Random.range(1, 3)
        
        for _ in range(num_operations):
            var = Random.choice(self.variables)
            
            if var.var_type == "boolean":
                operations.append(f"    this.{var.name} = !this.{var.name};")
            elif var.var_type == "number":
                op = Random.choice(["+", "-", "*"])
                value = Random.range(1, 10)
                operations.append(f"    this.{var.name} = this.{var.name} {op} {value};")
            elif var.var_type == "string":
                new_value = Random.choice(['"Updated"', '"New Value"', '"Modified"'])
                operations.append(f"    this.{var.name} = {new_value};")
            
            # Add console log
            operations.append(f"    console.log('Updated {var.name}:', this.{var.name});")
        
        return "\n".join(operations)
    
    def generate_watch_functions(self):
        """Generate @Watch functions for state variables"""
        if not self.variables:
            return
        
        watch_count = Random.range(0, min(2, len(self.variables)))
        
        for i in range(watch_count):
            var = Random.choice(self.variables)
            watch_func = f"""  @Watch('onWatch{var.name}')
  on{var.name}Changed(propName: string) {{
    console.log(`Property ${{propName}} changed to: ${{this.{var.name}}}`);
  }}"""
            self.observers.append(watch_func)
    
    def get_all_declarations(self):
        """Get all state variable declarations"""
        return [var.to_declaration() for var in self.variables]
    
    def get_all_functions(self):
        """Get all generated functions"""
        return self.functions + self.observers


def generate_state_management():
    """Generate complete state management code"""
    manager = StateManager()
    manager.generate_state_variables()
    manager.generate_state_functions()
    manager.generate_watch_functions()
    
    return manager.get_all_declarations(), manager.get_all_functions()