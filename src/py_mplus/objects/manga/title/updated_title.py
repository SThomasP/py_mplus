from py_mplus.objects import MPObject, MPData
from py_mplus.objects.manga.title import Title


class UpdatedTitle(MPObject):
    def _decode(self, buffer: MPData, category, skip):
        if category == 1:
            self.title = Title(buffer, buffer.uint32())
        elif category == 2:
            self.chapter_id = buffer.uint32()
        elif category == 3:
            self.chapter_name = buffer.string()
        elif category == 4:
            self.chapter_sub_title = buffer.string()
        elif category == 5:
            self.is_latest = buffer.boolean()
        elif category == 6:
            self.is_vertical_only = buffer.boolean()
        else:
            buffer.skip_type(skip)


'''
 e.decode = function (e, t) {
    e instanceof x || (e = x.create(e));
    var n = void 0 === t ? e.len : e.pos + t,
    r = new R.Proto.UpdatedTitle;
    while (e.pos < n) {
      var a = e.uint32();
      switch (a >>> 3) {
        case 1:
          r.title = R.Proto.Title.decode(e, e.uint32());
          break;
        case 2:
          r.chapterId = e.uint32();
          break;
        case 3:
          r.chapterName = e.string();
          break;
        case 4:
          r.chapterSubTitle = e.string();
          break;
        case 5:
          r.isLatest = e.bool();
          break;
        case 6:
          r.isVerticalOnly = e.bool();
          break;
        default:
          e.skipType(7 & a);
          break
      }
    }
    return r
  }
'''