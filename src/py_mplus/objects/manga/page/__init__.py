from py_mplus.objects import MPObject, MPData
from py_mplus.objects.external.ad_network.ad_network_list import AdNetworkList
from py_mplus.objects.manga.page.banner_list import BannerList
from py_mplus.objects.manga.page.last_page import LastPage
from py_mplus.objects.manga.page.manga_page import MangaPage


class Page(MPObject):
    def _decode(self, buffer: MPData, a):
        if a == 1:
            self.manga_page = MangaPage(buffer, buffer.uint32())
        elif a == 2:
            self.banner_list = BannerList(buffer, buffer.uint32())
        elif a == 3:
            self.last_page = LastPage(buffer, buffer.uint32())
        elif a == 4:
            self.advertisement = AdNetworkList(buffer, buffer.uint32())
        else:
            buffer.skip_type(7 & a)


'''
  e.decode = function (e, t) {
    e instanceof x || (e = x.create(e));
    var n = void 0 === t ? e.len : e.pos + t,
    r = new R.Proto.Page;
    while (e.pos < n) {
      var a = e.uint32();
      switch (a >>> 3) {
        case 1:
          r.mangaPage = R.Proto.Page.MangaPage.decode(e, e.uint32());
          break;
        case 2:
          r.bannerList = R.Proto.Page.BannerList.decode(e, e.uint32());
          break;
        case 3:
          r.lastPage = R.Proto.Page.LastPage.decode(e, e.uint32());
          break;
        case 4:
          r.advertisement = R.Proto.AdNetworkList.decode(e, e.uint32());
          break;
        default:
          e.skipType(7 & a);
          break
      }
    }
    return r
  }
'''