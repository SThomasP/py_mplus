from py_mplus import MPData
from py_mplus.objects import MPObject
from py_mplus.objects.external.banner import Banner
from py_mplus.objects.views.title_detail_view.publisher_news import PublisherNews


class PublisherItem(MPObject):
    def _decode(self, buffer: MPData, a, i):
        if a == 1:
            self.banner = Banner(buffer, buffer.uint32())
        elif a == 2:
            self.publisher_news = PublisherNews(buffer, buffer.uint32())
        else:
            buffer.skip_type(7 & i)


'''
  e.decode = function (e, t) {
    e instanceof p || (e = p.create(e));
    var n = void 0 === t ? e.len : e.pos + t,
    a = new g.Proto.TitleDetailView.PublisherItem;
    while (e.pos < n) {
      var i = e.uint32();
      switch (i >>> 3) {
        case 1:
          a.banner = g.Proto.Banner.decode(e, e.uint32());
          break;
        case 2:
          a.publisherNews = g.Proto.PublisherNews.decode(e, e.uint32());
          break;
        default:
          e.skipType(7 & i);
          break
      }
    }
    return a
  },
'''