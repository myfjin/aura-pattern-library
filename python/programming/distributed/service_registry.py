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
    """Demo of the service registry."""
    registry = ServiceRegistry()
    
    # Register some services
    web_id = registry.register("web-server", "192.168.1.10", 8080, {"production", "frontend"})
    api_id = registry.register("api-server", "192.168.1.20", 3000, {"production", "backend"})
    db_id = registry.register("database", "192.168.1.30", 5432, {"production", "database"})
    
    print(f"Registered services: {web_id}, {api_id}, {db_id}")
    
    # Find services
    web_services = registry.find("web-server")
    print(f"Found {len(web_services)} web services")
    
    production_services = registry.find("web-server", {"production"})
    print(f"Found {len(production_services)} production web services")
    
    # Send heartbeats
    for _ in range(5):
        registry.heartbeat(web_id)
        registry.heartbeat(api_id)
        time.sleep(0.1)
    
    print("Sent heartbeats")
    
    # Deregister a service
    registry.deregister(db_id)
    db_services = registry.find("database")
    print(f"Found {len(db_services)} database services after deregistering")
    
    # Test expiration by waiting
    print("Waiting for service expiration...")
    time.sleep(1)
    
    # This service should still be alive due to heartbeats
    web_services = registry.find("web-server")
    print(f"Found {len(web_services)} web services after waiting")


if __name__ == "__main__":
    main()