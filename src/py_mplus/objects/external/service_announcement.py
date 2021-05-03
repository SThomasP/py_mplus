from py_mplus.objects import MPObject, MPData


class ServiceAnnouncement(MPObject):
    def _decode(self, buffer: MPData, category, skip):
        if category == 1:
            self.title = buffer.string()
        elif category == 2:
            self.body = buffer.string()
        elif category == 3:
            self.date = buffer.int32()
        else:
            buffer.skip_type(skip)

'''
  e.decode = function (e, t) {
    e instanceof x || (e = x.create(e));
    var n = void 0 === t ? e.len : e.pos + t,
    r = new R.Proto.ServiceAnnouncement;
    while (e.pos < n) {
      var a = e.uint32();
      switch (a >>> 3) {
        case 1:
          r.title = e.string();
          break;
        case 2:
          r.body = e.string();
          break;
        case 3:
          r.date = e.int32();
          break;
        default:
          e.skipType(7 & a);
          break
      }
    }
    return r
  }
'''