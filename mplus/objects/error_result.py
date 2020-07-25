from mplus.objects import MPObject, MPData
from mplus.objects.external.popup.os_default import OSDefault

ACTIONS = ['DEFAULT', 'MAINTENANCE', 'UNAUTHORIZED', 'GEO-IP BLOCKED']


class ErrorResult(MPObject):
    def _decode(self, buffer: MPData, a):
        if a == 1:
            self.action = buffer.int32()
        elif a == 2:
            self.english_popup = OSDefault(buffer, buffer.uint32())
        elif a == 3:
            self.spanish_popup = OSDefault(buffer, buffer.uint32())
        elif a == 4:
            self.debug_info = buffer.string()
        else:
            buffer.skip_type(7 & a)


'''
e.decode = function (e, t) {
e instanceof x || (e = x.create(e));
var n = void 0 === t ? e.len : e.pos + t,
r = new R.Proto.ErrorResult;
while (e.pos < n) {
  var a = e.uint32();
  switch (a >>> 3) {
    case 1:
      r.action = e.int32();
      break;
    case 2:
      r.englishPopup = R.Proto.Popup.OSDefault.decode(e, e.uint32());
      break;
    case 3:
      r.spanishPopup = R.Proto.Popup.OSDefault.decode(e, e.uint32());
      break;
    case 4:
      r.debugInfo = e.string();
      break;
    default:
      e.skipType(7 & a);
      break
  }
}
return r
}
'''