from py_mplus.objects import MPObject, MPData
from py_mplus.objects.external.banner import Banner
from py_mplus.objects.manga.title.title_list import TitleList


class Contents(MPObject):
    def _decode(self, buffer: MPData, a):
        if a == 1:
            self.banner = Banner(buffer, buffer.uint32())
        elif a == 2:
            self.title_list = TitleList(buffer, buffer.uint32())
        else:
            buffer.skip_type(7 & a)


'''
    e.decode = function (e, t) {
      e instanceof x || (e = x.create(e));
      var n = void 0 === t ? e.len : e.pos + t,
      r = new R.Proto.FeaturedTitlesView.Contents;
      while (e.pos < n) {
        var a = e.uint32();
        switch (a >>> 3) {
          case 1:
            r.banner = R.Proto.Banner.decode(e, e.uint32());
            break;
          case 2:
            r.titleList = R.Proto.TitleList.decode(e, e.uint32());
            break;
          default:
            e.skipType(7 & a);
            break
        }
      }
      return r
    }
'''