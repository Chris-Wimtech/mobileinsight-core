CXX = g++
CXXFLAGS = -fPIC -I/usr/include/python2.7
LDFLAGS = -fPIC -I/usr/lib/python2.7

src = $(wildcard *.cpp)
obj = $(src:.cpp=.o)

dm_collector_c: $(obj)
	$(CXX) -shared $(LDFLAGS) $^ -o $@

.NOTHIN: clean
clean:
	rm -f $(obj) dm_collector_c
