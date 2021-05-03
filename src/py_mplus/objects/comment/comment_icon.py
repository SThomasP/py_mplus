from py_mplus.objects import MPData, MPObject


class CommentIcon(MPObject):
    def _decode(self, buffer: MPData, category, skip):
        if category == 1:
            self.id = buffer.uint32()
        elif category == 2:
            self.image_url = buffer.string()
        else:
            buffer.skip_type(skip)

'''
  e.decode = function (e, t) {
    e instanceof x || (e = x.create(e));
    var n = void 0 === t ? e.len : e.pos + t,
    r = new R.Proto.CommentIcon;
    while (e.pos < n) {
      var a = e.uint32();
      switch (a >>> 3) {
        case 1:
          r.id = e.uint32();
          break;
        case 2:
          r.imageUrl = e.string();
          break;
        default:
          e.skipType(7 & a);
          break
      }
    }
    return r
  }
'''