from py_mplus import MPData
from py_mplus.objects import MPObject


class UserTickets(MPObject):
    def _decode(self, buffer: MPData, a, i):
        if a == 1:
            self.current_ticket = buffer.uint32()
        elif a == 2:
            self.next_ticket_time_stamp = buffer.uint32()
        else:
            buffer.skip_type(7 & i)

'''
e.decode = function (e, t) {
  e instanceof p || (e = p.create(e));
  var n = void 0 === t ? e.len : e.pos + t,
  a = new g.Proto.UserTickets;
  while (e.pos < n) {
    var i = e.uint32();
    switch (i >>> 3) {
      case 1:
        a.currentTickets = e.uint32();
        break;
      case 2:
        a.nextTicketTimestamp = e.uint32();
        break;
      default:
        e.skipType(7 & i);
        break
    }
  }
  return a
},
'''