        A B C D
    A   1 1 0 0
    B   1 1 1 1
    C   0 1 1 1
    D   0 0 1 1

This data has been used to simulate a simple routing of packets using the AODV algo.


AODV is a reactive (or on-demand) MANET routing protocol, and as such, it maintains routes for which there is a demand in the network (i.e. packets are frequently sent on the route). AODV maintains a routing table with the next hop for reaching destinations. Routes time out after a while if not used (i.e. no packets are sent on them). AODV features the following routing message types:

RREQ: Route request

RREP: Route reply

RERR: Route error

When a node wants to send a packet, and it doesn’t know the route to the destination, it initiates route discovery, by sending an RREQ multicast message. The neighboring nodes record where the message came from and forward it to their neighbors until the message gets to the destination node. The destination node replies with an RREP, which gets back to the source on the reverse path along which the RREQ came. 

Forward routes are set up in the intermediate nodes as the RREP travels back to the source. An intermediate node can also send an RREP in reply to a received RREQ if it knows the route to the destination, thus nodes can join an existing route. When the RREP arrives at the source, and the route is created, communication can begin between the source and the destination. If a route no longer works due to link break, i.e. messages cannot be forwarded on it, a RERR message is broadcast by the node which detects the link break. Other nodes re-broadcast the message. 

The RERR message indicates the destination which is unreachable. Nodes receiving the message make the route inactive (and eventually the route is deleted). The next packet to be sent triggers route discovery. As a reactive protocol, generally AODV has less overhead (less route maintenance messages) than proactive ones, but setting up new routes takes time while packets are waiting to be delivered. (Note that the routing protocol overhead depends on the mobility level in the network.)

Additionally, even though AODV is a reactive protocol, nodes can send periodic hello messages to discover links to neighbors and update the status of these links. This mechanism is local (hello messages are only sent to neighbors, and not forwarded), and it can make the network more responsive to local topology changes. By default, hello messages are turned off in INET’s AODV implementation.
