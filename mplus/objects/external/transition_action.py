from mplus.objects import MPObject
METHODS = ['PUSH', 'MODAL', 'EXTERNAL']


class TransitionAction(MPObject):
    def _decode(self, buffer, a):
        if a == 1:
            self.method = buffer.int32()
        elif a == 2:
            self.url = buffer.string()
        else:
            buffer.skip_type(7 & a)


'''
  e.decode = function (e, t) {
    e instanceof x || (e = x.create(e));
    var n = void 0 === t ? e.len : e.pos + t,
    r = new R.Proto.TransitionAction;
    while (e.pos < n) {
      var a = e.uint32();
      switch (a >>> 3) {
        case 1:
          r.method = e.int32();
          break;
        case 2:
          r.url = e.string();
          break;
        default:
          e.skipType(7 & a);
          break
      }
    }
    return r
'''