from mplus.objects import MPData, MPObject
from mplus.objects.external.popup.app_default import AppDefault
from mplus.objects.external.popup.os_default import OSDefault


class Popup(MPObject):
    def _decode(self, buffer: MPData, a):
        if a == 1:
            self.os_default = OSDefault(buffer, buffer.uint32())
        elif a == 2:
            self.app_default = AppDefault(buffer, buffer.uint32())
        else:
            buffer.skip_type(7 & a)



'''
  e.decode = function (e, t) {
    e instanceof x || (e = x.create(e));
    var n = void 0 === t ? e.len : e.pos + t,
    r = new R.Proto.Popup;
    while (e.pos < n) {
      var a = e.uint32();
      switch (a >>> 3) {
        case 1:
          r.osDefault = R.Proto.Popup.OSDefault.decode(e, e.uint32());
          break;
        case 2:
          r.appDefault = R.Proto.Popup.AppDefault.decode(e, e.uint32());
          break;
        default:
          e.skipType(7 & a);
          break
      }
    }
    return r
  }
'''

