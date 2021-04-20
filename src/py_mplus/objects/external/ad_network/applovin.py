from py_mplus.objects import MPObject, MPData


class AppLoving(MPObject):
    def _decode(self, buffer: MPData, a, i):
        if a == 1:
            self.unit_id = buffer.string()
        else:
            buffer.skip_type(7 & i)

'''
    while (e.pos < n) {
      var i = e.uint32();
      switch (i >>> 3) {
        case 1:
          r.unitID = e.string();
          break;
        default:
          e.skipType(7 & i);
          break
'''