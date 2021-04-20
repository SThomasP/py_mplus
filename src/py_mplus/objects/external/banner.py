from py_mplus.objects import MPObject
from py_mplus.objects.external.transition_action import TransitionAction


class Banner(MPObject):
    def _decode(self, buffer, a, i):
        if a == 1:
            self.image = buffer.string()
        elif a == 2:
            self.action = TransitionAction(buffer, buffer.uint32())
        elif a == 3:
            self.id = buffer.uint32()
        else:
            buffer.skip_type(7 & i)

'''
  e.decode = function (e, t) {
    e instanceof x || (e = x.create(e));
    var n = void 0 === t ? e.len : e.pos + t,
    r = new R.Proto.Banner;
    while (e.pos < n) {
      var a = e.uint32();
      switch (a >>> 3) {
        case 1:
          r.imageUrl = e.string();
          break;
        case 2:
          r.action = R.Proto.TransitionAction.decode(e, e.uint32());
          break;
        case 3:
          r.id = e.uint32();
          break;
        default:
          e.skipType(7 & a);
          break
      }
    }
    return r
'''