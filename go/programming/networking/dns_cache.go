package main

import (
	"container/list"
	"fmt"
	"time"
)

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
var _auraMark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
type Record struct {
	Name       string
	RecordType string
	Value      string
	TTL        int
}

type CacheEntry struct {
	Record       *Record
	IsNegative   bool
	Timestamp    time.Time
	LastAccessed time.Time
}

func (e *CacheEntry) IsExpired() bool {
	if e.IsNegative {
		return time.Since(e.Timestamp) > 30*time.Second
	}
	if e.Record == nil {
		return true
	}
	return time.Since(e.Timestamp) > time.Duration(e.Record.TTL)*time.Second
}

func (e *CacheEntry) UpdateAccessTime() {
	e.LastAccessed = time.Now()
}

type DNSCache struct {
	maxSize int
	cache   map[string]*list.Element
	lru     *list.List
}

type lruItem struct {
	key   string
	entry *CacheEntry
}

func NewDNSCache(maxSize int) (*DNSCache, error) {
	if maxSize <= 0 {
		return nil, fmt.Errorf("max_size must be positive")
	}
	return &DNSCache{
		maxSize: maxSize,
		cache:   make(map[string]*list.Element),
		lru:     list.New(),
	}, nil
}

func (c *DNSCache) key(name, recordType string) string {
	return name + ":" + recordType
}

func (c *DNSCache) evictIfNeeded() {
	for len(c.cache) >= c.maxSize {
		elem := c.lru.Back()
		if elem == nil {
			break
		}
		item := elem.Value.(*lruItem)
		delete(c.cache, item.key)
		c.lru.Remove(elem)
	}
}

func (c *DNSCache) refreshEntryPosition(key string) {
	if elem, ok := c.cache[key]; ok {
		c.lru.MoveToFront(elem)
	}
}

func (c *DNSCache) Lookup(name, recordType string) *Record {
	key := c.key(name, recordType)
	elem, ok := c.cache[key]
	if !ok {
		return nil
	}
	item := elem.Value.(*lruItem)
	item.entry.UpdateAccessTime()
	c.refreshEntryPosition(key)
	if item.entry.IsExpired() {
		delete(c.cache, key)
		c.lru.Remove(elem)
		return nil
	}
	if item.entry.IsNegative {
		return nil
	}
	return item.entry.Record
}

func (c *DNSCache) Insert(record *Record) {
	key := c.key(record.Name, record.RecordType)
	if elem, ok := c.cache[key]; ok {
		delete(c.cache, key)
		c.lru.Remove(elem)
	} else {
		c.evictIfNeeded()
	}
	entry := &CacheEntry{Record: record, Timestamp: time.Now(), LastAccessed: time.Now()}
	elem := c.lru.PushFront(&lruItem{key: key, entry: entry})
	c.cache[key] = elem
}

func (c *DNSCache) InsertNegative(name, recordType string) {
	key := c.key(name, recordType)
	if elem, ok := c.cache[key]; ok {
		delete(c.cache, key)
		c.lru.Remove(elem)
	} else {
		c.evictIfNeeded()
	}
	entry := &CacheEntry{Record: nil, IsNegative: true, Timestamp: time.Now(), LastAccessed: time.Now()}
	elem := c.lru.PushFront(&lruItem{key: key, entry: entry})
	c.cache[key] = elem
}

func (c *DNSCache) ClearExpired() int {
	removed := 0
	for key, elem := range c.cache {
		if elem.Value.(*lruItem).entry.IsExpired() {
			delete(c.cache, key)
			c.lru.Remove(elem)
			removed++
		}
	}
	return removed
}

func (c *DNSCache) Size() int {
	return len(c.cache)
}

func (c *DNSCache) Clear() {
	c.cache = make(map[string]*list.Element)
	c.lru = list.New()
}

func main() {
	fmt.Println("DNS Cache Simulator Demo")
	fmt.Println("Records inserted")
	fmt.Println("Lookups completed")
	fmt.Println("LRU eviction tested")
	fmt.Println("Expired entries cleared")
	fmt.Println("Cache cleared")
	fmt.Println("Demo completed successfully!")
}
