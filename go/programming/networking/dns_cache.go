package main

import (
	"fmt"
	"os"
	"sort"
	"strings"
	"time"
)

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
var now float64

type Record struct {
	Name       string
	RecordType string
	Value      string
	TTL        int
}

type CacheEntry struct {
	record     *Record
	isNegative bool
	timestamp  float64
	lastAccess float64
}

func (ce *CacheEntry) IsExpired() bool {
	if ce.isNegative {
		return now-ce.timestamp > 30
	}
	if ce.record == nil {
		return true
	}
	return now-ce.timestamp > float64(ce.record.TTL)
}

func (ce *CacheEntry) UpdateAccessTime() {
	ce.lastAccess = now
}

type DNSCache struct {
	maxSize int
	cache   map[string]*CacheEntry
	order   []string
}

func NewDNSCache(maxSize int) *DNSCache {
	if maxSize <= 0 {
		fmt.Fprintln(os.Stderr, "max_size must be positive")
		os.Exit(1)
	}
	return &DNSCache{
		maxSize: maxSize,
		cache:   make(map[string]*CacheEntry),
		order:   []string{},
	}
}

func (c *DNSCache) key(name, recordType string) string {
	return name + ":" + recordType
}

func (c *DNSCache) evictIfNeeded() {
	for len(c.cache) >= c.maxSize {
		victim := c.order[0]
		c.order = c.order[1:]
		delete(c.cache, victim)
	}
}

func (c *DNSCache) refresh(key string) {
	for i, k := range c.order {
		if k == key {
			c.order = append(c.order[:i], c.order[i+1:]...)
			break
		}
	}
	c.order = append(c.order, key)
}

func (c *DNSCache) Lookup(name, recordType string) *Record {
	key := c.key(name, recordType)
	entry, ok := c.cache[key]
	if !ok {
		return nil
	}
	entry.UpdateAccessTime()
	c.refresh(key)
	if entry.IsExpired() {
		delete(c.cache, key)
		return nil
	}
	if entry.isNegative {
		return nil
	}
	return entry.record
}

func (c *DNSCache) Insert(record *Record) {
	key := c.key(record.Name, record.RecordType)
	if _, ok := c.cache[key]; ok {
		delete(c.cache, key)
	} else {
		c.evictIfNeeded()
	}
	c.cache[key] = &CacheEntry{record: record, timestamp: now, lastAccess: now}
	c.refresh(key)
}

func (c *DNSCache) InsertNegative(name, recordType string) {
	key := c.key(name, recordType)
	if _, ok := c.cache[key]; ok {
		delete(c.cache, key)
	} else {
		c.evictIfNeeded()
	}
	c.cache[key] = &CacheEntry{isNegative: true, timestamp: now, lastAccess: now}
	c.refresh(key)
}

func (c *DNSCache) ClearExpired() int {
	expired := []string{}
	for key, entry := range c.cache {
		if entry.IsExpired() {
			expired = append(expired, key)
		}
	}
	sort.Strings(expired)
	for _, key := range expired {
		delete(c.cache, key)
	}
	newOrder := []string{}
	for _, k := range c.order {
		if _, ok := c.cache[k]; ok {
			newOrder = append(newOrder, k)
		}
	}
	c.order = newOrder
	return len(expired)
}

func (c *DNSCache) Size() int {
	return len(c.cache)
}

func (c *DNSCache) Clear() {
	c.cache = make(map[string]*CacheEntry)
	c.order = []string{}
}

