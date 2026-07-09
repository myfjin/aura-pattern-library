# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import re
from typing import Dict, List, Optional, Tuple, Any, Callable, Union
from dataclasses import dataclass


@dataclass
class Route:
    """Represents a single route with pattern, handler and name."""
    pattern: str
    handler: Callable
    name: Optional[str] = None
    _compiled_pattern: re.Pattern = None
    _param_names: List[str] = None

    def __post_init__(self):
        """Compile the pattern and extract parameter names."""
        # Convert pattern to regex and extract parameter names
        param_names = []
        regex_pattern = self.pattern
        
        # Find all parameters in the pattern like {id} or {name}
        param_matches = re.findall(r'\{([^}]+)\}', self.pattern)
        for param in param_matches:
            param_names.append(param)
            # Replace {param} with a regex group that matches anything except '/'
            regex_pattern = regex_pattern.replace(f'{{{param}}}', r'([^/]+)')
        
        # Ensure pattern matches the entire path
        regex_pattern = f'^{regex_pattern}$'
        self._compiled_pattern = re.compile(regex_pattern)
        self._param_names = param_names


class URLRouter:
    """Simple URL router that supports parameters and reverse URL building."""
    
    def __init__(self):
        self.routes: List[Route] = []
        self.named_routes: Dict[str, Route] = {}
    
    def add_route(self, pattern: str, handler: Callable, name: Optional[str] = None) -> None:
        """Add a route to the router.
        
        Args:
            pattern: URL pattern with optional parameters in curly braces
            handler: Function to call when route matches
            name: Optional name for reverse URL lookup
        """
        route = Route(pattern, handler, name)
        self.routes.append(route)
        if name:
            self.named_routes[name] = route
    
    def route(self, pattern: str, name: Optional[str] = None) -> Callable:
        """Decorator for adding routes.
        
        Args:
            pattern: URL pattern with optional parameters in curly braces
            name: Optional name for reverse URL lookup
        """
        def decorator(handler: Callable) -> Callable:
            self.add_route(pattern, handler, name)
            return handler
        return decorator
    
    def match(self, path: str) -> Tuple[Optional[Callable], Dict[str, str]]:
        """Match a path against registered routes.
        
        Args:
            path: The URL path to match
            
        Returns:
            Tuple of (handler, parameters) or (None, {}) if no match
        """
        path = path.rstrip('/') or '/'
        
        for route in self.routes:
            match = route._compiled_pattern.match(path)
            if match:
                # Extract parameters
                params = {}
                if route._param_names:
                    for i, param_name in enumerate(route._param_names):
                        params[param_name] = match.group(i + 1)
                return route.handler, params
        
        return None, {}
    
    def build_url(self, name: str, **kwargs) -> Optional[str]:
        """Build a URL from a named route.
        
        Args:
            name: Name of the route
            **kwargs: Parameters to substitute in the pattern
            
        Returns:
            URL string or None if route not found
        """
        if name not in self.named_routes:
            return None
            
        route = self.named_routes[name]
        url = route.pattern
        
        # Replace parameters with provided values
        for param_name, value in kwargs.items():
            url = url.replace(f'{{{param_name}}}', str(value))
            
        return url


# Demo application
def demo():
    """Demonstrate URL router functionality."""
    router = URLRouter()
    
    # Define handlers
    def home_handler():
        return "Welcome to the home page!"
    
    def user_handler(user_id: str):
        return f"User profile for user {user_id}"
    
    def post_handler(user_id: str, post_id: str):
        return f"Post {post_id} by user {user_id}"
    
    def search_handler(query: str, page: str = "1"):
        return f"Search results for '{query}' (page {page})"
    
    # Add routes using method
    router.add_route("/", home_handler, "home")
    router.add_route("/user/{user_id}", user_handler, "user_profile")
    router.add_route("/user/{user_id}/post/{post_id}", post_handler, "user_post")
    
    # Add route using decorator
    @router.route("/search/{query}", "search")
    def search_handler_decorated(query: str, page: str = "1"):
        return f"Search results for '{query}' (page {page})"
    
    # Test matching
    test_paths = [
        "/",
        "/user/123",
        "/user/456/post/789",
        "/search/python",
        "/search/python?page=2",
        "/nonexistent"
    ]
    
    print("URL Matching Tests:")
    print("-" * 40)
    for path in test_paths:
        handler, params = router.match(path)
        if handler:
            result = handler(**params)
            print(f"Path: {path}")
            print(f"  Handler: {handler.__name__}")
            print(f"  Params: {params}")
            print(f"  Result: {result}")
        else:
            print(f"Path: {path}")
            print(f"  No match found")
        print()
    
    # Test reverse URL building
    print("Reverse URL Building Tests:")
    print("-" * 40)
    build_tests = [
        ("home", {}),
        ("user_profile", {"user_id": "123"}),
        ("user_post", {"user_id": "456", "post_id": "789"}),
        ("search", {"query": "python"}),
        ("nonexistent", {})
    ]
    
    for name, params in build_tests:
        url = router.build_url(name, **params)
        if url:
            print(f"Route '{name}' with {params} -> {url}")
        else:
            print(f"Route '{name}' not found")
    
    # Verify round-trip consistency
    print("\nRound-trip Consistency Test:")
    print("-" * 40)
    test_routes = [
        ("user_profile", {"user_id": "abc"}),
        ("user_post", {"user_id": "def", "post_id": "456"})
    ]
    
    for name, params in test_routes:
        # Build URL
        url = router.build_url(name, **params)
        if url:
            # Match it back
            handler, matched_params = router.match(url)
            if handler and handler.__name__ == router.named_routes[name].handler.__name__:
                match_success = matched_params == params
                print(f"Route '{name}': {match_success} - {url} -> {matched_params}")
            else:
                print(f"Route '{name}': False - Handler mismatch")
        else:
            print(f"Route '{name}': False - URL building failed")


if __name__ == "__main__":
    demo()