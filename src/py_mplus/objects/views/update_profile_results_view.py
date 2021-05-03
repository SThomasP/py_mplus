from py_mplus.objects import MPObject, MPData
RESULTS = ['SUCCESS', 'DUPLICATED', 'NG_WORD']


class UpdateProfileResultsView(MPObject):
    def _decode(self, buffer: MPData, category, skip):
        if category == 1:
            self.result = buffer.int32()
        else:
            buffer.skip_type(skip)

'''
 e.decode = function (e, t) {
    e instanceof x || (e = x.create(e));
    var n = void 0 === t ? e.len : e.pos + t,
    r = new R.Proto.UpdateProfileResultView;
    while (e.pos < n) {
      var a = e.uint32();
      switch (a >>> 3) {
        case 1:
          r.result = e.int32();
          break;
        default:
          e.skipType(7 & a);
          break
      }
    }
    return r
  }
'''