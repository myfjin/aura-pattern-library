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
    """Self-test: backoff arithmetic exact, circuit breaker lifecycle on a
    fake clock, retry counts proven against a stubbed transport, plus one
    real request against a local server (no external network)."""
    # 1. Exponential backoff without jitter is exact: 0.5, 1, 2, 4, cap 5.
    bo = ExponentialBackoff(base_delay=0.5, max_delay=5.0, multiplier=2.0, jitter=False)
    trace = [bo.calculate_delay(a) for a in (1, 2, 3, 4, 5)]
    assert trace == [0.5, 1.0, 2.0, 4.0, 5.0], f"backoff trace wrong: {trace}"
    jbo = ExponentialBackoff(base_delay=0.5, max_delay=5.0, multiplier=2.0, jitter=True)
    random.seed(42)
    assert all(0 < jbo.calculate_delay(a) <= 5.0 for a in range(1, 8)), "jitter escaped bounds"

    # 2. Circuit breaker lifecycle on a fake clock.
    _now = [10_000.0]
    _real_time = time.time
    time.time = lambda: _now[0]
    try:
        cb = CircuitBreaker(failure_threshold=3, recovery_timeout=2.0)
        def boom():
            raise ValueError("down")
        failures = 0
        for _ in range(3):
            try:
                cb.call(boom)
            except ValueError:
                failures += 1
        assert failures == 3 and cb.state == CircuitState.OPEN, \
            f"3 failures must OPEN the breaker, state {cb.state}"
        # While OPEN, calls are rejected WITHOUT invoking the function.
        called = [0]
        def probe():
            called[0] += 1
            return "ok"
        try:
            cb.call(probe)
            assert False, "OPEN breaker let a call through"
        except CircuitBreakerException:
            pass
        assert called[0] == 0, "OPEN breaker still invoked the function"
        # After the recovery timeout it half-opens; success CLOSES it.
        _now[0] += 2.1
        assert cb.call(probe) == "ok"
        assert cb.state == CircuitState.CLOSED, f"half-open success must close, state {cb.state}"
        assert called[0] == 1
    finally:
        time.time = _real_time

    # 3. Retry counting against a stubbed transport (no sockets, no sleeps).
    client_stub = HTTPClient(
        retry_policy=RetryPolicy(max_attempts=3),
        backoff_strategy=ExponentialBackoff(base_delay=0.01, max_delay=1.0,
                                            multiplier=2.0, jitter=False),
        circuit_breaker=CircuitBreaker(failure_threshold=100),
    )
    attempts = [0]
    def flaky_transport(request):
        attempts[0] += 1
        if attempts[0] < 3:
            raise urllib.error.URLError("transient")
        return HTTPResponse(status_code=200, headers={}, body=b"{}", url=request.full_url)
    client_stub._make_request = flaky_transport
    slept = []
    _real_sleep = time.sleep
    time.sleep = lambda s: slept.append(s)
    try:
        resp = client_stub.request("GET", "http://stub.local/x")
        assert resp.status_code == 200
        assert attempts[0] == 3, f"2 transients + success must take 3 attempts, took {attempts[0]}"
        assert slept == [0.01, 0.02], f"backoff sleeps must be [0.01, 0.02], got {slept}"

        # Permanent failure: exactly max_attempts tries, then HTTPException.
        attempts[0] = 0
        def always_down(request):
            attempts[0] += 1
            raise urllib.error.URLError("dead")
        client_stub._make_request = always_down
        try:
            client_stub.request("GET", "http://stub.local/x")
            assert False, "dead endpoint returned a response"
        except HTTPException:
            pass
        assert attempts[0] == 3, f"must stop at max_attempts=3, tried {attempts[0]}"
    finally:
        time.sleep = _real_sleep

    _live_server_check()
    print("http_retry_client: backoff 0.5/1/2/4/cap5 exact, breaker "
          "open→half-open→closed, retries 3/3 with sleeps [0.01,0.02], "
          "live 200 — PASS")


def _live_server_check():
    """One real request through the full urllib stack against a local server."""
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

    client = HTTPClient(
        retry_policy=RetryPolicy(max_attempts=2),
        backoff_strategy=ExponentialBackoff(base_delay=0.05, max_delay=0.2,
                                            multiplier=2.0, jitter=False),
        circuit_breaker=CircuitBreaker(failure_threshold=10, recovery_timeout=1.0),
    )

    # A real 200 through the full stack, body parsed.
    response = client.get(f"{base}/get")
    assert response.status_code == 200, f"live GET returned {response.status_code}"
    assert response.json()["url"] == "/get", f"live body wrong: {response.body!r}"

    # A retryable 500 exhausts its attempts and raises honestly.
    try:
        client.get(f"{base}/status/500")
        assert False, "500 endpoint returned a response"
    except HTTPException:
        pass

    server.shutdown()


if __name__ == "__main__":
    main()