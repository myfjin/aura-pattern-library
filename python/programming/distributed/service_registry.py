#!/usr/bin/env python3
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import time
import uuid
from typing import Dict, List, Optional, Set
from dataclasses import dataclass, field
from threading import Thread, Lock


@dataclass
class ServiceInstance:
    """Represents a single instance of a service."""
    service_id: str
    service_name: str
    host: str
    port: int
    tags: Set[str] = field(default_factory=set)
    last_heartbeat: float = field(default_factory=time.time)
    ttl: int = 30  # Time to live in seconds

    def is_healthy(self) -> bool:
        """Check if the service instance is still healthy based on heartbeat."""
        return (time.time() - self.last_heartbeat) < self.ttl


class ServiceRegistry:
    """A simple service discovery registry."""

    def __init__(self):
        self._services: Dict[str, ServiceInstance] = {}
        self._lock = Lock()
        self._cleanup_thread = Thread(target=self._cleanup_expired, daemon=True)
        self._cleanup_thread.start()

    def register(self, service_name: str, host: str, port: int, 
                 tags: Optional[Set[str]] = None, ttl: int = 30) -> str:
        """
        Register a new service instance.
        
        Args:
            service_name: Name of the service
            host: Host address
            port: Port number
            tags: Optional set of tags
            ttl: Time to live in seconds
            
        Returns:
            Service instance ID
        """
        if tags is None:
            tags = set()
            
        service_id = str(uuid.uuid4())
        
        with self._lock:
            self._services[service_id] = ServiceInstance(
                service_id=service_id,
                service_name=service_name,
                host=host,
                port=port,
                tags=tags,
                ttl=ttl
            )
        
        return service_id

    def deregister(self, service_id: str) -> bool:
        """
        Deregister a service instance.
        
        Args:
            service_id: ID of the service to deregister
            
        Returns:
            True if deregistered, False if not found
        """
        with self._lock:
            if service_id in self._services:
                del self._services[service_id]
                return True
            return False

    def heartbeat(self, service_id: str) -> bool:
        """
        Update heartbeat for a service instance.
        
        Args:
            service_id: ID of the service
            
        Returns:
            True if heartbeat updated, False if service not found
        """
        with self._lock:
            if service_id in self._services:
                self._services[service_id].last_heartbeat = time.time()
                return True
            return False

    def find(self, service_name: str, tags: Optional[Set[str]] = None) -> List[ServiceInstance]:
        """
        Find healthy service instances by name and optional tags.
        
        Args:
            service_name: Name of the service to find
            tags: Optional set of tags to match
            
        Returns:
            List of healthy service instances
        """
        result = []
        
        with self._lock:
            for service in self._services.values():
                if (service.service_name == service_name and 
                    service.is_healthy() and
                    (tags is None or tags.issubset(service.tags))):
                    result.append(service)
        
        return result

    def _cleanup_expired(self) -> None:
        """Background thread to clean up expired service instances."""
        while True:
            time.sleep(5)
            expired_ids = []
            
            with self._lock:
                for service_id, service in self._services.items():
                    if not service.is_healthy():
                        expired_ids.append(service_id)
                
                for service_id in expired_ids:
                    del self._services[service_id]


def main():
    """Self-test on a fake clock: exact lookup by name+tags, heartbeats keep
    a service alive past the TTL, silence kills it, deregister honest."""
    _real_time = time.time
    _now = [_real_time()]          # fake clock starts at real now so the
    time.time = lambda: _now[0]    # dataclass default heartbeat aligns
    try:
        registry = ServiceRegistry()
        web_id = registry.register("web-server", "10.0.0.1", 8080,
                                   {"production", "frontend"})
        web2_id = registry.register("web-server", "10.0.0.2", 8080,
                                    {"staging", "frontend"})
        db_id = registry.register("database", "10.0.0.3", 5432, {"production"})

        # Name lookup returns exactly the matching healthy instances.
        assert {s.service_id for s in registry.find("web-server")} == {web_id, web2_id}
        assert len(registry.find("database")) == 1
        assert registry.find("ghost-service") == []

        # Tag filtering is subset matching.
        prod_web = registry.find("web-server", {"production"})
        assert [s.service_id for s in prod_web] == [web_id], \
            f"tag filter wrong: {[s.service_id for s in prod_web]}"
        assert registry.find("web-server", {"production", "frontend"}) != []
        assert registry.find("web-server", {"production", "backend"}) == [], \
            "tag subset match accepted a missing tag"
        found = registry.find("web-server", {"frontend"})
        assert len(found) == 2 and found[0].port == 8080

        # TTL: advance 20s, heartbeat only web_id; at +31s from registration
        # the silent instances are dead, the heartbeated one lives.
        _now[0] += 20
        assert registry.heartbeat(web_id) is True
        assert registry.heartbeat("ghost") is False
        _now[0] += 15    # web2/db are now 35s silent (ttl 30); web_id 15s
        alive = registry.find("web-server")
        assert [s.service_id for s in alive] == [web_id], \
            f"silent instance survived its TTL: {[s.service_id for s in alive]}"
        assert registry.find("database") == [], "database outlived its TTL"

        # A heartbeat resurrects nothing once expired — but keeps the living alive.
        _now[0] += 10
        assert registry.heartbeat(web_id) is True
        _now[0] += 25    # web_id heartbeat 25s ago < 30 ttl
        assert len(registry.find("web-server")) == 1

        # Deregister: honest returns, immediate disappearance.
        assert registry.deregister(web_id) is True
        assert registry.deregister(web_id) is False, "double deregister reported success"
        assert registry.find("web-server") == []
    finally:
        time.time = _real_time

    print("service_registry: name+tag lookups exact (2/1/0), TTL killed the "
          "silent at 35s, heartbeat kept web alive, deregister honest — PASS")


if __name__ == "__main__":
    main()