from py_mplus.objects import MPObject, MPData
RESPONSES = ['QUESTION', 'ANSWER']


class Feedback(MPObject):
    def _decode(self, buffer: MPData, a, i):
        if a == 1:
            self.time_stamp = buffer.uint32()
        elif a == 2:
            self.body = buffer.string()
        elif a == 3:
            self.response_type = buffer.int32()
        else:
            buffer.skip_type(7 & i)


'''
  e.decode = function (e, t) {
    e instanceof x || (e = x.create(e));
    var n = void 0 === t ? e.len : e.pos + t,
    r = new R.Proto.Feedback;
    while (e.pos < n) {
      var a = e.uint32();
      switch (a >>> 3) {
        case 1:
          r.timeStamp = e.uint32();
          break;
        case 2:
          r.body = e.string();
          break;
        case 3:
          r.responseType = e.int32();
          break;
        default:
          e.skipType(7 & a);
          break
      }
    }
    return r
  }
'''