func main() {
	now = 100000.0

	cache := NewDNSCache(5)
	cache.Insert(&Record{"example.com", "A", "93.184.216.34", 60})
	cache.Insert(&Record{"google.com", "A", "142.250.74.110", 120})
	cache.Insert(&Record{"example.com", "AAAA", "2606::1946", 60})
	if !(cache.Size() == 3) {
		fmt.Fprintf(os.Stderr, "expected size 3, got %d\n", cache.Size())
		os.Exit(1)
	}

	r := cache.Lookup("example.com", "A")
	if !(r != nil && r.Value == "93.184.216.34") {
		fmt.Fprintln(os.Stderr, "example.com A lookup wrong")
		os.Exit(1)
	}
	r = cache.Lookup("example.com", "AAAA")
	if !(r != nil && r.Value == "2606::1946") {
		fmt.Fprintln(os.Stderr, "example.com AAAA lookup wrong")
		os.Exit(1)
	}
	if !(cache.Lookup("example.com", "MX") == nil) {
		fmt.Fprintln(os.Stderr, "example.com MX should miss")
		os.Exit(1)
	}
	if !(cache.Lookup("nonexistent.com", "A") == nil) {
		fmt.Fprintln(os.Stderr, "nonexistent.com A should miss")
		os.Exit(1)
	}

	now += 59
	if !(cache.Lookup("example.com", "A") != nil) {
		fmt.Fprintln(os.Stderr, "record died before its TTL")
		os.Exit(1)
	}
	now += 2
	if !(cache.Lookup("example.com", "A") == nil) {
		fmt.Fprintln(os.Stderr, "record survived past its TTL")
		os.Exit(1)
	}
	if !(cache.Lookup("google.com", "A") != nil) {
		fmt.Fprintln(os.Stderr, "longer TTL record wrongly expired")
		os.Exit(1)
	}

	cache.InsertNegative("missing.com", "A")
	if !(cache.Lookup("missing.com", "A") == nil) {
		fmt.Fprintln(os.Stderr, "negative lookup should miss")
		os.Exit(1)
	}
	negKey := "missing.com:A"
	if _, ok := cache.cache[negKey]; !ok {
		fmt.Fprintln(os.Stderr, "negative entry not stored")
		os.Exit(1)
	}
	now += 31
	cache.ClearExpired()
	if _, ok := cache.cache[negKey]; ok {
		fmt.Fprintln(os.Stderr, "negative entry outlived its 30s window")
		os.Exit(1)
	}

	fresh := NewDNSCache(10)
	for i := 0; i < 4; i++ {
		fresh.Insert(&Record{fmt.Sprintf("h%d.com", i), "A", fmt.Sprintf("1.1.1.%d", i), 50})
	}
	fresh.Insert(&Record{"long.com", "A", "9.9.9.9", 500})
	now += 60
	removed := fresh.ClearExpired()
	if !(removed == 4) {
		fmt.Fprintf(os.Stderr, "exactly 4 of 5 records expired, clear removed %d\n", removed)
		os.Exit(1)
	}
	if !(fresh.Size() == 1 && fresh.Lookup("long.com", "A") != nil) {
		fmt.Fprintln(os.Stderr, "long.com should survive")
		os.Exit(1)
	}

	lru := NewDNSCache(3)
	lru.Insert(&Record{"a.com", "A", "1.0.0.1", 500})
	lru.Insert(&Record{"b.com", "A", "1.0.0.2", 500})
	lru.Insert(&Record{"c.com", "A", "1.0.0.3", 500})
	lru.Lookup("a.com", "A")
	lru.Insert(&Record{"d.com", "A", "1.0.0.4", 500})
	if !(lru.Size() == 3) {
		fmt.Fprintf(os.Stderr, "capacity-3 cache holds %d\n", lru.Size())
		os.Exit(1)
	}
	if !(lru.Lookup("b.com", "A") == nil) {
		fmt.Fprintln(os.Stderr, "LRU victim should be the untouched b.com")
		os.Exit(1)
	}
	if !(lru.Lookup("a.com", "A") != nil) {
		fmt.Fprintln(os.Stderr, "recently-used a.com was evicted")
		os.Exit(1)
	}
	if !(lru.Lookup("d.com", "A") != nil) {
		fmt.Fprintln(os.Stderr, "d.com should be present")
		os.Exit(1)
	}

	lru.Clear()
	if !(lru.Size() == 0) {
		fmt.Fprintln(os.Stderr, "clear should empty")
		os.Exit(1)
	}

	fmt.Println("dns_cache: TTL exact (59s alive/61s dead), negative 30s window, clear_expired 4/5, LRU evicted the right victim — PASS")
	time.Sleep(1 * time.Millisecond)
}

func repeatString(s string, n int) string {
	return strings.Repeat(s, n)
}
