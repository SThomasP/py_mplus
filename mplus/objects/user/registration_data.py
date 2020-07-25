from mplus.objects import MPObject, MPData


class RegistrationData(MPObject):
    def _decode(self, buffer: MPData, a):
        if a == 1:
            self.device_secret = buffer.string()
        else:
            buffer.skip_type(7 & a)

'''
  e.decode = function (e, t) {
    e instanceof x || (e = x.create(e));
    var n = void 0 === t ? e.len : e.pos + t,
    r = new R.Proto.RegistrationData;
    while (e.pos < n) {
      var a = e.uint32();
      switch (a >>> 3) {
        case 1:
          r.deviceSecret = e.string();
          break;
        default:
          e.skipType(7 & a);
          break
      }
    }
    return r
  }
'''