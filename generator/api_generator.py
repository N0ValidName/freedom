"""
System API call generation for OpenHarmony ArkTS applications
"""

from utils.random import Random


class APICall:
    """Represents an OpenHarmony system API call"""
    
    def __init__(self, api_name, module, parameters=None):
        self.api_name = api_name
        self.module = module
        self.parameters = parameters or []
    
    def generate_call(self):
        """Generate the API call code"""
        params = ", ".join(self.parameters) if self.parameters else ""
        return f"{self.module}.{self.api_name}({params})"


class APIGenerator:
    """Generates OpenHarmony system API calls"""
    
    def __init__(self):
        self.api_calls = []
        self.imports = set()
    
    def generate_apis(self, count=None):
        """Generate random system API calls"""
        if count is None:
            count = Random.range(1, 8)
        
        for _ in range(count):
            api_category = Random.choice([
                "ui", "data", "media", "network", "device", "security"
            ])
            
            if api_category == "ui":
                self.generate_ui_api()
            elif api_category == "data":
                self.generate_data_api()
            elif api_category == "media":
                self.generate_media_api()
            elif api_category == "network":
                self.generate_network_api()
            elif api_category == "device":
                self.generate_device_api()
            elif api_category == "security":
                self.generate_security_api()
    
    def generate_ui_api(self):
        """Generate UI-related API calls"""
        ui_apis = [
            ("showToast", "promptAction", [f'{{message: "{Random.string()}", duration: 2000}}']),
            ("showDialog", "promptAction", [f'{{title: "{Random.string()}", message: "{Random.string()}"}}']),
            ("openLink", "common", [f'"{Random.string()}.html"']),
            ("getWindowProperties", "window", []),
            ("setStatusBarColor", "window", [f'"#{Random.hex_digits(6)}"']),
        ]
        
        api_name, module, params = Random.choice(ui_apis)
        api_call = APICall(api_name, module, params)
        self.api_calls.append(api_call)
        
        if module == "promptAction":
            self.imports.add("import promptAction from '@ohos.promptAction';")
        elif module == "window":
            self.imports.add("import window from '@ohos.window';")
    
    def generate_data_api(self):
        """Generate data storage API calls"""
        data_apis = [
            ("setItem", "preferences", [f'"{Random.string()}"', f'"{Random.string()}"']),
            ("getItem", "preferences", [f'"{Random.string()}"']),
            ("removeItem", "preferences", [f'"{Random.string()}"']),
            ("query", "dataAbility", [f'"{Random.string()}"']),
            ("insert", "dataAbility", [f'{{name: "{Random.string()}", value: {Random.range(1, 100)}}}']),
        ]
        
        api_name, module, params = Random.choice(data_apis)
        api_call = APICall(api_name, module, params)
        self.api_calls.append(api_call)
        
        if module == "preferences":
            self.imports.add("import dataPreferences from '@ohos.data.preferences';")
        elif module == "dataAbility":
            self.imports.add("import dataAbility from '@ohos.data.dataAbility';")
    
    def generate_media_api(self):
        """Generate media-related API calls"""
        media_apis = [
            ("createAudioPlayer", "media", []),
            ("play", "audioPlayer", []),
            ("pause", "audioPlayer", []),
            ("createVideoPlayer", "media", []),
            ("setDisplaySurface", "videoPlayer", [f'"{Random.string()}"']),
            ("takePicture", "camera", []),
        ]
        
        api_name, module, params = Random.choice(media_apis)
        api_call = APICall(api_name, module, params)
        self.api_calls.append(api_call)
        
        if module in ["media", "audioPlayer", "videoPlayer"]:
            self.imports.add("import media from '@ohos.multimedia.media';")
        elif module == "camera":
            self.imports.add("import camera from '@ohos.multimedia.camera';")
    
    def generate_network_api(self):
        """Generate network API calls"""
        network_apis = [
            ("request", "http", [f'{{url: "https://example.com/{Random.string()}", method: "GET"}}']),
            ("createWebSocket", "webSocket", [f'"ws://example.com/{Random.string()}"']),
            ("send", "webSocket", [f'"{Random.string()}"']),
            ("download", "request", [f'{{url: "https://example.com/file.{Random.choice(["jpg", "png", "mp4"])}""}}']),
        ]
        
        api_name, module, params = Random.choice(network_apis)
        api_call = APICall(api_name, module, params)
        self.api_calls.append(api_call)
        
        if module == "http":
            self.imports.add("import http from '@ohos.net.http';")
        elif module == "webSocket":
            self.imports.add("import webSocket from '@ohos.net.webSocket';")
        elif module == "request":
            self.imports.add("import request from '@ohos.request';")
    
    def generate_device_api(self):
        """Generate device-related API calls"""
        device_apis = [
            ("getDeviceInfo", "deviceInfo", []),
            ("getBatteryStats", "batteryStats", []),
            ("vibrate", "vibrator", [str(Random.range(100, 1000))]),
            ("getLocation", "geoLocationManager", []),
            ("startLocationUpdates", "geoLocationManager", []),
        ]
        
        api_name, module, params = Random.choice(device_apis)
        api_call = APICall(api_name, module, params)
        self.api_calls.append(api_call)
        
        if module == "deviceInfo":
            self.imports.add("import deviceInfo from '@ohos.deviceInfo';")
        elif module == "batteryStats":
            self.imports.add("import batteryStats from '@ohos.batteryStats';")
        elif module == "vibrator":
            self.imports.add("import vibrator from '@ohos.vibrator';")
        elif module == "geoLocationManager":
            self.imports.add("import geoLocationManager from '@ohos.geoLocationManager';")
    
    def generate_security_api(self):
        """Generate security-related API calls"""
        security_apis = [
            ("checkPermission", "abilityAccessCtrl", [f'"{Random.choice(["ohos.permission.CAMERA", "ohos.permission.MICROPHONE", "ohos.permission.LOCATION"])}"']),
            ("requestPermissions", "abilityAccessCtrl", [f'["{Random.choice(["ohos.permission.READ_MEDIA", "ohos.permission.WRITE_MEDIA"])}"]']),
            ("encrypt", "cryptoFramework", [f'"{Random.string()}"']),
            ("decrypt", "cryptoFramework", [f'"{Random.string()}"']),
        ]
        
        api_name, module, params = Random.choice(security_apis)
        api_call = APICall(api_name, module, params)
        self.api_calls.append(api_call)
        
        if module == "abilityAccessCtrl":
            self.imports.add("import abilityAccessCtrl from '@ohos.abilityAccessCtrl';")
        elif module == "cryptoFramework":
            self.imports.add("import cryptoFramework from '@ohos.security.cryptoFramework';")
    
    def generate_api_functions(self):
        """Generate functions that call system APIs"""
        if not self.api_calls:
            return []
        
        functions = []
        function_count = Random.range(1, min(4, len(self.api_calls) + 1))
        
        for i in range(function_count):
            func_name = f"callSystemAPI{i}"
            api_calls_subset = Random.sample(self.api_calls, Random.range(1, min(3, len(self.api_calls) + 1)))
            
            func_body = []
            func_body.append("    try {")
            
            for api_call in api_calls_subset:
                call_code = api_call.generate_call()
                if api_call.api_name in ["getDeviceInfo", "getLocation", "getItem"]:
                    func_body.append(f"      const result = await {call_code};")
                    func_body.append(f"      console.log('API result:', result);")
                else:
                    func_body.append(f"      await {call_code};")
                    func_body.append(f"      console.log('API call successful: {api_call.api_name}');")
            
            func_body.append("    } catch (error) {")
            func_body.append(f"      console.error('API call failed:', error);")
            func_body.append("    }")
            
            function_code = f"  async {func_name}() {{\n" + "\n".join(func_body) + "\n  }"
            functions.append(function_code)
        
        return functions
    
    def get_imports(self):
        """Get all required imports"""
        return list(self.imports)
    
    def get_api_calls(self):
        """Get all generated API calls"""
        return self.api_calls


def generate_system_apis():
    """Generate system API calls and related functions"""
    generator = APIGenerator()
    generator.generate_apis()
    functions = generator.generate_api_functions()
    imports = generator.get_imports()
    
    return imports, functions