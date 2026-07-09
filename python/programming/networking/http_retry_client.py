"""
HTTP Client with Retry, Backoff, and Circuit Breaker Support

This module provides a robust HTTP client that supports configurable retry policies,
exponential backoff, and circuit breaker pattern to handle transient failures gracefully.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import time
import random
import logging
from enum import Enum
from typing import Optional, Callable, Any, Dict, Tuple
from dataclasses import dataclass
from abc import ABC, abstractmethod
import urllib.request
import urllib.error
import json

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class HTTPException(Exception):
    """Base exception for HTTP client errors"""
    pass


class CircuitBreakerException(HTTPException):
    """Exception raised when circuit breaker is open"""
    pass


class CircuitState(Enum):
    """Circuit breaker states"""
    CLOSED = "closed"
    OPEN = "open"
    HALF_OPEN = "half_open"


@dataclass
class HTTPResponse:
    """HTTP response container"""
    status_code: int
    headers: Dict[str, str]
    body: bytes
    url: str

    def json(self) -> Any:
        """Parse response body as JSON"""
        return json.loads(self.body.decode('utf-8'))


class RetryPolicy:
    """Configurable retry policy"""
    
    def __init__(
        self,
        max_attempts: int = 3,
        status_codes: Tuple[int, ...] = (429, 500, 502, 503, 504),
        exceptions: Tuple[type, ...] = (urllib.error.URLError,)
    ):
        """
        Initialize retry policy.
        
        Args:
            max_attempts: Maximum number of retry attempts
            status_codes: HTTP status codes that should trigger retries
            exceptions: Exception types that should trigger retries
        """
        self.max_attempts = max_attempts
        self.status_codes = status_codes
        self.exceptions = exceptions


class BackoffStrategy(ABC):
    """Abstract base class for backoff strategies"""
    
    @abstractmethod
    def calculate_delay(self, attempt: int) -> float:
        """
        Calculate delay for given attempt number.
        
        Args:
            attempt: Current attempt number (1-based)
            
        Returns:
            Delay in seconds
        """
        pass


class ExponentialBackoff(BackoffStrategy):
    """Exponential backoff with jitter"""
    
    def __init__(
        self,
        base_delay: float = 1.0,
        max_delay: float = 60.0,
        multiplier: float = 2.0,
        jitter: bool = True
    ):
        """
        Initialize exponential backoff.
        
        Args:
            base_delay: Initial delay in seconds
            max_delay: Maximum delay in seconds
            multiplier: Multiplier for each subsequent delay
            jitter: Whether to add random jitter
        """
        self.base_delay = base_delay
        self.max_delay = max_delay
        self.multiplier = multiplier
        self.jitter = jitter
    
    def calculate_delay(self, attempt: int) -> float:
        """Calculate exponential backoff delay"""
        delay = min(
            self.base_delay * (self.multiplier ** (attempt - 1)),
            self.max_delay
        )
        
        if self.jitter:
            delay = delay / 2 + random.uniform(0, delay) / 2
            
        return delay


class CircuitBreaker:
    """Circuit breaker implementation"""
    
    def __init__(
        self,
        failure_threshold: int = 5,
        recovery_timeout: float = 30.0,
        expected_exception: type = Exception
    ):
        """
        Initialize circuit breaker.
        
        Args:
            failure_threshold: Number of failures before opening circuit
            recovery_timeout: Time in seconds before trying to close circuit
            expected_exception: Exception type to count as failure
        """
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.expected_exception = expected_exception
        
        self.failure_count = 0
        self.last_failure_time: Optional[float] = None
        self.state = CircuitState.CLOSED
    
    def call(self, func: Callable, *args, **kwargs) -> Any:
        """
        Execute function through circuit breaker.
        
        Args:
            func: Function to execute
            *args: Positional arguments for function
            **kwargs: Keyword arguments for function
            
        Returns:
            Function result
            
        Raises:
            CircuitBreakerException: If circuit is open
            Exception: Any exception raised by the function
        """
        if self.state == CircuitState.OPEN:
            if self.last_failure_time and (
                time.time() - self.last_failure_time > self.recovery_timeout
            ):
                self.state = CircuitState.HALF_OPEN
            else:
                raise CircuitBreakerException("Circuit breaker is OPEN")
        
        try:
            result = func(*args, **kwargs)
            self.on_success()
            return result
        except self.expected_exception as e:
            self.on_failure()
            raise e
    
    def on_success(self) -> None:
        """Handle successful call"""
        self.failure_count = 0
        self.state = CircuitState.CLOSED
    
    def on_failure(self) -> None:
        """Handle failed call"""
        self.failure_count += 1
        self.last_failure_time = time.time()
        
        if self.failure_count >= self.failure_threshold:
            self.state = CircuitState.OPEN


class HTTPClient:
    """HTTP client with retry, backoff, and circuit breaker support"""
    
    def __init__(
        self,
        retry_policy: Optional[RetryPolicy] = None,
        backoff_strategy: Optional[BackoffStrategy] = None,
        circuit_breaker: Optional[CircuitBreaker] = None
    ):
        """
        Initialize HTTP client.
        
        Args:
            retry_policy: Retry policy to use
            backoff_strategy: Backoff strategy to use
            circuit_breaker: Circuit breaker to use
        """
        self.retry_policy = retry_policy or RetryPolicy()
        self.backoff_strategy = backoff_strategy or ExponentialBackoff()
        self.circuit_breaker = circuit_breaker or CircuitBreaker()
    
    def _make_request(self, request: urllib.request.Request) -> HTTPResponse:
        """
        Make a single HTTP request.
        
        Args:
            request: urllib request object
            
        Returns:
            HTTP response
            
        Raises:
            urllib.error.HTTPError: For HTTP errors
            urllib.error.URLError: For URL errors
        """
        try:
            with urllib.request.urlopen(request) as response:
                return HTTPResponse(
                    status_code=response.getcode(),
                    headers=dict(response.headers),
                    body=response.read(),
                    url=response.geturl()
                )
        except urllib.error.HTTPError as e:
            # Re-raise with status code for retry logic
            raise urllib.error.HTTPError(
                e.url, e.code, e.msg, e.headers, e.fp
            ) from e
    
    def request(
        self,
        method: str,
        url: str,
        headers: Optional[Dict[str, str]] = None,
        data: Optional[bytes] = None
    ) -> HTTPResponse:
        """
        Make HTTP request with retry and circuit breaker.
        
        Args:
            method: HTTP method (GET, POST, etc.)
            url: Request URL
            headers: Request headers
            data: Request body data
            
        Returns:
            HTTP response
            
        Raises:
            HTTPException: For unrecoverable errors
        """
        request = urllib.request.Request(
            url=url,
            data=data,
            headers=headers or {},
            method=method
        )
        
        last_exception: Optional[Exception] = None
        
        for attempt in range(1, self.retry_policy.max_attempts + 1):
            try:
                # Execute request through circuit breaker
                response = self.circuit_breaker.call(
                    self._make_request, request
                )
                
                # Check if response should be retried
                if response.status_code in self.retry_policy.status_codes:
                    raise urllib.error.HTTPError(
                        url, response.status_code, "Retryable status", 
                        {}, None
                    )
                
                return response
                
            except self.retry_policy.exceptions as e:
                last_exception = e
                
                # If this is the last attempt, don't retry
                if attempt == self.retry_policy.max_attempts:
                    break
                
                # Check if this is a retryable status code
                if isinstance(e, urllib.error.HTTPError) and \
                   e.code not in self.retry_policy.status_codes:
                    raise HTTPException(f"Non-retryable HTTP error: {e.code}") from e
                
                # Calculate and apply backoff delay
                delay = self.backoff_strategy.calculate_delay(attempt)
                logger.info(
                    f"Attempt {attempt} failed. Retrying in {delay:.2f}s..."
                )
                time.sleep(delay)
        
        # If we get here, all retries failed
        raise HTTPException(
            f"Request failed after {self.retry_policy.max_attempts} attempts"
        ) from last_exception
    
    def get(self, url: str, headers: Optional[Dict[str, str]] = None) -> HTTPResponse:
        """Make GET request"""
        return self.request("GET", url, headers)
    
    def post(
        self, 
        url: str, 
        data: Optional[bytes] = None, 
        headers: Optional[Dict[str, str]] = None
    ) -> HTTPResponse:
        """Make POST request"""
        return self.request("POST", url, headers, data)
    
    def put(
        self, 
        url: str, 
        data: Optional[bytes] = None, 
        headers: Optional[Dict[str, str]] = None
    ) -> HTTPResponse:
        """Make PUT request"""
        return self.request("PUT", url, headers, data)
    
    def delete(self, url: str, headers: Optional[Dict[str, str]] = None) -> HTTPResponse:
        """Make DELETE request"""
        return self.request("DELETE", url, headers)


def main():
    """Demo of HTTP client against a local test server (no external network needed)"""
    import http.server
    import threading

    class DemoHandler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            if self.path.startswith("/status/"):
                code = int(self.path.rsplit("/", 1)[1])
            else:
                code = 200
            body = json.dumps({"url": self.path}).encode()
            self.send_response(code)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, *args):
            pass  # keep demo output clean

    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), DemoHandler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{server.server_address[1]}"

    # Create a client with custom retry policy and backoff
    client = HTTPClient(
        retry_policy=RetryPolicy(
            max_attempts=3,
            status_codes=(429, 500, 502, 503, 504),
            exceptions=(urllib.error.URLError,)
        ),
        backoff_strategy=ExponentialBackoff(
            base_delay=0.5,
            max_delay=5.0,
            multiplier=2.0,
            jitter=True
        ),
        circuit_breaker=CircuitBreaker(
            failure_threshold=3,
            recovery_timeout=2.0
        )
    )
    
    # Demo 1: Successful request
    print("=== Demo 1: Successful Request ===")
    try:
        response = client.get(f"{base}/get")
        print(f"Status: {response.status_code}")
        print(f"URL: {response.url}")
        print("Success!")
    except Exception as e:
        print(f"Error: {e}")
    
    print()
    
    # Demo 2: Retryable error
    print("=== Demo 2: Retryable Error ===")
    try:
        # This will fail with 500 error and retry
        response = client.get(f"{base}/status/500")
        print(f"Status: {response.status_code}")
    except HTTPException as e:
        print(f"Failed after retries: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    
    print()
    
    # Demo 3: Circuit breaker
    print("=== Demo 3: Circuit Breaker ===")
    print("Making several failing requests to trigger circuit breaker...")
    
    for i in range(5):
        try:
            response = client.get(f"{base}/status/503")
            print(f"Request {i+1}: Success (unexpected)")
        except CircuitBreakerException as e:
            print(f"Request {i+1}: Circuit breaker open - {e}")
        except HTTPException as e:
            print(f"Request {i+1}: Failed - {e}")
        except Exception as e:
            print(f"Request {i+1}: Unexpected error - {e}")
    
    print("Waiting for circuit breaker to recover...")
    time.sleep(3)  # Wait for recovery timeout

    print("Making request after recovery time:")
    try:
        response = client.get(f"{base}/get")
        print(f"Status: {response.status_code}")
        print("Recovered successfully!")
    except Exception as e:
        print(f"Recovery failed: {e}")

    server.shutdown()


if __name__ == "__main__":
    main()