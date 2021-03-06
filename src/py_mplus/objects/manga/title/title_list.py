from py_mplus.objects import MPObject, MPData
from py_mplus.objects.manga.title import Title


class TitleList(MPObject):
    def _decode(self, buffer: MPData, category, skip):
        if category == 1:
            self.list_name = buffer.string()
        elif category == 2:
            if not hasattr(self, 'featured_titles'):
                self.featured_titles = []
            self.featured_titles.append(Title(buffer, buffer.uint32()))
        else:
            buffer.skip_type(skip)


'''
  e.decode = function (e, t) {
    e instanceof x || (e = x.create(e));
    var n = void 0 === t ? e.len : e.pos + t,
    r = new R.Proto.TitleList;
    while (e.pos < n) {
      var a = e.uint32();
      switch (a >>> 3) {
        case 1:
          r.listName = e.string();
          break;
        case 2:
          r.featuredTitles && r.featuredTitles.length || (r.featuredTitles = [
          ]),
          r.featuredTitles.push(R.Proto.Title.decode(e, e.uint32()));
          break;
        default:
          e.skipType(7 & a);
          break
      }
    }
    return r
  }
'''