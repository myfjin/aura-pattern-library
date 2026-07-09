"""
HTTP Request Multiplexer Module

A lightweight HTTP request multiplexer that routes requests based on path and method,
with support for middleware chains and parameterized routes.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import re
from typing import Dict, List, Callable, Any, Optional, Tuple, Union
from dataclasses import dataclass
from enum import Enum


class HTTPMethod(Enum):
    """HTTP methods supported by the multiplexer."""
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"
    HEAD = "HEAD"
    OPTIONS = "OPTIONS"


@dataclass
class Request:
    """HTTP request object."""
    method: HTTPMethod
    path: str
    headers: Dict[str, str]
    body: Optional[str] = None
    params: Dict[str, str] = None
    
    def __post_init__(self):
        if self.params is None:
            self.params = {}


@dataclass
class Response:
    """HTTP response object."""
    status_code: int
    body: str
    headers: Dict[str, str] = None
    
    def __post_init__(self):
        if self.headers is None:
            self.headers = {}


class Handler:
    """Request handler that processes incoming requests."""
    
    def __init__(self, func: Callable[[Request], Response]):
        """
        Initialize a handler with a function.
        
        Args:
            func: Function that takes a Request and returns a Response
        """
        self.func = func
    
    def handle(self, request: Request) -> Response:
        """
        Handle a request.
        
        Args:
            request: The incoming request
            
        Returns:
            Response object
        """
        try:
            return self.func(request)
        except Exception as e:
            return Response(500, f"Internal Server Error: {str(e)}")


class Route:
    """Represents a route with path pattern, methods, and handler."""
    
    def __init__(self, path: str, methods: List[HTTPMethod], handler: Handler):
        """
        Initialize a route.
        
        Args:
            path: Path pattern (can include parameters like /user/{id})
            methods: List of HTTP methods this route supports
            handler: Handler to process requests to this route
        """
        self.path = path
        self.methods = methods
        self.handler = handler
        self._compile_pattern()
    
    def _compile_pattern(self) -> None:
        """Compile the path pattern into a regex for matching."""
        # Convert path parameters like {id} to regex groups
        pattern = re.sub(r'{([^}]+)}', r'(?P<\1>[^/]+)', self.path)
        # Ensure the pattern matches the entire path
        self.pattern = re.compile(f'^{pattern}$')
    
    def matches(self, path: str) -> Optional[Dict[str, str]]:
        """
        Check if this route matches the given path.
        
        Args:
            path: The path to match against
            
        Returns:
            Dictionary of path parameters if match, None otherwise
        """
        match = self.pattern.match(path)
        if match:
            return match.groupdict()
        return None


class Middleware:
    """Middleware that can process requests before they reach handlers."""
    
    def __init__(self, func: Callable[[Request, Callable[[], Response]], Response]):
        """
        Initialize middleware.
        
        Args:
            func: Function that takes a request and next function, returns response
        """
        self.func = func
    
    def process(self, request: Request, next_func: Callable[[], Response]) -> Response:
        """
        Process the request.
        
        Args:
            request: The incoming request
            next_func: Function to call to continue the chain
            
        Returns:
            Response object
        """
        return self.func(request, next_func)


class Multiplexer:
    """HTTP request multiplexer that routes requests to appropriate handlers."""
    
    def __init__(self):
        """Initialize the multiplexer."""
        self.routes: List[Route] = []
        self.middlewares: List[Middleware] = []
    
    def add_route(self, path: str, methods: List[HTTPMethod], handler: Handler) -> None:
        """
        Add a route to the multiplexer.
        
        Args:
            path: Path pattern
            methods: List of HTTP methods
            handler: Handler for this route
        """
        route = Route(path, methods, handler)
        self.routes.append(route)
    
    def add_middleware(self, middleware: Middleware) -> None:
        """
        Add middleware to the chain.
        
        Args:
            middleware: Middleware to add
        """
        self.middlewares.append(middleware)
    
    def route(self, path: str, methods: List[HTTPMethod]):
        """
        Decorator for adding routes.
        
        Args:
            path: Path pattern
            methods: List of HTTP methods
            
        Returns:
            Decorator function
        """
        def decorator(func: Callable[[Request], Response]):
            handler = Handler(func)
            self.add_route(path, methods, handler)
            return func
        return decorator
    
    def dispatch(self, request: Request) -> Response:
        """
        Dispatch a request to the appropriate handler.
        
        Args:
            request: The incoming request
            
        Returns:
            Response from the handler
        """
        # Find matching route
        route, params = self._find_route(request.path, request.method)
        
        if route is None:
            return Response(404, "Not Found")
        
        # Add path parameters to request
        request.params = params
        
        # Process through middleware chain
        def final_handler():
            return route.handler.handle(request)
        
        return self._process_middlewares(request, final_handler, 0)
    
    def _find_route(self, path: str, method: HTTPMethod) -> Tuple[Optional[Route], Dict[str, str]]:
        """
        Find a route that matches the path and method.
        
        Args:
            path: Request path
            method: HTTP method
            
        Returns:
            Tuple of (route, params) or (None, {})
        """
        for route in self.routes:
            if method not in route.methods:
                continue
                
            params = route.matches(path)
            if params is not None:
                return route, params
        
        return None, {}
    
    def _process_middlewares(self, request: Request, final_handler: Callable[[], Response], index: int) -> Response:
        """
        Process the request through the middleware chain.
        
        Args:
            request: The request
            final_handler: The final handler to call
            index: Current middleware index
            
        Returns:
            Response from the chain
        """
        # If we've processed all middlewares, call the final handler
        if index >= len(self.middlewares):
            return final_handler()
        
        # Get current middleware
        middleware = self.middlewares[index]
        
        # Create next function that processes the rest of the chain
        def next_func():
            return self._process_middlewares(request, final_handler, index + 1)
        
        # Process with current middleware
        return middleware.process(request, next_func)


def create_default_handler(message: str) -> Callable[[Request], Response]:
    """Create a simple handler that returns a fixed message."""
    def handler(request: Request) -> Response:
        return Response(200, message)
    return handler


def create_param_handler() -> Callable[[Request], Response]:
    """Create a handler that uses path parameters."""
    def handler(request: Request) -> Response:
        params_str = ", ".join([f"{k}={v}" for k, v in request.params.items()])
        return Response(200, f"Params: {params_str}")
    return handler


def logging_middleware(request: Request, next_func: Callable[[], Response]) -> Response:
    """Simple logging middleware."""
    print(f"Request: {request.method.value} {request.path}")
    response = next_func()
    print(f"Response: {response.status_code}")
    return response


def auth_middleware(request: Request, next_func: Callable[[], Response]) -> Response:
    """Simple authentication middleware."""
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        return Response(401, "Unauthorized")
    return next_func()


def main():
    """Demo the multiplexer functionality."""
    # Create multiplexer
    mux = Multiplexer()
    
    # Add middlewares
    mux.add_middleware(Middleware(logging_middleware))
    mux.add_middleware(Middleware(auth_middleware))
    
    # Add routes using decorator
    @mux.route("/", [HTTPMethod.GET])
    def home_handler(request: Request) -> Response:
        return Response(200, "Welcome to the home page!")
    
    @mux.route("/user/{id}", [HTTPMethod.GET])
    def user_handler(request: Request) -> Response:
        user_id = request.params["id"]
        return Response(200, f"User profile for ID: {user_id}")
    
    @mux.route("/api/data", [HTTPMethod.POST])
    def data_handler(request: Request) -> Response:
        return Response(201, "Data created successfully")
    
    # Add route using add_route method
    mux.add_route("/health", [HTTPMethod.GET], Handler(create_default_handler("OK")))
    
    # Test requests
    test_requests = [
        Request(HTTPMethod.GET, "/", {"Authorization": "Bearer token"}),
        Request(HTTPMethod.GET, "/user/123", {"Authorization": "Bearer token"}),
        Request(HTTPMethod.POST, "/api/data", {"Authorization": "Bearer token"}, "sample data"),
        Request(HTTPMethod.GET, "/health", {"Authorization": "Bearer token"}),
        Request(HTTPMethod.GET, "/nonexistent", {"Authorization": "Bearer token"}),
        Request(HTTPMethod.GET, "/", {}),  # No auth header
    ]
    
    print("Testing HTTP Multiplexer")
    print("=" * 30)
    
    for i, req in enumerate(test_requests, 1):
        print(f"\nTest {i}: {req.method.value} {req.path}")
        response = mux.dispatch(req)
        print(f"Status: {response.status_code}")
        print(f"Body: {response.body}")


if __name__ == "__main__":
    main()