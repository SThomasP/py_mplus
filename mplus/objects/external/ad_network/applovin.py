from mplus.objects import MPObject, MPData


class AppLoving(MPObject):
    def _decode(self, buffer: MPData, a):
        if a == 1:
            self.unit_id = buffer.string()
        else:
            buffer.skip_type(7 & a)

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