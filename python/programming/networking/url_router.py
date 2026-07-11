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


def demo():
    """Self-test: exact param extraction, no-match honesty, reverse URL
    building, and build→match round-trip identity."""
    router = URLRouter()

    router.add_route("/", lambda: "home", "home")
    router.add_route("/user/{user_id}", lambda user_id: f"user {user_id}", "user_profile")
    router.add_route("/user/{user_id}/post/{post_id}",
                     lambda user_id, post_id: f"post {post_id} by {user_id}", "user_post")

    @router.route("/search/{query}", "search")
    def search_handler(query: str):
        return f"results for {query}"

    # Exact matching and param extraction.
    handler, params = router.match("/")
    assert handler is not None and params == {} and handler() == "home"

    handler, params = router.match("/user/123")
    assert params == {"user_id": "123"}, f"single param wrong: {params}"
    assert handler(**params) == "user 123"

    handler, params = router.match("/user/456/post/789")
    assert params == {"user_id": "456", "post_id": "789"}, f"two params wrong: {params}"
    assert handler(**params) == "post 789 by 456"
    assert int(params["user_id"]) + int(params["post_id"]) == 1245, \
        "456 + 789 must be 1245"

    # Decorator-registered route works identically.
    handler, params = router.match("/search/python")
    assert params == {"query": "python"} and handler(**params) == "results for python"

    # No-match honesty: unknown paths, partial paths, over-long paths.
    for miss in ("/nonexistent", "/user", "/user/1/post", "/user/1/post/2/extra"):
        handler, params = router.match(miss)
        assert handler is None, f"path {miss!r} matched a route"

    # Reverse building is exact.
    assert router.build_url("home") == "/"
    assert router.build_url("user_profile", user_id="123") == "/user/123"
    assert router.build_url("user_post", user_id="456", post_id="789") == \
        "/user/456/post/789"
    assert router.build_url("nonexistent") is None

    # ROUND-TRIP: build → match must return the same params.
    for name, kwargs in (("user_profile", {"user_id": "abc"}),
                         ("user_post", {"user_id": "def", "post_id": "456"}),
                         ("search", {"query": "rust"})):
        url = router.build_url(name, **kwargs)
        handler, matched = router.match(url)
        assert handler is not None, f"built URL {url!r} does not match its own route"
        assert matched == kwargs, f"round-trip params diverged: {kwargs} -> {matched}"

    print("url_router: params exact (456+789=1245), 4 non-matches honest, "
          "reverse build exact, 3 round-trips identical — PASS")


if __name__ == "__main__":
    demo()