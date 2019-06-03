CXX = g++
CXXFLAGS = -I/usr/include/python2.7   
LDFLAGS = -L/usr/lib/python2.7 -lpython

src = $(wildcard *.cpp)
obj = $(src:.cpp=.o)

dm_collector_c: $(obj)
	$(CXX) -shared $(LDFLAGS) $^ -o $@  

.NOTHIN: clean
clean:
	rm -f $(obj) dm_collector_c
