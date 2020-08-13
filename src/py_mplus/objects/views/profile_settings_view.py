from py_mplus.objects import MPObject, MPData
from py_mplus.objects.comment.comment_icon import CommentIcon


class ProfileSettingsView(MPObject):
    def _decode(self, buffer: MPData, a):
        if a == 1:
            if not hasattr(self, 'icon_list'):
                self.icon_list = []
            self.icon_list.append(CommentIcon(buffer, buffer.uint32()))
        elif a == 2:
            self.user_name = buffer.string()
        elif a == 3:
            self.my_icon = CommentIcon(buffer, buffer.uint32())
        else:
            buffer.skip_type(7 & a)

'''
  e.decode = function (e, t) {
    e instanceof x || (e = x.create(e));
    var n = void 0 === t ? e.len : e.pos + t,
    r = new R.Proto.ProfileSettingsView;
    while (e.pos < n) {
      var a = e.uint32();
      switch (a >>> 3) {
        case 1:
          r.iconList && r.iconList.length || (r.iconList = [
          ]),
          r.iconList.push(R.Proto.CommentIcon.decode(e, e.uint32()));
          break;
        case 2:
          r.userName = e.string();
          break;
        case 3:
          r.myIcon = R.Proto.CommentIcon.decode(e, e.uint32());
          break;
        default:
          e.skipType(7 & a);
          break
      }
    }
    return r
  }
'''