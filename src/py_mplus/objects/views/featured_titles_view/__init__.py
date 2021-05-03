from py_mplus.objects import MPObject, MPData
from py_mplus.objects.external.banner import Banner
from py_mplus.objects.views.featured_titles_view.contents import Contents


class FeaturedTitlesView(MPObject):
    def _decode(self, buffer: MPData, category, skip):
        if category == 1:
            self.main_banner = Banner(buffer, buffer.uint32())
        elif category == 2:
            self.sub_banner_one = Banner(buffer, buffer.uint32())
        elif category == 3:
            self.sub_banner_two = Banner(buffer, buffer.uint32())
        elif category == 4:
            if not hasattr(self, 'contents'):
                self.contents = []
            self.contents.append(Contents(buffer, buffer.uint32()))
        else:
            buffer.skip_type(skip)

'''
  e.decode = function (e, t) {
    e instanceof x || (e = x.create(e));
    var n = void 0 === t ? e.len : e.pos + t,
    r = new R.Proto.FeaturedTitlesView;
    while (e.pos < n) {
      var a = e.uint32();
      switch (a >>> 3) {
        case 1:
          r.mainBanner = R.Proto.Banner.decode(e, e.uint32());
          break;
        case 2:
          r.subBanner_1 = R.Proto.Banner.decode(e, e.uint32());
          break;
        case 3:
          r.subBanner_2 = R.Proto.Banner.decode(e, e.uint32());
          break;
        case 4:
          r.contents && r.contents.length || (r.contents = [
          ]),
          r.contents.push(R.Proto.FeaturedTitlesView.Contents.decode(e, e.uint32()));
          break;
        default:
          e.skipType(7 & a);
          break
      }
    }
    return r
  }
'''