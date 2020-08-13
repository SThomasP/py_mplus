from py_mplus.objects import MPObject, MPData
from py_mplus.objects.external.banner import Banner


class BannerList(MPObject):
    def _decode(self, buffer: MPData, a):
        if a == 1:
            self.banner_title = buffer.string()
        elif a == 2:
            if not hasattr(self, 'banners'):
                self.banners = []
            self.banners.append(Banner(buffer, buffer.uint32()))
        else:
            buffer.skip_type(7 & a)


'''
    e.decode = function (e, t) {
      e instanceof x || (e = x.create(e));
      var n = void 0 === t ? e.len : e.pos + t,
      r = new R.Proto.Page.BannerList;
      while (e.pos < n) {
        var a = e.uint32();
        switch (a >>> 3) {
          case 1:
            r.bannerTitle = e.string();
            break;
          case 2:
            r.banners && r.banners.length || (r.banners = [
            ]),
            r.banners.push(R.Proto.Banner.decode(e, e.uint32()));
            break;
          default:
            e.skipType(7 & a);
            break
        }
      }
      return r
    }
'''