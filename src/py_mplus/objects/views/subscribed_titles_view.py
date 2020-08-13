from py_mplus.objects import MPObject, MPData
from py_mplus.objects.manga.title import Title


class SubscribedTitlesView(MPObject):
    def _decode(self, buffer: MPData, a):
        if a == 1:
            if not hasattr(self, 'titles'):
                self.titles = []
            self.titles.append(Title(buffer, buffer.uint32()))
        else:
            buffer.skip_type(7 & a)


'''
  e.decode = function (e, t) {
    e instanceof x || (e = x.create(e));
    var n = void 0 === t ? e.len : e.pos + t,
    r = new R.Proto.SubscribedTitlesView;
    while (e.pos < n) {
      var a = e.uint32();
      switch (a >>> 3) {
        case 1:
          r.titles && r.titles.length || (r.titles = [
          ]),
          r.titles.push(R.Proto.Title.decode(e, e.uint32()));
          break;
        default:
          e.skipType(7 & a);
          break
      }
    }
    return r
  }
'''