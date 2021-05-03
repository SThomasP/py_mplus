from py_mplus.objects import MPData, MPObject
from py_mplus.objects.comment.comment_icon import CommentIcon


class SettingsView(MPObject):
    def _decode(self, buffer: MPData, category, skip):
        if category == 1:
            self.my_icon = CommentIcon(buffer, buffer.uint32())
        elif category == 2:
            self.user_name = buffer.string()
        elif category == 3:
            self.notice_of_news_and_events = buffer.boolean()
        elif category == 4:
            self.notice_of_updates_of_subscribed_titles = buffer.boolean()
        elif category == 5:
            self.english_titles_count = buffer.uint32()
        elif category == 6:
            self.spanish_titles_count = buffer.uint32()
        else:
            buffer.skip_type(skip)


'''
  e.decode = function (e, t) {
    e instanceof x || (e = x.create(e));
    var n = void 0 === t ? e.len : e.pos + t,
    r = new R.Proto.SettingsView;
    while (e.pos < n) {
      var a = e.uint32();
      switch (a >>> 3) {
        case 1:
          r.myIcon = R.Proto.CommentIcon.decode(e, e.uint32());
          break;
        case 2:
          r.userName = e.string();
          break;
        case 3:
          r.noticeOfNewsAndEvents = e.bool();
          break;
        case 4:
          r.noticeOfUpdatesOfSubscribedTitles = e.bool();
          break;
        case 5:
          r.englishTitlesCount = e.uint32();
          break;
        case 6:
          r.spanishTitlesCount = e.uint32();
          break;
        default:
          e.skipType(7 & a);
          break
      }
    }
    return r
  }
'''