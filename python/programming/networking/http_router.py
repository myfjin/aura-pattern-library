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
    """Self-test: routing + params + method discrimination exact, middleware
    chain order and short-circuit, 404/401 honest."""
    mux = Multiplexer()

    # Middleware order probe: record entry order, auth short-circuits.
    seen = []
    def order_probe(request, next_func):
        seen.append("probe")
        return next_func()
    mux.add_middleware(Middleware(order_probe))
    mux.add_middleware(Middleware(auth_middleware))

    @mux.route("/", [HTTPMethod.GET])
    def home_handler(request: Request) -> Response:
        return Response(200, "home")

    @mux.route("/user/{id}", [HTTPMethod.GET])
    def user_handler(request: Request) -> Response:
        return Response(200, f"user:{request.params['id']}")

    @mux.route("/api/data", [HTTPMethod.POST])
    def data_handler(request: Request) -> Response:
        return Response(201, "created")

    mux.add_route("/health", [HTTPMethod.GET], Handler(create_default_handler("OK")))

    auth = {"Authorization": "Bearer token"}

    # Exact dispatch results.
    r = mux.dispatch(Request(HTTPMethod.GET, "/", dict(auth)))
    assert (r.status_code, r.body) == (200, "home"), f"home route wrong: {r.status_code}/{r.body}"

    r = mux.dispatch(Request(HTTPMethod.GET, "/user/123", dict(auth)))
    assert r.status_code == 200 and r.body == "user:123", f"param route wrong: {r.body}"

    r = mux.dispatch(Request(HTTPMethod.POST, "/api/data", dict(auth), "payload"))
    assert r.status_code == 201 and r.body == "created"

    r = mux.dispatch(Request(HTTPMethod.GET, "/health", dict(auth)))
    assert (r.status_code, r.body) == (200, "OK")

    # Method discrimination: GET on a POST-only route must not dispatch.
    r = mux.dispatch(Request(HTTPMethod.GET, "/api/data", dict(auth)))
    assert r.status_code in (404, 405), \
        f"GET on POST-only route returned {r.status_code}"

    # Unknown path → 404.
    r = mux.dispatch(Request(HTTPMethod.GET, "/nonexistent", dict(auth)))
    assert r.status_code == 404, f"missing route returned {r.status_code}"

    # AUTH short-circuit: without the header the handler never runs.
    seen.clear()
    r = mux.dispatch(Request(HTTPMethod.GET, "/", {}))
    assert r.status_code == 401 and r.body == "Unauthorized", \
        f"missing auth must 401, got {r.status_code}"
    assert seen == ["probe"], \
        "middleware order broken: probe must run before auth rejects"

    # Middleware runs once per dispatch, in registration order.
    seen.clear()
    mux.dispatch(Request(HTTPMethod.GET, "/", dict(auth)))
    assert seen == ["probe"], f"probe middleware ran {len(seen)} times"

    # Param extraction sums as planted numbers.
    r = mux.dispatch(Request(HTTPMethod.GET, "/user/450", dict(auth)))
    assert int(r.body.split(":")[1]) + 550 == 1000, "450 + 550 must be 1000"

    print("http_router: 4 routes exact (200/200/201/200), method+path honest "
          "(404), auth 401 short-circuit after probe, params exact — PASS")


if __name__ == "__main__":
    main()