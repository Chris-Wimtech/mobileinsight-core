CXX = g++
CXXFLAGS = -I/usr/include/python2.7 -lpython2.7

dm_collector_c: dm_collector_c.o utils.o log_packet.o log_config.o hdlc.o export_manager.o

dm_collector_c.o: consts.h hdlc.h log_config.h log_packet.h export_manager.h
export_manager.o: consts.h export_manager.h hdlc.h log_packet.h log_packet_helper.h
hdlc.o: hdlc.h
log_config.o: consts.h log_config.h
log_packet.o: consts.h log_packet.h
utils.o: utils.h
