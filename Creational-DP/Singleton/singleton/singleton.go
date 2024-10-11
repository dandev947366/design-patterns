package singleton

// Singleton interface
type Singleton interface {
	AddOne() int
}

type singleton struct {
	count int
}

var instance *singleton

// GetInstance returns the singleton instance
func GetInstance() Singleton {
	// Initialize the instance only once (singleton pattern)
	if instance == nil {
		instance = &singleton{count: 100} // Struct literal should use curly braces
	}
	return instance
}

// AddOne increments the count by one and returns the new value
func (s *singleton) AddOne() int { // Fix method signature with parentheses
	s.count++
	return s.count
}
