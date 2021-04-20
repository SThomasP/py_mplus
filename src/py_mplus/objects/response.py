from py_mplus.objects import MPObject, MPData
from py_mplus.objects.error_result import ErrorResult
from py_mplus.objects.success_result import SuccessResult


class Response(MPObject):
    def _decode(self, buffer: MPData, a, i):
        if a == 1:
            self.success = SuccessResult(buffer, buffer.uint32())
        elif a == 2:
            self.error = ErrorResult(buffer, buffer.uint32())
        else:
            buffer.skip_type(7 & i)


'''
  e.decode = function (e, t) {
    e instanceof x || (e = x.create(e));
    var n = void 0 === t ? e.len : e.pos + t,
    r = new R.Proto.Response;
    while (e.pos < n) {
      var a = e.uint32();
      switch (a >>> 3) {
        case 1:
          r.success = R.Proto.SuccessResult.decode(e, e.uint32());
          break;
        case 2:
          r.error = R.Proto.ErrorResult.decode(e, e.uint32());
          break;
        default:
          e.skipType(7 & a);
          break
      }
    }
    return r
'''