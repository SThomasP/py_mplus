from mplus.objects import MPObject


class Chapter(MPObject):
    def _decode(self, buffer, a):
        if a == 1:
            self.title_id = buffer.uint32()
        elif a == 2:
            self.chapter_id = buffer.uint32()
        elif a == 3:
            self.name = buffer.string()
        elif a == 4:
            self.subtitle = buffer.string()  # subtitle
        elif a == 5:
            self.thumbnail = buffer.string()  # thumbnail
        elif a == 6:
            self.start_date = buffer.uint32()
        elif a == 7:
            self.end_date = buffer.uint32()  # end date
        elif a == 8:
            self.already_seen = buffer.boolean()  # already viewed
        elif a == 9:
            self.is_vertical_only = buffer.boolean()  # is vertical only
        else:
            buffer.skip_type(7 & a)



'''
  e.decode = function (e, t) {
    e instanceof x || (e = x.create(e));
    var n = void 0 === t ? e.len : e.pos + t,
    r = new R.Proto.Chapter;
    while (e.pos < n) {
      var a = e.uint32();
      switch (a >>> 3) {
        case 1:
          r.titleId = e.uint32();
          break;
        case 2:
          r.chapterId = e.uint32();
          break;
        case 3:
          r.name = e.string();
          break;
        case 4:
          r.subTitle = e.string();
          break;
        case 5:
          r.thumbnailUrl = e.string();
          break;
        case 6:
          r.startTimeStamp = e.uint32();
          break;
        case 7:
          r.endTimeStamp = e.uint32();
          break;
        case 8:
          r.alreadyViewed = e.bool();
          break;
        case 9:
          r.isVerticalOnly = e.bool();
          break;
        default:
          e.skipType(7 & a);
          break
      }
    }
    return r
'''